import numpy as np
from lotto_sim import theoretical_diff, N_CHOSEN_NUMBERS, N_TOTAL_NUMBERS, ALPHA

MIN_STEP_SIZE = 1
MIN_DRAWS = 50


def find_min_draws(target_diff: float) -> int:
    step_size = MIN_STEP_SIZE
    # increase step size until theoretical difference is smaller than diff
    while theoretical_diff(step_size) > target_diff or step_size < MIN_DRAWS:
        step_size *= 2
    # start binary search for minimum n_draws so that theoretical_diff(n_draws) < diff
    n_draws = step_size
    step_size //= 2
    while step_size >= MIN_STEP_SIZE:
        current_diff = theoretical_diff(n_draws)
        # if we happen to exactly hit it, return n_draws
        if current_diff == target_diff:
            return n_draws
        # if we're not there yet, increase n_draws
        if current_diff > target_diff:
            n_draws += step_size
        # if we overshot it, decrease n_draws
        else:
            n_draws -= step_size
        # home in -> decrease step_size
        step_size //= 2
    return n_draws


def calc_min_draws(target_diff: float, alpha: float = ALPHA) -> float:
    p = N_CHOSEN_NUMBERS / N_TOTAL_NUMBERS
    return (alpha * (target_diff + 2) / target_diff)**2 * (1 - p) / p


def main():
    # 24,06% diff
    target_diff = 0.2406
    minimum_better_found = find_min_draws(target_diff)
    minimum_better_calced = calc_min_draws(target_diff)
    print(f"Minimum number of draws achieving {100 * target_diff:.2f}% (calculated):\t{minimum_better_calced:.2f}")
    print(f"Minimum number of draws achieving {100 * target_diff:.2f}% (found):\t{minimum_better_found}")
    print(f"Achieved Difference:\t{theoretical_diff(minimum_better_found)}")
    print(f"Difference for 1 less:\t{theoretical_diff(minimum_better_found - 1)}")
    print(f"Difference for 1 more:\t{theoretical_diff(minimum_better_found + 1)}")


if __name__ == "__main__":
    main()
