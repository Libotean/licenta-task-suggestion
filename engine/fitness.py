def fitness(sequence, energy, prev_context, C, params):
    total = 0.0

    for task in sequence:

        total += step_value(task, energy, prev_context, C, params)

        energy = max(0.0, energy - params['alpha'] * task.effort)
        prev_context = task.context
    
    return total

def step_value(task, energy, prev_context, C, params):
    # scorul task-ului la energia curenta
    mismatch = max(0.0, task.effort - energy)
    score = (params['w1'] * task.importance
             + params['w2'] * task.urgency
             - params['w3'] * mismatch)

    # costul schimbarii contextului
    if prev_context is None or prev_context == task.context:
        cost = 0.0
    else: 
        cost = C.get((prev_context, task.context), params['default_cost'])

    return score - params['lam'] * cost