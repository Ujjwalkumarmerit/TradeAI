"""Offline lexical-overlap versus BM25 comparison on synthetic data."""
import json,math,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from trustdesk.knowledge import KnowledgeBase,tokenize
def bm25(query,chunks,k1=1.5,b=0.75):
    q=tokenize(query); docs=[tokenize(c.text) for c in chunks]
    if not q or not docs:return []
    avgdl=sum(map(len,docs))/len(docs); df=Counter(t for d in docs for t in set(d)); scored=[]
    for c,terms in zip(chunks,docs):
        counts=Counter(terms); dl=len(terms); score=0.0
        for term in q:
            if counts[term]:
                idf=math.log(1+(len(docs)-df[term]+0.5)/(df[term]+0.5)); tf=counts[term]
                score+=idf*(tf*(k1+1))/(tf+k1*(1-b+b*dl/max(avgdl,1)))
        if score:scored.append((score,c.priority,c.doc_id))
    scored.sort(key=lambda x:(x[0],x[1]),reverse=True)
    return [d for _,_,d in scored[:4]]
def main():
    kb=KnowledgeBase(str(ROOT/"knowledge")); cases=json.loads((ROOT/"evaluation/questions.json").read_text(encoding="utf-8")); cases=[c for c in cases if c.get("expected_source")]
    a=b=0
    for c in cases:
        a+=c["expected_source"] in [x["doc_id"] for x in kb.search(c["question"],4)]
        b+=c["expected_source"] in bm25(c["question"],kb.chunks)
    n=len(cases)
    print(f"Fixture cases with expected source: {n}")
    print(f"Existing lexical overlap hit@4: {a}/{n} ({a/n:.1%})")
    print(f"BM25 alternative hit@4:       {b}/{n} ({b/n:.1%})")
    print("Descriptive result on a small synthetic fixture; not production evidence.")
if __name__=="__main__":main()
