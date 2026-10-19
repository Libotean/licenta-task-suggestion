import math
from engine.models import Task
from engine.fitness import fitness

C = {
    ('Programare', 'Research'): 0.2, ('Programare', 'Housework') : 0.8,
    ("Research", "Programare"): 0.2, ("Research", "Housework"): 0.7,
    ("Housework", "Programare"): 0.6, ("Housework", "Research"): 0.5,
}

PARAMS = {'w1': 1, 'w2': 1, 'w3': 1, 'lam': 1, 'alpha': 0.2, 'default_cost': 0.5}

A = Task("A", 40, 0.75, 0.75, 1.0, "Programare")
B = Task("B", 20, 0.5, 0.25, 0.5, "Research")
Cv = Task("C", 15, 0.25, 0.25, 0.0, "Housework")
D = Task("D", 20, 0.5, 0.25, 0.5, "Programare")

def test_a_d():
    assert math.isclose(fitness([A, D], 0.5, "Programare", C, PARAMS), 1.55)

def test_a_c():
    assert math.isclose(fitness([A, Cv], 0.5, "Programare", C, PARAMS), 0.7)

def test_d_b_c():
    assert math.isclose(fitness([D, B, Cv], 0.5, "Programare", C, PARAMS), 1.0)