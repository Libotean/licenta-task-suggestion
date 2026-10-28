from engine.loader import load_scenarios
from engine.greedy import greedy
from engine.config import C, PARAMS

SCENARIOS = load_scenarios()

def run_greedy(name):
    scenario = SCENARIOS[name]
    sequence = greedy(scenario['tasks'], scenario['window'], scenario['energy'], scenario['prev_context'], C, PARAMS)
    return [t.id for t in sequence]

def test_scenariu_1():
    assert run_greedy('scenariul_1') == ['A', 'D']

def test_capcana_lookahead():
    assert run_greedy('capcana_lookahead') == ['L']