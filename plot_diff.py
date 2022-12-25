from lotto_sim import sample_draws, extremum_diff, theoretical_diff
import matplotlib.ticker
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


MIN_DRAWS = 500
N_DRAWS = 6000
DRAW_INTERVAL = 50

N_RUNS = 20


def main():
    # simulate draws
    steps = list(range(MIN_DRAWS, N_DRAWS + 1, DRAW_INTERVAL))
    runs = []
    for _ in range(N_RUNS):
        draws = sample_draws(N_DRAWS)
        diffs = [extremum_diff(draws[:size]) for size in steps]
        runs.append(diffs)

    y_measured = np.average(runs, axis=0)
    y_theoretical = [theoretical_diff(size) for size in steps]

    fig, ax = plt.subplots()
    ax.plot(steps, y_measured, label="measured")
    ax.plot(steps, y_theoretical, label=f"theoretical")
    plt.legend()
    plt.xlabel("Number of draws")
    plt.ylabel("Extremum Difference")
    plt.savefig("extremum_diff.png")


if __name__ == "__main__":
    main()
