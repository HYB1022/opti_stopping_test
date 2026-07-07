import random
import csv

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# ======================
# 한글 폰트 설정
# ======================

font_candidates = [
    "Malgun Gothic",
    "AppleGothic",
    "NanumGothic"
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


def simulate(n=100, ratio=0.37, trials=2000):

    success_count = 0

    for _ in range(trials):

        if run_trial(n, ratio):
            success_count += 1

    return success_count / trials


# ======================
# 실험 설정
# ======================

RATIOS = [i / 100 for i in range(1, 100)]

TRIALS = 2000

results = []

print("=" * 50)
print("최적 정지 이론 시뮬레이션")
print("=" * 50)

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
        f"관찰 비율 {ratio*100:.0f}% "
        f"→ 성공률 {success_rate*100:.2f}%"
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

    writer.writerow(
        ["ratio", "success_rate"]
    )

    writer.writerows(results)

print("\nresults.csv 저장 완료")


# ======================
# 데이터프레임
# ======================

df = pd.DataFrame(
    results,
    columns=[
        "ratio",
        "success_rate"
    ]
)

df["ratio_percent"] = df["ratio"] * 100
df["success_percent"] = df["success_rate"] * 100


# ======================
# 전체 최고점
# ======================

max_idx = df["success_rate"].idxmax()

best_ratio = df.loc[max_idx, "ratio"]
best_success = df.loc[max_idx, "success_rate"]


# ======================
# 37% 이전 최고
# ======================

before_df = df[df["ratio"] <= 0.37]

before_idx = before_df["success_rate"].idxmax()

before_ratio = df.loc[before_idx, "ratio"]
before_success = df.loc[before_idx, "success_rate"]


# ======================
# 37% 이후 최고
# ======================

after_df = df[df["ratio"] > 0.37]

after_idx = after_df["success_rate"].idxmax()

after_ratio = df.loc[after_idx, "ratio"]
after_success = df.loc[after_idx, "success_rate"]


# ======================
# 그래프
# ======================

plt.figure(figsize=(12, 7))

plt.plot(
    df["ratio_percent"],
    df["success_percent"],
    linewidth=2
)

# 37% 기준선
plt.axvline(
    x=37,
    linestyle="--",
    alpha=0.8,
    label="37% 법칙"
)

# ----------------------
# 37% 이전 최고
# ----------------------

plt.scatter(
    before_ratio * 100,
    before_success * 100,
    s=120
)

plt.annotate(
    f"37% 이전 최고\n({before_ratio*100:.0f}%, {before_success*100:.2f}%)",
    (
        before_ratio * 100,
        before_success * 100
    )
)

# ----------------------
# 37% 이후 최고
# ----------------------

if after_idx != before_idx:

    plt.scatter(
        after_ratio * 100,
        after_success * 100,
        s=120
    )

    plt.annotate(
        f"37% 이후 최고\n({after_ratio*100:.0f}%, {after_success*100:.2f}%)",
        (
            after_ratio * 100,
            after_success * 100
        )
    )

# ----------------------
# 전체 최고
# ----------------------

if max_idx not in [before_idx, after_idx]:

    plt.scatter(
        best_ratio * 100,
        best_success * 100,
        s=150
    )

    plt.annotate(
        f"전체 최고\n({best_ratio*100:.0f}%, {best_success*100:.2f}%)",
        (
            best_ratio * 100,
            best_success * 100
        )
    )

# ----------------------

plt.xlabel("관찰 비율 (%)")
plt.ylabel("성공률 (%)")

plt.title(
    "최적 정지 이론(37% 법칙) 시뮬레이션"
)

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    "optimal_stopping_graph.png",
    dpi=300
)

plt.show()


print("\n그래프 저장 완료")

print(
    f"\n전체 최고 성공률 : "
    f"{best_success*100:.2f}%"
)

print(
    f"최적 관찰 비율 : "
    f"{best_ratio*100:.0f}%"
)