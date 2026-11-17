import json
from pathlib import Path
from .engine import SupportEngine
def main():
    cases=json.loads(Path("evaluation/questions.json").read_text(encoding="utf-8")); engine=SupportEngine()
    correct=total=hits=0; rows=[]
    for c in cases:
        r=engine.answer(c["question"]); ok=r["status"]==c["expected_status"]; correct+=int(ok)
        source=c.get("expected_source"); found=None
        if source:
            total+=1; found=any(x["doc_id"]==source for x in engine.kb.search(c["question"],limit=4)); hits+=int(found)
        rows.append((c["id"],ok,found,r["status"],c["expected_status"]))
    print(f"Decision accuracy: {correct}/{len(cases)} = {correct/len(cases):.1%}")
    print(f"Retrieval hit@4: {hits}/{total} = {hits/max(1,total):.1%}")
    print("NOTE: synthetic fixture evaluation only; not a company-data quality claim.")
    for row in rows:
        if not row[1] or row[2] is False: print("MISMATCH",row)
if __name__=="__main__": main()
