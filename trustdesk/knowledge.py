from dataclasses import dataclass
from pathlib import Path
import re
@dataclass
class Chunk:
    doc_id:str; title:str; text:str; updated_at:str; priority:int
def parse_doc(path):
    raw=path.read_text(encoding="utf-8"); meta={}; body=raw
    if raw.startswith("---"):
        parts=raw.split("---",2)
        if len(parts)==3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k,v=line.split(":",1); meta[k.strip()]=v.strip()
            body=parts[2].strip()
    return meta,body
STOPWORDS=set("a an the is are do does did to for of in on at my your i we you it me can how what when where who will would should could and or if with after before be been am please tell about used has have".split())
def tokenize(text):
    words=re.findall(r"[a-z0-9]+",text.lower()); out=set()
    for w in words:
        if w=="cancelled": w="cancel"
        if w in STOPWORDS: continue
        if len(w)>4 and w.endswith("ies"): w=w[:-3]+"y"
        elif len(w)>4 and w.endswith("s") and not w.endswith("ss"): w=w[:-1]
        elif len(w)>5 and w.endswith("ed"): w=w[:-2]
        out.add(w)
    return out
class KnowledgeBase:
    def __init__(self,directory="knowledge"): self.directory=Path(directory); self.chunks=[]; self.reload()
    def reload(self):
        self.chunks=[]
        for path in sorted(self.directory.glob("*.md")):
            meta,body=parse_doc(path)
            if meta.get("status","active")!="active": continue
            heading=meta.get("title",path.stem)
            for line in body.splitlines():
                line=line.strip()
                if not line: continue
                if line.startswith("#"): heading=line.lstrip("# ").strip(); continue
                paragraph=f"{meta.get('title',path.stem)}. {heading}. {line}"
                self.chunks.append(Chunk(meta.get("doc_id",path.stem),meta.get("title",path.stem),paragraph,meta.get("updated_at","unknown"),int(meta.get("priority",0))))
        return len(self.chunks)
    def search(self,query,limit=4):
        q=tokenize(query)
        if not q: return []
        scored=[]
        for c in self.chunks:
            terms=tokenize(c.text); overlap=len(q&terms); score=overlap/max(1,len(q))
            if overlap: scored.append((score,c.priority,c))
        scored.sort(key=lambda x:(x[0],x[1]),reverse=True)
        return [{"score":round(s,3),"doc_id":c.doc_id,"title":c.title,"text":c.text,"updated_at":c.updated_at,"matches":len(q&tokenize(c.text))} for s,_,c in scored[:limit]]
