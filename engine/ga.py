import random
from engine.fitness import fitness

def decode(perm, window):
    sequence = []
    remaining = window
    for task in perm:
        if task.duration <= remaining:
            sequence.append(task)
            remaining -= task.duration
    return sequence

def evaluate(perm, window, energy, prev_context, C, params):
    sequence = decode(perm, window)
    if not sequence:
        return 0.0, []

    best_value, best_sequence = float("-inf"), []
    for k in range(1, len(sequence) + 1):
        value = fitness(sequence[:k], energy, prev_context, C, params)
        if value > best_value:
            best_value, best_sequence = value, sequence[:k]
    return best_value, best_sequence

def random_search(tasks, window, energy, prev_context, C, params, n=200, seed=42):
    rng = random.Random(seed)
    best_value, best_sequence = float("-inf"), []

    for _ in range(n):
        perm = list(tasks)
        rng.shuffle(perm)
        value, sequence = evaluate(perm, window, energy, prev_context, C, params)
        if value > best_value:
            best_value, best_sequence = value, sequence

    return best_sequence

