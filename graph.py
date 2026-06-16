import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

plt.figure(figsize=(8, 5))

plt.plot(
    df["ratio"],
    df["success_rate"],
    marker="o"
)

plt.xlabel("Observation Ratio")
plt.ylabel("Success Rate")
plt.title("Optimal Stopping Simulation")

plt.grid(True)

plt.savefig(
    "optimal_stopping_graph.png",
    dpi=300
)

plt.show()