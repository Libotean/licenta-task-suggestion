from engine.loader import load_scenarios
from engine.config import C, PARAMS
from engine.greedy import greedy
from engine.fitness import fitness
from engine.brute_force import brute_force
from engine.ga import ga

def first_id(sequence):
    return sequence[0].id if sequence else None

def main():
    print(f"{'scenariu':22} {'greedy':7} {'ga':7} {'optim':7} {'asteptat':9} {'F greedy':>9} {'F ga':>6} {'F optim':>8} {'dif':>6}")
    for name, scenario in load_scenarios().items():
        args = (scenario["tasks"], scenario["window"], scenario["energy"], scenario["prev_context"], C, PARAMS)
        g_seq = greedy(*args)
        o_seq = brute_force(*args)
        ga_seq = ga(*args)
        
        ga_fit = fitness(ga_seq, scenario["energy"], scenario["prev_context"], C, PARAMS)
        g_fit = fitness(g_seq, scenario["energy"], scenario["prev_context"], C, PARAMS)
        o_fit = fitness(o_seq, scenario["energy"], scenario["prev_context"], C, PARAMS)

        g_sug = first_id(g_seq)
        mark = "OK" if g_sug == scenario["expected"] else "X"
        print(f"{name:22} {str(g_sug):7} {str(first_id(ga_seq)):7} {str(first_id(o_seq)):7} "
              f"{str(scenario['expected']):9} {g_fit:9.2f} {ga_fit:6.2f} {o_fit:8.2f} "
              f"{o_fit - g_fit:6.2f}  {mark}")

if __name__ == "__main__":
    main()