import csv

from simulation import simulate

RATIOS = [
    0.10,
    0.20,
    0.30,
    0.37,
    0.40,
    0.50,
    0.60,
    0.70,
]

TRIALS = 10000

results = []

print("실험 시작...\n")

for ratio in RATIOS:
    success_rate = simulate(
        n=100,
        ratio=ratio,
        trials=TRIALS
    )

    results.append(
        [ratio, success_rate]
    )

    print(
        f"{ratio:.2f} → "
        f"{success_rate:.4f}"
    )

with open(
    "results.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:
    writer = csv.writer(f)

    writer.writerow(
        ["ratio", "success_rate"]
    )

    writer.writerows(results)

print("\nresults.csv 저장 완료")