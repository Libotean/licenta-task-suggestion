import matplotlib.pyplot as plt
from engine.generator import generate_scenario
from engine.config import C, PARAMS
from engine.ga import ga

GENS = 300
s = generate_scenario(100, seed=1)
args = (s["tasks"], s["window"], s["energy"], s["prev_context"], C, PARAMS)

for seed in range(5):
    history = []
    ga(*args, generations=GENS, seed=seed, history=history)
    plt.plot(history, label=f"seed {seed}")

plt.xlabel("Generatia")
plt.ylabel("Fitness-ul celui mai bun individ")
plt.title(f"Convergenta GA – scenariul {s['name']}")
plt.legend()
plt.grid(True)
plt.savefig(f"convergenta_{s['name']}.png", dpi=150)
plt.show()