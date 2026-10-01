import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


class LinearRegressor:
    """
    Extended Linear Regression model with support for categorical variables
    and gradient descent fitting.
    """

    def __init__(self):
        self.coefficients = None
        self.intercept = None

    def fit(self, X, y, method="least_squares", learning_rate=0.01, iterations=1000):
        """
        Fit the model using either normal equation or gradient descent.

        Args:
            X (np.ndarray): Independent variable data (2D array).
            y (np.ndarray): Dependent variable data (1D array).
            method (str): "least_squares" or "gradient_descent".
            learning_rate (float): Learning rate for gradient descent.
            iterations (int): Number of iterations for gradient descent.
        """
        if method not in ["least_squares", "gradient_descent"]:
            raise ValueError(
                f"Method {method} not available for training linear regression."
            )

        if np.ndim(X) == 1:
            X = X.reshape(-1, 1)

        X_with_bias = np.insert(X, 0, 1, axis=1)

        if method == "least_squares":
            self.fit_multiple(X_with_bias, y)
        elif method == "gradient_descent":
            self.fit_gradient_descent(X_with_bias, y, learning_rate, iterations)

    def fit_multiple(self, X, y):
        """
        Fit the model using multiple linear regression.

        Args:
            X (np.ndarray): Independent variable data (2D array), with bias.
            y (np.ndarray): Dependent variable data (1D array).
        """
        y_b = y.reshape(-1, 1)
        w = np.linalg.pinv(X.T @ X) @ X.T @ y_b

        self.intercept = w[0, 0]
        self.coefficients = w[1:, 0]

    def fit_gradient_descent(self, X, y, learning_rate=0.01, iterations=1000):
        """
        Fit the model using gradient descent.

        Args:
            X (np.ndarray): Independent variable data (2D array), with bias.
            y (np.ndarray): Dependent variable data (1D array).
            learning_rate (float): Learning rate for gradient descent.
            iterations (int): Number of iterations for gradient descent.
        """
        m = len(y)

        # Initialize parameters close to 0
        self.coefficients = np.random.rand(X.shape[1] - 1) * 0.01
        self.intercept = np.random.rand() * 0.01

        for epoch in range(iterations):
            predictions = self.predict(X[:, 1:])
            error = predictions - y

            gradient = (2 / m) * (X.T @ error)

            self.intercept -= learning_rate * gradient[0]
            self.coefficients -= learning_rate * gradient[1:]

            if epoch % 1000 == 0:
                mse = np.mean(error ** 2)
                print(f"Epoch {epoch}: MSE = {mse}")

    def predict(self, X):
        """
        Predict the dependent variable values using the fitted model.

        Args:
            X (np.ndarray): Independent variable data (1D or 2D array).

        Returns:
            np.ndarray: Predicted values.
        """
        if self.coefficients is None or self.intercept is None:
            raise ValueError("Model is not yet fitted")

        if np.ndim(X) == 1:
            predictions = self.coefficients * X + self.intercept
        else:
            predictions = X @ self.coefficients + self.intercept

        return predictions


def evaluate_regression(y_true, y_pred):
    """
    Evaluates the performance of a regression model by calculating R^2, RMSE, and MAE.

    Args:
        y_true (np.ndarray): True values.
        y_pred (np.ndarray): Predicted values.

    Returns:
        dict: Dictionary containing R2, RMSE, and MAE.
    """
    rss = np.sum((y_true - y_pred) ** 2)
    tss = np.sum((y_true - np.mean(y_true)) ** 2)
    r_squared = 1 - rss / tss

    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    mae = np.mean(np.abs(y_true - y_pred))

    return {"R2": r_squared, "RMSE": rmse, "MAE": mae}


def one_hot_encode(X, categorical_indices, drop_first=False):
    """
    One-hot encode the categorical columns specified in categorical_indices.

    Args:
        X (np.ndarray): 2D data array.
        categorical_indices (list of int): Indices of categorical columns.
        drop_first (bool): Whether to drop the first dummy column.

    Returns:
        np.ndarray: Transformed array with one-hot encoded columns.
    """
    X = np.array(X, dtype=object)
    transformed_columns = []

    for col_idx in range(X.shape[1]):
        if col_idx in categorical_indices:
            categorical_column = X[:, col_idx]
            unique_values = np.unique(categorical_column)
            one_hot = (categorical_column[:, None] == unique_values).astype(int)

            if drop_first:
                one_hot = one_hot[:, 1:]

            transformed_columns.append(one_hot)
        else:
            transformed_columns.append(X[:, col_idx].reshape(-1, 1))

    X_transformed = np.hstack(transformed_columns)
    return X_transformed.astype(float)