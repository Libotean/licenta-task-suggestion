import math
from engine.loader import load_scenarios
from engine.config import C, TEST_PARAMS as PARAMS
from engine.ga import decode, evaluate

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