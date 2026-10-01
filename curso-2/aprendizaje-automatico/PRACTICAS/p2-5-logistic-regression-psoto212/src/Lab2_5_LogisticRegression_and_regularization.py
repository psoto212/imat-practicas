import numpy as np


class LogisticRegressor:
    def __init__(self):
        """
        Initializes the Logistic Regressor model.

        Attributes:
        - weights (np.ndarray): A placeholder for the weights of the model.
                                These will be initialized in the training phase.
        - bias (float): A placeholder for the bias of the model.
                        This will also be initialized in the training phase.
        """
        self.weights = None
        self.bias = None

    def fit(
        self,
        X,
        y,
        learning_rate=0.01,
        num_iterations=1000,
        penalty=None,
        l1_ratio=0.5,
        C=1.0,
        verbose=False,
        print_every=100,
    ):
        """
        Fits the logistic regression model to the data using gradient descent.
        """
        # Ensure numpy arrays
        X = np.array(X)
        y = np.array(y).reshape(-1)

        # Obtain m (number of examples) and n (number of features)
        m, n = X.shape

        # Initialize all parameters to 0
        self.weights = np.zeros(n)
        self.bias = 0.0

        # Execute the iterative gradient descent
        for i in range(num_iterations):
            # Forward propagation
            y_hat = self.predict_proba(X)

            # Compute loss
            loss = self.log_likelihood(y, y_hat)

            # Logging
            if i % print_every == 0 and verbose:
                print(f"Iteration {i}: Loss {loss}")

            # Gradient of the negative log-likelihood
            error = y_hat - y
            dw = (1 / m) * np.dot(X.T, error)
            db = (1 / m) * np.sum(error)

            # Regularization
            if penalty == "lasso":
                dw = self.lasso_regularization(dw, m, C)
            elif penalty == "ridge":
                dw = self.ridge_regularization(dw, m, C)
            elif penalty == "elasticnet":
                dw = self.elasticnet_regularization(dw, m, C, l1_ratio)

            # Update parameters
            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db

    def predict_proba(self, X):
        """
        Predicts probability estimates for all classes for each sample X.
        """
        X = np.array(X)

        # Logits
        z = np.dot(X, self.weights) + self.bias

        # Sigmoid transformation
        return self.sigmoid(z)

    def predict(self, X, threshold=0.5):
        """
        Predicts class labels for samples in X.
        """
        probabilities = self.predict_proba(X)
        classification_result = (probabilities >= threshold).astype(int)
        return classification_result

    def lasso_regularization(self, dw, m, C):
        """
        Applies L1 regularization (Lasso) to the gradient.
        """
        lasso_gradient = (C / m) * np.sign(self.weights)
        return dw + lasso_gradient

    def ridge_regularization(self, dw, m, C):
        """
        Applies L2 regularization (Ridge) to the gradient.
        """
        ridge_gradient = (C / m) * self.weights
        return dw + ridge_gradient

    def elasticnet_regularization(self, dw, m, C, l1_ratio):
        """
        Applies Elastic Net regularization to the gradient.
        """
        lasso_gradient = (C / m) * np.sign(self.weights)
        ridge_gradient = (C / m) * self.weights
        elasticnet_gradient = l1_ratio * lasso_gradient + (1 - l1_ratio) * ridge_gradient
        return dw + elasticnet_gradient

    @staticmethod
    def log_likelihood(y, y_hat):
        """
        Computes the Log-Likelihood loss for logistic regression.
        """
        y = np.array(y).reshape(-1)
        y_hat = np.array(y_hat).reshape(-1)

        m = y.shape[0]

        # Avoid log(0)
        epsilon = 1e-15
        y_hat = np.clip(y_hat, epsilon, 1 - epsilon)

        loss = -(1 / m) * np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
        return loss

    @staticmethod
    def sigmoid(z):
        """
        Computes the sigmoid of z.
        """
        sigmoid_value = 1 / (1 + np.exp(-z))
        return sigmoid_value