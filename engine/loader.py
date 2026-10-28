import json
from pathlib import Path
from engine.models import Task

SCENARIOS_PATH = Path(__file__).parent / "scenarios" / "scenarios.json"

def load_scenarios(path = SCENARIOS_PATH):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for s in data:
        s['tasks'] = [Task(**t) for t in s['tasks']]
    return {s['name']: s for s in data}
