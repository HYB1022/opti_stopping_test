import random


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
    success = 0

    for _ in range(trials):
        if run_trial(n, ratio):
            success += 1

    return success / trials