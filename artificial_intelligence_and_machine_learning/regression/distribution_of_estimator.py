import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def sim(n_sim):
    X = np.linspace(0.0, 10.0, 101).reshape(-1, 1)
    sigma_sq = 4

    print(f"X range: {X[0]} to {X[-1]} (Total elements: {len(X)})")

    epsilon = np.random.normal(0, np.sqrt(sigma_sq), size=(len(X), n_sim))
    Y = 2 * X + epsilon


    xtx_inv = np.linalg.inv(X.T @ X)
    theta_ml = xtx_inv @ X.T @ Y

    return theta_ml.flatten(), X, sigma_sq


def main():
    n_sim = 10**8

    thetas, X, sigma_sq = sim(n_sim)

    theoretical_mean = 2
    theoretical_var = sigma_sq * (1 / (X.T @ X)[0, 0])
    theoretical_std = np.sqrt(theoretical_var)

    plt.figure(figsize=(10, 6))
    plt.hist(thetas, bins=100, density=True, alpha=0.6, color='skyblue', label='Simulated $\theta^{ML}$')

    x_axis = np.linspace(min(thetas), max(thetas), 100)
    plt.plot(x_axis, norm.pdf(x_axis, theoretical_mean, theoretical_std), 
             'r-', lw=2, label=f'Theoretical N({theoretical_mean:.2f}, {theoretical_var:.4f})')

    plt.title(r"Comparison of Empirical vs. Theoretical Distribution of $\theta^{ML}$")
    plt.xlabel(r"$\theta$ value")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.show()




if __name__ == "__main__":
    main()
