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

def tournament(population, values, k, rng):
    contenders = rng.sample(range(len(population)), k)
    best = max(contenders, key=lambda i: values[i])
    return population[best]

def order_crossover(parent1, parent2, rng):
    n = len(parent1)
    if n < 2:
        return list(parent1)

    a, b = sorted(rng.sample(range(n), 2))
    child = [None] * n
    child[a:b + 1] = parent1[a:b + 1]
    taken = set(parent1[a:b + 1])
    fill = [gene for gene in parent2 if gene not in taken]
    j = 0
    for i in range(n):
        if child[i] is None:
            child[i] = fill[j]
            j += 1
    return child

def swap_mutation(perm, p_m, rng):
    perm = list(perm)
    if len(perm) >= 2 and rng.random() < p_m:
        i, j = rng.sample(range(len(perm)), 2)
        perm[i], perm[j] = perm[j], perm[i]
    return perm