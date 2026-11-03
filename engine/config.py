C = {
    ('Programare', 'Research'): 0.2, ('Programare', 'Housework'): 0.8,
    ("Research", "Programare"): 0.2, ("Research", "Housework"): 0.7,
    ("Housework", "Programare"): 0.6, ("Housework", "Research"): 0.5,
}

TEST_PARAMS = {'w1': 1, 'w2': 1, 'w3': 1, 'lam': 1, 'alpha': 0.2, 'default_cost': 0.5}

PARAMS = {'w1': 1, 'w2': 1, 'w3': 1, 'lam': 0.5, 'alpha': 0.2, 'default_cost': 0.5}

HORIZON_H = 72 
# daca raman mai mult de 3 zile de rezerva, 
# task-ul nu e deloc urgent, 
# iar in ultimele 3 zile urgenta creste treptat pana la 1 