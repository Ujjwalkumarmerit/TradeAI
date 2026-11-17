import json
from pathlib import Path
import pytest
from trustdesk.engine import SupportEngine
from scripts.evaluate_adversarial import assess
CASES=json.loads((Path(__file__).resolve().parents[1]/"evaluation/adversarial.json").read_text(encoding="utf-8"))
@pytest.mark.parametrize("index,case",list(enumerate(CASES)))
def test_adversarial_case_has_safe_expected_behavior(index,case):
    passed,_=assess(index,SupportEngine(generator=None).answer(case["input"]))
    assert passed
