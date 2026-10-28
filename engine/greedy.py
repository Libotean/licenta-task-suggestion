from engine.fitness import step_value

def greedy(tasks, window, energy, prev_context, C, params):
    sequence = []
    available = list(tasks)
    remaining = window

    while True:
        candidates = [t for t in available if t.duration <= remaining]
        if not candidates:
            break

        best = max(candidates, key=lambda t: step_value(t, energy, prev_context, C, params))
        value = step_value(best, energy, prev_context, C, params)

        if sequence and value <= 0:
            break

        sequence.append(best)
        available.remove(best)
        remaining -= best.duration
        energy = max(0.0, energy - params['alpha'] * best.effort)
        prev_context = best.context

    return sequence