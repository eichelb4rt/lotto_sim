from lotto_sim import sample_draws, occurences, ALL_NUMBERS, N_TOTAL_NUMBERS
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

N_DRAWS = 6000


def main():
    draws = sample_draws(N_DRAWS)
    distribution = occurences(draws)
    plt.bar(ALL_NUMBERS, distribution)
    plt.ylim(0, max(distribution))
    plt.title(f"Number of draws: {N_DRAWS}")
    plt.xlabel("drawn number")
    plt.ylabel("occurences")
    plt.xticks([0, N_TOTAL_NUMBERS - 1], labels=[1, N_TOTAL_NUMBERS])
    plt.savefig(f"distributions/{N_DRAWS}_draws.png")


if __name__ == "__main__":
    main()
