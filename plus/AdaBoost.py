import numpy as np
from collections import Counter
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value  # Value if the node is a leaf in the tree

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        
    def fit(self, X, y, sample_weight=None):
        self.n_classes_ = len(set(y))
        self.n_features_ = X.shape[1]
        self.tree_ = self._grow_tree(X, y, sample_weight)
        
    def _predict(self, inputs):
        node = self.tree_
        while node.value is None:
            if inputs[node.feature] < node.threshold:
                node = node.left
            else:
                node = node.right
        print("node feature : ", node.feature)
        print("node value : ", node.value)
        return node.value
        
    def predict(self, X):
        return [self._predict(inputs) for inputs in X]
   
    def _most_common_label(self, y, sample_weight):
        counter = Counter(y)
        most_common = counter.most_common(1)[0][0]
        return most_common
    
    def _grow_tree(self, X, y, sample_weight, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(set(y))
        
        # Stopping criteria
        if (depth >= self.max_depth
            or n_labels == 1
            or n_samples < 2):
            leaf_value = self._most_common_label(y, sample_weight)
            return Node(value=leaf_value)
        
        # Find best split
        best_feature, best_threshold = self._best_split(X, y, sample_weight)
        
        # Grow left and right child
        left_indices, right_indices = self._split(X[:, best_feature], best_threshold)
        left = self._grow_tree(X[left_indices, :], y[left_indices], sample_weight[left_indices], depth + 1)
        right = self._grow_tree(X[right_indices, :], y[right_indices], sample_weight[right_indices], depth + 1)
        return Node(best_feature, best_threshold, left, right)
    
    def _information_gain(self, y, sample_weight, feature_values, threshold):
        parent_entropy = self._entropy(y, sample_weight)
        
        # Generate split
        left_indices, right_indices = self._split(feature_values, threshold)
        if len(left_indices) == 0 or len(right_indices) == 0:
            return 0
        
        # Calculate information gain
        n = len(y)
        n_l, n_r = len(left_indices), len(right_indices)
        e_l, e_r = self._entropy(y[left_indices], sample_weight[left_indices]), self._entropy(y[right_indices], sample_weight[right_indices])
        child_entropy = (n_l / n) * e_l + (n_r / n) * e_r
        ig = parent_entropy - child_entropy
        return ig
    
    def _entropy(self, y, sample_weight):
        hist = np.bincount(y, weights=sample_weight)
        ps = hist / np.sum(hist)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])
    
    def _best_split(self, X, y, sample_weight):
        best_gain = -1
        split_index, split_threshold = None, None
        
        for feature_index in range(self.n_features_):
            feature_values = X[:, feature_index]
            unique_values = set(feature_values)
            
            for threshold in unique_values:
                gain = self._information_gain(y, sample_weight, feature_values, threshold)
                
                if gain > best_gain:
                    best_gain = gain
                    split_index = feature_index
                    split_threshold = threshold
        
        return split_index, split_threshold
    
    def _split(self, feature_values, threshold):
        left_indices = np.argwhere(feature_values <= threshold).flatten()
        right_indices = np.argwhere(feature_values > threshold).flatten()
        return left_indices, right_indices

class AdaBoost:
    def __init__(self, n_estimators=50):
        self.n_estimators = n_estimators
        self.models = []
        self.alphas = []
        self.weight_list = []

    def fit(self, X, y):
        n_samples = X.shape[0]
        weights = np.ones(n_samples) / n_samples
        
        print('initial weights :', weights)
        self.weight_list.append(weights)

        for _ in range(self.n_estimators):
            model = DecisionTree(max_depth=1)  # Weak learner (decision stump)
            model.fit(X, y, sample_weight=weights)

            predictions = model.predict(X)
            epsilon = np.sum(weights * (predictions != y)) / np.sum(weights)
            print('epsilon :', epsilon)

            alpha = 0.5 * np.log((1 - epsilon) / epsilon)

            # Update instance weights
            weights = (weights * np.exp(-alpha * y * predictions)) / np.sum(weights)
            
            self.weight_list.append(weights) 
            self.models.append(model)
            self.alphas.append(alpha)

    def predict(self, X):
        predictions = np.zeros(X.shape[0])
        for alpha, model in zip(self.alphas, self.models):
            print('alpha :', alpha)
            predictions += alpha * np.array(model.predict(X)).astype('float64')
            print('res prediction :', predictions)

        return np.sign(predictions)

X_train = np.array([[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
y_train = np.array([1,1,1,2,2,2,1,1,1,2])

# Create and train AdaBoost classifier
adaboost_clf = AdaBoost(n_estimators=3)
adaboost_clf.fit(X_train, y_train)

print("wl : ", adaboost_clf.weight_list)
# Make predictions
predictions = adaboost_clf.predict(X_train)
print('last', predictions)