import math
from engine.loader import load_scenarios
from engine.fitness import fitness
from engine.config import C, PARAMS

SCENARIOS = load_scenarios()

def fitness_for(order):
    scenario = SCENARIOS["scenariul_1"]
    by_id = {t.id: t for t in scenario['tasks']}
    sequence = [by_id[i] for i in order]
    return fitness(sequence, scenario['energy'], scenario['prev_context'], C, PARAMS)

def test_a_d():
    assert math.isclose(fitness_for(["A", "D"]), 1.55)

def test_a_c():
    assert math.isclose(fitness_for(["A", "C"]), 0.7)

def test_d_b_c():
    assert math.isclose(fitness_for(["D", "B", "C"]), 1.0)

def test_d_a():
    assert math.isclose(fitness_for(["D", "A"]), 1.65)