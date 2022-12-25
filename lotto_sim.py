import random
import numpy as np
from collections import Counter


# params of lotto
N_CHOSEN_NUMBERS = 6
N_TOTAL_NUMBERS = 49
ALL_NUMBERS = range(1, N_TOTAL_NUMBERS + 1)
# param of theoretical approximation
ALPHA = 2.2


def theoretical_diff(n_draws: int, alpha: float = ALPHA) -> float:
    # (mu + alpha * sigma) / (mu - alpha * sigma) = (np + alpha * sqrt(n * p * (1 - p))) / (np - alpha * sqrt(n * p * (1 - p)))
    # = (sqrt(np) + alpha * sqrt(1 - p)) / (sqrt(np) - alpha * sqrt(1 - p))
    p = N_CHOSEN_NUMBERS / N_TOTAL_NUMBERS
    middle = np.sqrt(n_draws * p)
    shift = np.sqrt(1 - p)
    return (middle + alpha * shift) / (middle - alpha * shift) - 1


def extremum_diff(draws: list[list[int]]) -> float:
    stats = occurences(draws)
    if np.isclose(min(stats), 0):
        return 0
    return (max(stats) / min(stats)) - 1


def occurences(draws: list[list[int]]) -> list[float]:
    n_occurences = Counter()
    for draw in draws:
        n_occurences += Counter(draw)
    return [n_occurences[i] for i in ALL_NUMBERS]


def sample_draws(n_draws: int) -> list[list[int]]:
    draws = [None] * n_draws
    for i in range(n_draws):
        draws[i] = random.sample(ALL_NUMBERS, N_CHOSEN_NUMBERS)
        # assert that all numbers are unique
        assert len(set(draws[i])) == N_CHOSEN_NUMBERS, f"{draws[i]}"
    return draws


def main():
    # simulate draws
    N_DRAWS = 3000
    draws = sample_draws(N_DRAWS)
    print(extremum_diff(draws))


if __name__ == "__main__":
    main()
