from engine.loader import load_scenarios
from engine.config import C, TEST_PARAMS as PARAMS 
from engine.brute_force import brute_force

SCENARIOS = load_scenarios()

def run_brute_force(name):
    scenario = SCENARIOS[name]
    sequence = brute_force(scenario['tasks'], scenario['window'], scenario['energy'], scenario['prev_context'], C, PARAMS)
    return [t.id for t in sequence]

def test_scenariu_1():
    assert run_brute_force('scenariul_1') == ['D', 'A']

def test_capcana_lookahead():
    assert run_brute_force('capcana_lookahead') == ['S1', 'S2']

def test_nimic_nu_incape():
    assert run_brute_force('nimic_nu_incape') == []