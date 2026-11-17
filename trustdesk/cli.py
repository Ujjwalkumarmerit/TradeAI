import argparse, json
from .engine import SupportEngine
def main():
    p=argparse.ArgumentParser()
    p.add_argument("message"); p.add_argument("--order-id"); p.add_argument("--email")
    a=p.parse_args()
    print(json.dumps(SupportEngine().answer(a.message,a.order_id,a.email),indent=2))
if __name__=="__main__": main()
