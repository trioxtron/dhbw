import numpy as np
import matplotlib.pyplot as plt

def simulate_data(slope, n_points):
    # simulate X data and create random noise epsilons 
    epsilon = np.random.normal(0, 2, size=(n_points, 1))
    X = np.linspace(0.0, 10.0, n_points).reshape(-1, 1)

    # create Y data using a linear relationship with noise
    Y = slope * X + epsilon

    return X, Y

def estimate_slope(X, Y):
    # calculate the slope using the least squares formula
    xtx_inv = np.linalg.inv(X.T @ X)
    theta_ml = xtx_inv @ X.T @ Y
    return theta_ml.flatten()[0]

def calculate_squared_error(Y_true, Y_pred):
    return np.mean((Y_true - Y_pred) ** 2)


def run_simulation(slope, n_points, n_simulations):
    squared_errors = []

    for _ in range(n_simulations):
        X, Y = simulate_data(slope, n_points)

        # train-test split
        split_idx = int(len(X) * 0.80)
        X_train, Y_train = X[:split_idx], Y[:split_idx]
        X_test, Y_test = X[split_idx:], Y[split_idx:]

        estimated_slope = estimate_slope(X_train, Y_train)
        Y_pred = estimated_slope * X_test
        error = calculate_squared_error(Y_test, Y_pred)
        squared_errors.append(error)

    plt.hist(squared_errors, bins=30, density=True, alpha=0.6)
    plt.title("Distribution of Squared Errors from Simulations")
    plt.xlabel("Squared Error")
    plt.ylabel("Density")
    plt.grid(axis='y', alpha=0.3)
    plt.show()

def run_single_simulation(slope, n_points):
    X, Y = simulate_data(slope, n_points)
    # train-test split
    split_idx = int(len(X) * 0.8)
    X_train, Y_train = X[:split_idx], Y[:split_idx]
    X_test, Y_test = X[split_idx:], Y[split_idx:]

    estimated_slope = estimate_slope(X_train, Y_train)
    Y_pred = estimated_slope * X_test
    error = calculate_squared_error(Y_test, Y_pred)

    print(f"Estimated slope: {estimated_slope:.4f}")
    print(f"Squared error: {error:.4f}")

    # plot
    plt.scatter(X, Y, alpha=0.6, label="Data Points")
    plt.plot(X_test, Y_pred, color='red', label="Fitted Line")
    plt.title("Single Simulation of Data and Fitted Line")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid()
    plt.show()


def plot_example_data(slope, n_points):
    X, Y = simulate_data(slope, n_points)
    plt.scatter(X, Y, alpha=0.6)
    plt.title("example of simulated data")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.show()


def main():
    slope = 2
    n_points = 100
    n_simulations = 10**4

    #run_single_simulation(slope, n_points)
    #plot_example_data(slope, n_points)
    run_simulation(slope, n_points, n_simulations)




if __name__ == "__main__":
    main()
