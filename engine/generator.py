import random
from engine.models import Task

CONTEXTS = ("Programare", "Research", "Housework")

def generate_scenario(n, seed, window=180):
    rng = random.Random(seed)
    tasks = []
    for i in range(n):
        tasks.append(Task(
            id=f"T{i}",
            duration=rng.choice([15, 20, 30, 45, 60, 90]),
            importance=rng.choice([0.0, 0.25, 0.5, 0.75, 1.0]),
            urgency=round(rng.random(), 2),
            effort=rng.choice([0.0, 0.5, 1.0]),
            context=rng.choice(CONTEXTS),
        ))
    return {
        "name": f"n{n}_s{seed}",
        "window": window,
        "energy": rng.choice([0.0, 0.25, 0.5, 0.75, 1.0]),
        "prev_context": rng.choice(CONTEXTS),
        "tasks": tasks,
    }