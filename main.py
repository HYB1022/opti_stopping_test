import random
import csv

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

    if observe_count < 1:
        observe_count = 1

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

        if run_trial(
            n=n,
            ratio=ratio
        ):
            success_count += 1

    return success_count / trials


# ======================
# 실험 설정
# ======================

RATIOS = [i / 100 for i in range(1, 100)]

TRIALS = 2000

results = []


# ======================
# 시작 안내
# ======================

print("=" * 50)
print("최적 정지 이론 시뮬레이션")
print("잠시만 기다려 주십시오...")
print("초기화 중...")
print("=" * 50)
print()


# ======================
# 시뮬레이션 실행
# ======================

total_count = len(RATIOS)

for current, ratio in enumerate(
    RATIOS,
    start=1
):

    print(
        f"[{current}/{total_count}] "
        f"관찰 비율 {ratio*100:.0f}% 계산 중..."
    )

    success_rate = simulate(
        n=100,
        ratio=ratio,
        trials=TRIALS
    )

    results.append(
        [ratio, success_rate]
    )

    print(
        f"    → 성공률 {success_rate*100:.2f}%"
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
        [
            "ratio",
            "success_rate"
        ]
    )

    writer.writerows(results)

print()
print("results.csv 저장 완료")


# ======================
# 그래프용 리스트 생성
# ======================

ratio_percent = [
    ratio * 100
    for ratio, success in results
]

success_percent = [
    success * 100
    for ratio, success in results
]


# ======================
# 결과 분석
# ======================
# ======================
# 37% 이전 최고
# ======================

before_candidates = [
    item
    for item in results
    if item[0] <= 0.37
]

before_ratio, before_success = max(
    before_candidates,
    key=lambda x: x[1]
)


# ======================
# 최종 결정
# ======================

after_candidates = [
    item
    for item in results
    if item[0] > 0.37
]

final_ratio = before_ratio
final_success = before_success

for ratio, success in after_candidates:

    if success > before_success:

        final_ratio = ratio
        final_success = success
        break


# ======================
# 그래프
# ======================

plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13
plt.rcParams["legend.fontsize"] = 11

plt.figure(figsize=(10, 6))

plt.plot(
    ratio_percent,
    success_percent,
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
    s=120,
    zorder=5
)

plt.annotate(
    (
        f"37% 이전 최고\n"
        f"({before_ratio*100:.0f}%, "
        f"{before_success*100:.2f}%)"
    ),
    xy=(
        before_ratio * 100,
        before_success * 100
    ),
    xytext=(-100, -60),
    textcoords="offset points",
    arrowprops=dict(
        arrowstyle="->"
    ),
    bbox=dict(
        boxstyle="round,pad=0.3",
        alpha=0.85
    )
)

# ----------------------
# 최종 결정
# ----------------------

if final_ratio != before_ratio:

    plt.scatter(
        final_ratio * 100,
        final_success * 100,
        s=120,
        zorder=5
    )

    plt.annotate(
        (
            f"최종 결정\n"
            f"({final_ratio*100:.0f}%, "
            f"{final_success*100:.2f}%)"
        ),
        xy=(
            final_ratio * 100,
            final_success * 100
        ),
        xytext=(50, -40),
        textcoords="offset points",
        arrowprops=dict(
            arrowstyle="->"
        ),
        bbox=dict(
            boxstyle="round,pad=0.3",
            alpha=0.85
        )
    )

else:

    plt.annotate(
        (
            "최종 결정\n"
            "(37% 이전 최고 유지)"
        ),
        xy=(
            before_ratio * 100,
            before_success * 100
        ),
        xytext=(40, 40),
        textcoords="offset points",
        arrowprops=dict(
            arrowstyle="->"
        ),
        bbox=dict(
            boxstyle="round,pad=0.3",
            alpha=0.85
        )
    )

plt.xlabel("관찰 비율 (%)")
plt.ylabel("성공률 (%)")

plt.title(
    "최적 정지 이론(37% 법칙) 시뮬레이션"
)

# 제목과 주석 여백 확보
plt.subplots_adjust(top=0.88)

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig(
    "optimal_stopping_graph.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()

print()
print("그래프 저장 완료")

print(
    f"\n37% 이전 최고 : "
    f"{before_ratio*100:.0f}% "
    f"({before_success*100:.2f}%)"
)

print(
    f"최종 결정 : "
    f"{final_ratio*100:.0f}% "
    f"({final_success*100:.2f}%)"
)