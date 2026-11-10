import time
import statistics
from engine.generator import generate_scenario
from engine.config import C, PARAMS
from engine.fitness import fitness
from engine.greedy import greedy
from engine.ga import ga, random_search

SIZES = [30, 50, 100]
SCENARIO_SEEDS = range(1, 6)
RUN_SEEDS = range(10)
POP, GENS = 50, 300
BUDGET = POP * GENS

def timed(fn, *args, **kwargs):
    start = time.perf_counter()
    result = fn(*args, **kwargs)
    return result, time.perf_counter() - start

def main():
    for size in SIZES:
        print(f"\n=== Scenarii cu {size} task-uri ===")
        print(f"{'scenariu':10} {'greedy':>8} {'random':>8} {'ga':>8} "
              f"{'ga-greedy':>10} {'ga-random':>10} {'abatere ga':>11} {'timp ga':>9}")
        diffs_greedy, diffs_random = [], []

        for sc_seed in SCENARIO_SEEDS:
            s = generate_scenario(size, sc_seed)
            args = (s["tasks"], s["window"], s["energy"], s["prev_context"], C, PARAMS)

            def fit(seq):
                return fitness(seq, s["energy"], s["prev_context"], C, PARAMS)

            f_g = fit(greedy(*args))
            f_r, f_ga, t_ga = [], [], []
            for run_seed in RUN_SEEDS:
                f_r.append(fit(random_search(*args, n=BUDGET, seed=run_seed)))
                seq, t = timed(ga, *args, pop_size=POP, generations=GENS, seed=run_seed)
                f_ga.append(fit(seq))
                t_ga.append(t)

            m_r, m_ga = statistics.mean(f_r), statistics.mean(f_ga)
            diffs_greedy.append(m_ga - f_g)
            diffs_random.append(m_ga - m_r)
            print(f"{s['name']:10} {f_g:8.2f} {m_r:8.2f} {m_ga:8.2f} "
                  f"{m_ga - f_g:+10.2f} {m_ga - m_r:+10.2f} "
                  f"{statistics.stdev(f_ga):11.2f} {statistics.mean(t_ga):8.3f}s")

        print(f"{'medie':10} {'':8} {'':8} {'':8} "
              f"{statistics.mean(diffs_greedy):+10.2f} {statistics.mean(diffs_random):+10.2f}")

if __name__ == "__main__":
    main()