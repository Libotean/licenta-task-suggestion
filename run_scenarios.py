from engine.loader import load_scenarios
from engine.config import C, PARAMS
from engine.greedy import greedy
from engine.fitness import fitness

def first_id(sequence):
    return sequence[0].id if sequence else None

def main():
    print(f"{'scenariu':22} {'greedy':8} {'asteptat':9} {'fitness':>9}")
    for name, scenario in load_scenarios().items():
        sequence = greedy(scenario['tasks'], scenario['window'], scenario['energy'], scenario['prev_context'], C, PARAMS)
        fitness_val = fitness(sequence, scenario['energy'], scenario['prev_context'], C, PARAMS)
        suggestion = first_id(sequence)
        mark = 'OK' if suggestion == scenario['expected'] else 'X'
        print(f"{name:22} {str(suggestion):8} {str(scenario['expected']):9} {fitness_val:6.2f} {mark}")

if __name__ == "__main__":
    main()