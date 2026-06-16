import random
import math

N = 100

candidates = list(range(1, N + 1))
random.shuffle(candidates)

observe_count = int(N / math.e)

print(f"관찰 인원: {observe_count}")