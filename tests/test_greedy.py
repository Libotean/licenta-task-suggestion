from engine.loader import load_scenarios
from engine.greedy import greedy

C = {
    ("Programare", "Research"): 0.2, ("Programare", "Housework"): 0.8,
    ("Research", "Programare"): 0.2, ("Research", "Housework"): 0.7,
    ("Housework", "Programare"): 0.6, ("Housework", "Research"): 0.5,
}

PARAMS = {"w1": 1, "w2": 1, "w3": 1, "lam": 1, "alpha": 0.2, "default_cost": 0.5}
SCENARIOS = load_scenarios()

def run_greedy(name):
    scenario = SCENARIOS[name]
    sequence = greedy(scenario['tasks'], scenario['window'], scenario['energy'], scenario['prev_context'], C, PARAMS)
    return [t.id for t in sequence]

def test_scenariu_1():
    assert run_greedy('scenariul_1') == ['A', 'D']

def test_capcana_lookahead():
    assert run_greedy('capcana_lookahead') == ['L']