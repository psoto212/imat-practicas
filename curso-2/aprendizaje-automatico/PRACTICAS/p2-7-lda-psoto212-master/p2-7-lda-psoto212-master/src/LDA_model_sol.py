import numpy as np

class LinearDiscriminant:
    """
    Linear Discriminant Analysis (LDA) class.

    This class implements the LDA algorithm for dimensionality reduction and 
    finding the linear combination of features that best separates two or more 
    classes of objects or events.

    Attributes:
        weights (np.ndarray): The linear discriminants (eigenvectors) that can
            be used to transform the data into a lower-dimensional space.
    """

    def __init__(self, n_components=None):
        """
        Initializes the LinearDiscriminant instance with the number of components.
        
        Args:
            n_components (int, optional): Number of linear discriminants to retain. If None,
                                        all components are kept.
        """
        self.n_components = n_components
        self.weights = None
        self.class_means = None
        self.priors = None
        self.class_labels = None

    def fit(self, X, y):
        """
        Fit the LDA model according to the given training data.

        Args:
            X (np.ndarray): Training data, shape (n_samples, n_features), 
                where n_samples is the number of samples and n_features is 
                the number of features.
            y (np.ndarray): Target values, shape (n_samples,), where n_samples
                is the number of samples.

        Returns:
            None
        """
        n_features = X.shape[1]
        self.class_labels = np.unique(y)
        n_classes = len(self.class_labels)

        # Check if n_components is not set, use min(n_features, n_classes - 1)
        if self.n_components is None:
            self.n_components = min(n_features, n_classes - 1)

        # Calculate the mean vectors for each class
        self.mean_vectors = np.array([X[y == label].mean(axis=0) for label in self.class_labels])

        # Compute the overall mean of the data
        overall_mean = np.mean(X, axis=0)

        # Compute S_W and S_B
        S_W = np.zeros((n_features, n_features))
        S_B = np.zeros((n_features, n_features))
        for i, mean_vec in enumerate(self.mean_vectors):
            X_class = X[y == self.class_labels[i]]
            class_scatter = (X_class - mean_vec).T @ (X_class - mean_vec)
            S_W += class_scatter

            n_class_samples = X_class.shape[0]
            mean_diff = (mean_vec - overall_mean).reshape(n_features, 1)
            S_B += n_class_samples * (mean_diff @ mean_diff.T)

        # Solve the eigenvalue problem
        eigen_values, eigen_vectors = np.linalg.eig(np.linalg.pinv(S_W) @ S_B)

        # Sort eigenvectors by eigenvalues in descending order
        eigen_pairs = sorted(
            [(np.abs(eigen_values[i]), eigen_vectors[:, i]) for i in range(len(eigen_values))],
            key=lambda x: x[0],
            reverse=True
        )

        # Extract the linear discriminants (eigenvectors) based on n_components
        self.weights = np.array([eigen_pairs[i][1] for i in range(self.n_components)]).T.real

        # Store class means in the transformed space for classification
        self.class_means = np.array([mean_vec @ self.weights for mean_vec in self.mean_vectors])

        # Calculate priors
        self.priors = np.array([np.mean(y == label) for label in self.class_labels])

    def transform(self, X):
        """
        Project the data onto the top linear discriminants.
        
        Args:
            X (np.ndarray): Data to transform, shape (n_samples, n_features).
        
        Returns:
            X_transformed (np.ndarray): Data projected onto the selected linear discriminants,
                                        shape (n_samples, n_components).
        """
        X_transformed = X @ self.weights
        return X_transformed

    def fit_transform(self, X, y):
        """
        Fit to data, then transform it.

        Args:
            X (np.ndarray): Training data, shape (n_samples, n_features).
            y (np.ndarray): Target values, shape (n_samples,).

        Returns:
            X_lda (np.ndarray): Transformed data, shape (n_samples, n_components),
                where n_components <= n_classes - 1.
        """
        self.fit(X, y)
        return self.transform(X)

    def predict(self, X):
        """
        Predict class labels for samples in X.

        This method applies the learned linear discriminant analysis model to
        predict the class labels of the given samples. The prediction is based
        on which class mean (in the transformed space) the sample is closest to.

        Args:
            X (np.ndarray): Input data, shape (n_samples, n_features), where
                n_samples is the number of samples and n_features is the number
                of features.

        Returns:
            np.ndarray: Predicted class labels, shape (n_samples,), where each
                entry is the predicted class label for the corresponding sample
                in X.
        """
        # TODO: Project data onto the lower-dimensional space
        X_transformed = self.transform(X)

        # TODO: Calculate the distances from each point in X to each class mean
        distances = np.array([
            np.linalg.norm(X_transformed - class_mean, axis=1)
            for class_mean in self.class_means
        ]).T

        # TODO: Find the class with the minimum distance for each point
        predictions = self.class_labels[np.argmin(distances, axis=1)]

        return predictions