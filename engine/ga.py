import random
from engine.fitness import fitness
from engine.greedy import greedy

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

def ga(tasks, window, energy, prev_context, C, params, pop_size=50, generations=300, p_c=0.9, p_m=0.2, k=3, seed=42, history=None):
    rng = random.Random(seed)
    n = len(tasks)
    if n ==0:
        return []

    def score(perm):
        return evaluate([tasks[i] for i in perm], window, energy, prev_context, C, params)

    g_idx = [tasks.index(t) for t in greedy(tasks, window, energy, prev_context, C, params)]
    population = [g_idx + [i for i in range(n) if i not in g_idx]]
    while len(population) < pop_size:
        perm = list(range(n))
        rng.shuffle(perm)
        population.append(perm)

    for _ in range(generations):
        values = [score(p)[0] for p in population]
        best_i = max(range(pop_size), key=lambda i: values[i])
        if history is not None:
                history.append(values[best_i])
        new_population = [population[best_i]]

        while len(new_population) < pop_size:
            parent1 = tournament(population, values, k, rng)
            parent2 = tournament(population, values, k, rng)
            if rng.random() < p_c:
                child = order_crossover(parent1, parent2, rng)
            else:
                child = list(parent1)
            new_population.append(swap_mutation(child, p_m, rng))

        population = new_population

    results = [score(p) for p in population]
    best_i = max(range(pop_size), key=lambda i: results[i][0])
    return results[best_i][1]