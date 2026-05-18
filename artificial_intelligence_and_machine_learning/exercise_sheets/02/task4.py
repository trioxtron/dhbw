import numpy as np
import matplotlib.pyplot as plt

def simulate_data(slope, n_points, use_epsilon=True):
    # simulate X data and create random noise epsilons 
    X = np.random.uniform(0.0, 10.0, size=(n_points, 1))

    if use_epsilon:
        # create noise
        epsilon = np.random.normal(0, 2, size=(n_points, 1))
        # create Y data using a linear relationship with noise
        Y = slope * X + epsilon
    else:
        # create Y data using a linear relationship without noise
        Y = slope * X

    return X, Y

def estimate_slope(X, Y):
    # calculate the slope using the least squares formula
    xtx_inv = np.linalg.inv(X.T @ X)
    theta_ml = xtx_inv @ X.T @ Y
    return theta_ml.flatten()[0]

def predict(X, slope):
    return slope * X

def run_single_simulation(slope, n_points, use_epsilon=True):
    X, Y = simulate_data(slope, n_points, use_epsilon=use_epsilon)
    estimated_slope = estimate_slope(X, Y)

    x_star = 2
    y_star = slope * x_star
    y_pred_star = predict(x_star, estimated_slope)

    error = abs(y_star - y_pred_star)

    return error


def main():
    slope = 2
    n_points = [1, 2, 5, 10, 20, 50, 100, 500, 1000, 10000, 100000]

    epsilon_erorrs = []
    no_epsilon_erorrs = []
    for n in n_points:
        epsilon_error = run_single_simulation(slope, n)
        no_epsilon_error = run_single_simulation(slope, n, use_epsilon=False)

        epsilon_erorrs.append(epsilon_error)
        no_epsilon_erorrs.append(no_epsilon_error)

    plt.plot(n_points, epsilon_erorrs, marker='o', label='With Epsilon')
    plt.plot(n_points, no_epsilon_erorrs, marker='x', label='Without Epsilon')
    plt.legend()
    plt.xscale('log')
    plt.xlabel('Number of Data Points (log scale)')
    plt.ylabel('Absolute Error at x=2 (log scale)')
    plt.title('Error of Slope Estimation at x=2 vs Number of Data Points')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
