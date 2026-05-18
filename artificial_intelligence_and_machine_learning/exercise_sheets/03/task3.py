import numpy as np
import matplotlib.pyplot as plt

def simulate_data(n_points, use_epsilon=True, dimensions = 20):
    # simulate X data and create random noise epsilons
    X = np.random.normal(0.0, 10.0, size=(n_points, dimensions))
    weights = np.random.normal(0, 2, size=(dimensions, 1))

    if use_epsilon:
        # create noise
        epsilon = np.random.normal(0, 2, size=(n_points, 1))
        # create Y data using a linear relationship with noise
        Y = X @ weights + epsilon
    else:
        # create Y data using a linear relationship without noise
        Y = X @ weights

    return X, Y, weights

def estimate_weights(X, Y):
    # calculate the slope using the least squares formula
    xtx_inv = np.linalg.inv(X.T @ X)
    theta_ml = xtx_inv @ X.T @ Y
    return theta_ml.flatten()

def estimate_weights_regularized(X, Y, lambda_):
    # calculate the slope using the regularized least squares formula
    n_features = X.shape[1]
    xtx_inv = np.linalg.inv(X.T @ X + lambda_ * np.eye(n_features))
    theta_ridge = xtx_inv @ X.T @ Y
    return theta_ridge.flatten()

def get_optimal_lambda(X, Y, lambda_values):
    # train-test split
    split_idx = int(len(X) * 0.8)
    X_train, Y_train = X[:split_idx], Y[:split_idx]
    X_test, Y_test = X[split_idx:], Y[split_idx:]

    best_lambda = None
    best_error = float('inf')
    errors = []

    for lambda_ in lambda_values:
        # train model with current trainingsdata
        weights = estimate_weights_regularized(X_train, Y_train, lambda_)

        predictions = X_test @ weights.reshape(-1, 1)
        error = np.mean((predictions - Y_test) ** 2)
        errors.append(error)

        # find best lambda based on test error
        if error < best_error:
            best_error = error
            best_lambda = lambda_

    # visualize the error for different lambda values
    plt.figure(figsize=(10, 6))
    plt.plot(lambda_values, errors, label='test MSE', color='blue')
    plt.axvline(best_lambda, color='red', linestyle='--', label=f'best lambda: {best_lambda:.2f}')
    plt.title('MSE vs Lambda (Train vs. Test)')
    plt.xlabel('Lambda')
    plt.ylabel('Mean Squared Error')
    plt.legend()
    plt.grid()
    plt.show()

    return best_lambda

def main():
    n_points = 1000
    d = 20
    np.random.seed(42)

    X, Y, w_true = simulate_data(n_points, use_epsilon=True, dimensions=d)

    lambdas = np.logspace(-3, 3, 100)
    lambda_ = get_optimal_lambda(X, Y, list(lambdas))

    # Wertebereich für alpha (die x-Achse unserer Plots)
    alphas = np.linspace(-500, 500, 50)

    # Arrays zum Speichern der geschätzten Gewichte für jedes alpha
    # Form: (Anzahl der Alphas, Dimensionen)
    weights_standard = np.zeros((len(alphas), d))
    weights_regularized = np.zeros((len(alphas), d))

    # 2. Schleife über alle alpha-Werte
    for i, alpha in enumerate(alphas):
        # Kopien erstellen, damit wir die Originaldaten nicht dauerhaft überschreiben
        Y_mod = Y.copy()

        # Handschriftliche Notiz: Setze den letzten Y-Wert auf alpha
        Y_mod[-1] = alpha

        # Regression durchführen
        weights_standard[i, :] = estimate_weights(X, Y_mod)
        weights_regularized[i, :] = estimate_weights_regularized(X, Y_mod, lambda_)

    # 3. Erstelle d (20) Plots
    # Wir machen ein 4x5 Raster für die 20 Dimensionen
    #fig, axes = plt.subplots(4, 5, figsize=(18, 12), sharex=True)
    fig, axes = plt.subplots(4, 5, figsize=(14, 8), sharex=True)
    axes = axes.flatten()

    for j in range(d):
        axes[j].plot(alphas, weights_standard[:, j], label="Standard", color="red")
        axes[j].plot(alphas, weights_regularized[:, j], label="Regularized", color="blue")

        # plot the true weight as a horizontal dashed line for reference
        axes[j].axhline(w_true[j][0], color='gray', linestyle='--', label="True Weight")

        # plot mean of the estimated weights as vertical line for reference
        mean_standard = np.mean(weights_standard[:, j])
        mean_regularized = np.mean(weights_regularized[:, j])
        axes[j].axhline(mean_standard, color='red', linestyle=':', label="Mean Standard")
        axes[j].axhline(mean_regularized, color='blue', linestyle=':', label="Mean Regularized")

        axes[j].set_title(f"Component {j+1}")
        if j >= 15: # X-Achsen-Label nur in der untersten Reihe
            axes[j].set_xlabel(r"$\alpha$")
        if j % 5 == 0: # Y-Achsen-Label nur ganz links
            axes[j].set_ylabel("Estimator Value")

        if j == 0:
            axes[j].legend()

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()
