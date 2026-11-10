import math
from engine.loader import load_scenarios
from engine.config import C, TEST_PARAMS as PARAMS
from engine.ga import decode, evaluate, random_search, ga
from engine.greedy import greedy
from engine.fitness import fitness

SCENARIOS = load_scenarios()

def perm_of(name, order):
    by_id = {t.id: t for t in SCENARIOS[name]["tasks"]}
    return [by_id[i] for i in order]

def test_decode_sare_ce_nu_incape():
    perm = perm_of("scenariul_1", ["A", "C", "B", "D"])
    assert [t.id for t in decode(perm, 60)] == ["A", "C"]

def test_decode_capcana():
    perm = perm_of("capcana_lookahead", ["L", "S1", "S2"])
    assert [t.id for t in decode(perm, 60)] == ["L"]

def test_evaluate_taie_prefixul_prost():
    s = SCENARIOS["scenariul_1"]
    perm = perm_of("scenariul_1", ["D", "B", "C", "A"])
    value, seq = evaluate(perm, s["window"], s["energy"], s["prev_context"], C, PARAMS)
    assert [t.id for t in seq] == ["D", "B"]
    assert math.isclose(value, 1.2)

def run_random(name, seed=42):
    s = SCENARIOS[name]
    sequence = random_search(s["tasks"], s["window"], s["energy"], s["prev_context"], C, PARAMS, seed=seed)
    return [t.id for t in sequence]

def test_random_gaseste_optimul_capcana():
    assert run_random("capcana_lookahead") == ["S1", "S2"]

def test_random_gaseste_optimul_scenariul_1():
    assert run_random("scenariul_1") == ["D", "A"]

def test_random_nimic_nu_incape():
    assert run_random("nimic_nu_incape") == []

# NFR-09: acelasi seed, acelasi rezultat
def test_random_reproductivil():
    assert run_random("scenariul_1", seed=7) == run_random("scenariul_1", seed=7)

def run_ga(name, seed=42):
    s = SCENARIOS[name]
    seq = ga(s["tasks"], s["window"], s["energy"], s["prev_context"], C, PARAMS, seed=seed)
    return [t.id for t in seq]

def test_ga_capcana():
    assert run_ga("capcana_lookahead") == ["S1", "S2"]

def test_ga_scenariul_1():
    assert run_ga("scenariul_1") == ["D", "A"]

def test_ga_nimic_nu_incape():
    assert run_ga("nimic_nu_incape") == []

def test_ga_reproductibil():
    assert run_ga("scenariul_1", seed=7) == run_ga("scenariul_1", seed=7)

def test_ga_nu_e_mai_slab_decat_greedy():
    for name, s in SCENARIOS.items():
        args = (s["tasks"], s["window"], s["energy"], s["prev_context"], C, PARAMS)
        f_ga = fitness(ga(*args), s["energy"], s["prev_context"], C, PARAMS)
        f_greedy = fitness(greedy(*args), s["energy"], s["prev_context"], C, PARAMS)
        assert f_ga >= f_greedy - 1e-9

def test_ga_istoric():
    s = SCENARIOS["scenariul_1"]
    history = []
    ga(s["tasks"], s["window"], s["energy"], s["prev_context"], C, PARAMS,
       generations=30, history=history)
    assert len(history) == 30
    assert all(a <= b for a, b in zip(history, history[1:]))