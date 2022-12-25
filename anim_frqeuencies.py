from lotto_sim import sample_draws, N_TOTAL_NUMBERS
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


N_DRAWS = 6000
DRAW_INTERVAL = 50
HEIGHT = 0.05


def frequencies(draws_bool: np.ndarray[int]) -> np.ndarray[float]:
    return np.average(draws_bool, axis=0)


def create_animation(draws: list[list[int]]):
    # calculate frequencies
    steps = np.arange(DRAW_INTERVAL, len(draws) + 1, DRAW_INTERVAL, dtype=int)
    n_frames = len(steps)
    # boolean representation of draws
    drawn_numbers = np.arange(1, N_TOTAL_NUMBERS + 1)
    draws_bool = np.array([[number in draw for number in drawn_numbers] for draw in draws])
    frequencies_in_step = [frequencies(draws_bool[:n_drawn]) for n_drawn in steps]
    # calculate most and least occuring in every step
    most_occuring_in_step = [np.argmax(frequencies_in_step[i]) for i in range(n_frames)]
    least_occuring_in_step = [np.argmin(frequencies_in_step[i]) for i in range(n_frames)]

    # animate
    fig, (ax1, ax2) = plt.subplots(1, 2, width_ratios=[3, 1])

    # axes ylims
    min_frequency = frequencies_in_step[0][least_occuring_in_step[0]]
    max_frequency = frequencies_in_step[0][most_occuring_in_step[0]]
    max_y = max(HEIGHT, max_frequency)
    ax1.set_ylim(0, max_y)
    ax2.set_ylim(0, max_y)

    # initial plot
    x = np.arange(N_TOTAL_NUMBERS)
    ax1.set_title(f"Number of draws: {steps[0]}")
    ax1.set_xlabel("drawn number")
    ax1.set_ylabel("frequency")
    frequency_bars = ax1.bar(x, frequencies_in_step[0])
    ax1.set_xticks([0, N_TOTAL_NUMBERS - 1])
    ax1.set_xticklabels([1, N_TOTAL_NUMBERS])

    ax2.set_title(f"least vs most common")
    comparison_bars = ax2.bar([0, 1], [min_frequency, max_frequency])
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(["least", "most"], rotation='vertical')

    def animate(i):
        ax1.set_title(f"Number of draws: {(i + 1) * DRAW_INTERVAL}")
        # update frequencies
        for drawn_number, bar in enumerate(frequency_bars):
            bar.set_height(frequencies_in_step[i][drawn_number])
        # update comparison
        comparison_bars[0].set_height(frequencies_in_step[i][least_occuring_in_step[i]])
        comparison_bars[1].set_height(frequencies_in_step[i][most_occuring_in_step[i]])

    return animation.FuncAnimation(fig, animate, repeat=True, blit=False, frames=n_frames)


def main():
    # simulate draws
    draws = sample_draws(N_DRAWS)
    # evaluate stats
    anim = create_animation(draws)
    anim.save("animation.gif", fps=60)


if __name__ == "__main__":
    main()
