from engine.generator import generate_scenario

def test_numar_task_uri():
    assert len(generate_scenario(50, seed=1)["tasks"]) == 50

def test_acelasi_seed_acelasi_scenariu():
    assert generate_scenario(30, seed=5) == generate_scenario(30, seed=5)

def test_seed_diferit_scenariu_diferit():
    assert generate_scenario(30, seed=5) != generate_scenario(30, seed=6)

def test_valori_in_intervale():
    for t in generate_scenario(100, seed=3)["tasks"]:
        assert 0 <= t.importance <= 1
        assert 0 <= t.urgency <=1
        assert t.effort in (0.0, 0.5, 1.0)
        assert t.duration > 0