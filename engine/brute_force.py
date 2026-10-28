from engine.fitness import fitness

def brute_force(tasks, window, energy, prev_context, C, params):

    def explore(sequence, remaining, available):
        best_value = float('-inf')
        best_sequence = []

        if sequence:
            best_value = fitness(sequence, energy, prev_context, C, params)
            best_sequence = sequence

        for i, task in enumerate(available):
            if task.duration <= remaining:
                rest = available[:i] + available[i+1:]
                value, seq = explore(sequence + [task], remaining - task.duration, rest)
                if value > best_value:
                    best_value = value
                    best_sequence = seq

        return best_value, best_sequence

    best_value, best_sequence = explore([], window, list(tasks))
    return best_sequence