[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5BCxs_Tc)
# Laboratory 2.7: Linear Discriminant Analysis

## Description

In this laboratory practice, you will implement and evaluate a Linear Discriminant Analysis (LDA) model. You will work on the following tasks:

0. **Setup**:
   - Clone the repository and install the required packages.
   - Verify you can access the iris dataset.

1. **LinearDiscriminant Class Implementation**:
   - Implement the `LinearDiscriminant` class with the following methods:
     - `__init__`: Initialize the LDA model with configurable number of components.
     - `fit`: Fit the model using training data, calculating class means, scatter matrices, and extracting linear discriminants.
     - `transform`: Project data onto the top linear discriminants.
     - `fit_transform`: Convenience method to fit and transform in one step.
     - `predict`: Predict class labels by determining which class mean each sample is closest to in the transformed space.

2. **Model Analysis Components**:
   - Calculate class mean vectors for each class in the dataset.
   - Compute within-class and between-class scatter matrices.
   - Solve the eigenvalue problem for optimal class separation.
   - Extract top linear discriminants based on eigenvalues.
   - Store class means in the transformed space for classification.
   - Calculate class prior probabilities.

3. **Model Evaluation**:
   - Verify model works correctly on binary classification problems.
   - Test model performance on the iris dataset.
   - Evaluate prediction accuracy using appropriate metrics.
   - Analyze how the model separates different classes.

## Uploading Changes to GitHub

To upload your changes to GitHub and have them automatically evaluated using the provided tests, follow these steps:

1. **Stage Your Changes**:
   ```sh
   git add .
   ```

2. **Commit Your Changes**:
   ```sh
   git commit -m "Implement Linear Discriminant Analysis"
   ```
3. **Push Your Changes**:
   ```sh
   git push
   ``` 

Once you push your changes, the tests will be automatically executed. If all tests pass, you will receive 10 points. You can try as many times as you want until all tests pass.

Good luck!
