import random
import csv

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# ======================
# 한글 폰트 설정
# ======================

font_candidates = [
    "Malgun Gothic",      # Windows
    "AppleGothic",        # macOS
    "NanumGothic"         # Linux
]

available_fonts = {
    f.name for f in fm.fontManager.ttflist
}

for font in font_candidates:
    if font in available_fonts:
        plt.rcParams["font.family"] = font
        break

plt.rcParams["axes.unicode_minus"] = False


# ======================
# 최적 정지 이론
# ======================

def run_trial(n=100, ratio=0.37):

    candidates = list(range(1, n + 1))
    random.shuffle(candidates)

    observe_count = int(n * ratio)

    best_seen = max(candidates[:observe_count])

    selected = None

    for candidate in candidates[observe_count:]:

        if candidate > best_seen:
            selected = candidate
            break

    if selected is None:
        selected = candidates[-1]

    return selected == max(candidates)


def simulate(
    n=100,
    ratio=0.37,
    trials=10000
):

    success_count = 0

    for _ in range(trials):

        if run_trial(n, ratio):
            success_count += 1

    return success_count / trials


# ======================
# 실험 설정
# ======================

RATIOS = [
    0.10,
    0.20,
    0.30,
    0.37,
    0.40,
    0.50,
    0.60,
    0.70,
    0.80,
    0.90,
    1
]

TRIALS = 10000

results = []

print("=" * 40)
print("최적 정지 이론 시뮬레이션")
print("=" * 40)

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
        f"관찰 비율 {ratio:.2f} "
        f"→ 성공률 {success_rate:.4f}"
    )


# ======================
# CSV 저장
# ======================

with open(
    "results.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "ratio",
        "success_rate"
    ])

    writer.writerows(results)

print("\nresults.csv 저장 완료")


# ======================
# 그래프 출력
# ======================

df = pd.DataFrame(
    results,
    columns=[
        "ratio",
        "success_rate"
    ]
)

plt.figure(figsize=(10, 6))

plt.plot(
    df["ratio"],
    df["success_rate"],
    marker="o"
)

plt.xlabel("관찰 비율")
plt.ylabel("성공률")
plt.title("최적 정지 이론(37% 법칙) 시뮬레이션")

plt.grid(True)

max_idx = df["success_rate"].idxmax()

best_ratio = df.loc[max_idx, "ratio"]
best_success = df.loc[max_idx, "success_rate"]

plt.annotate(
    f"최적 비율\n({best_ratio:.2f}, {best_success:.3f})",
    xy=(best_ratio, best_success),
    xytext=(best_ratio + 0, best_success - 0.03),
)

plt.tight_layout()

plt.savefig(
    "optimal_stopping_graph.png",
    dpi=600
)

plt.show()

print("\noptimal_stopping_graph.png 저장 완료")

print(
    f"\n가장 높은 성공률: "
    f"{best_success:.4f}"
)

print(
    f"관찰 비율: "
    f"{best_ratio:.2f}"
)