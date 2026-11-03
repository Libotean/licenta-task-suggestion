import math
from datetime import datetime, timedelta
from engine.urgency import urgency

NOW = datetime(2026, 11, 3, 18, 0)

def test_fara_deadline():
    assert urgency(None, NOW, 60, 72) == 0.0

def test_deadline_departe():
    assert urgency(NOW + timedelta(days=10), NOW, 120, 72) == 0.0

def test_deadline_in_doua_zile():
    assert math.isclose(urgency(NOW + timedelta(days=2), NOW, 120, 72), 1 - 46 / 72)

def test_deadline_aproape():
    assert math.isclose(urgency(NOW + timedelta(hours=6), NOW, 120, 72), 1 - 4 / 72)

def test_nu_mai_incape():
    assert urgency(NOW + timedelta(hours=3), NOW, 240, 72) == 1.0