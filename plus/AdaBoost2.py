import numpy as np
import math

class Adaboost:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators
        self.trees = []
        self.alphas = []

    def _stump_classifier(self, X, feature_idx, threshold, polarity):
        feature_values = X[:, feature_idx]
        predictions = np.ones(len(feature_values))
        if polarity == 1:
            predictions[feature_values <= threshold] = -1
        else:
            predictions[feature_values > threshold] = -1
        return predictions

    def _calculate_weighted_error(self, weight, predictions, y):
        error = np.sum(weight[predictions != y])
        return error

    def _update_weights(self, weight, alpha, predictions, y):
        w_updated = weight * np.exp(-alpha * y * predictions)
        w_updated /= np.sum(w_updated)
        return w_updated

    def fit(self, X, y):
        num_samples, num_features = X.shape
        weight = np.ones(num_samples) / num_samples  # Initialize sample weights uniformly
        
        for _ in range(self.n_estimators):
            min_error = math.inf
            best_tree = None
            
            # search best stump
            for feature_idx in range(num_features):
                unique_values = np.unique(X[:, feature_idx])
                for threshold in unique_values:
                    for polarity in [1, -1]:
                        predictions = self._stump_classifier(X, feature_idx, threshold, polarity)
                        error = self._calculate_weighted_error(weight, predictions, y)
                        
                        if error < min_error:
                            min_error = error
                            best_tree = (feature_idx, threshold, polarity)
            
            feature_idx, threshold, polarity = best_tree
            predictions = self._stump_classifier(X, feature_idx, threshold, polarity)
            error = self._calculate_weighted_error(weight, predictions, y)
            
            alpha = 0.5 * np.log((1 - error) / error)
            weight = self._update_weights(weight, alpha, predictions, y)
            
            self.trees.append(best_tree)
            self.alphas.append(alpha)

    def _predict(self, x):
        prediction = 0
        for (feature_idx, threshold, polarity), alpha in zip(self.trees, self.alphas):
            prediction += alpha * self._stump_classifier(np.array([x]), feature_idx, threshold, polarity)[0]
        return np.sign(prediction)

    def predict(self, X):
        predictions = np.array([self._predict(x) for x in X])
        return predictions

# Given input data
X_train = np.array([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
y_train = np.array([1, 1, 1, -1, -1, -1, 1, 1, 1, -1])

adaboost_clf = Adaboost(n_estimators=10)
adaboost_clf.fit(X_train, y_train)

predictions_train = adaboost_clf.predict(X_train)

print("Predictions on training data:")
print(predictions_train)
