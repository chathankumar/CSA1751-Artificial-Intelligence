import numpy as np
from collections import Counter

# Function to calculate entropy
def entropy(y):
    freq = np.bincount(y)
    prob = freq / len(y)
    return -np.sum([p * np.log2(p) for p in prob if p > 0])

# Function to split the dataset
def split(X, y, feature, threshold):
    left = np.where(X[:, feature] <= threshold)[0]
    right = np.where(X[:, feature] > threshold)[0]
    return X[left], X[right], y[left], y[right]

# Function to compute information gain
def info_gain(X, y, feature, threshold):
    y_left, y_right = split(X, y, feature, threshold)[2:]
    if len(y_left) == 0 or len(y_right) == 0:
        return 0
    return entropy(y) - (len(y_left) / len(y)) * entropy(y_left) - (len(y_right) / len(y)) * entropy(y_right)

# Main decision tree algorithm
class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y, depth=0):
        if len(set(y)) == 1 or depth == self.max_depth:
            return Counter(y).most_common(1)[0][0]
        n_features = X.shape[1]
        best_feature, best_thresh, best_gain = None, None, -np.inf
        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                gain = info_gain(X, y, feature, threshold)
                if gain > best_gain:
                    best_gain = gain
                    best_feature, best_thresh = feature, threshold
        left_X, right_X, left_y, right_y = split(X, y, best_feature, best_thresh)
        if len(left_y) == 0 or len(right_y) == 0:
            return Counter(y).most_common(1)[0][0]
        return {
            'feature': best_feature,
            'threshold': best_thresh,
            'left': self.fit(left_X, left_y, depth + 1),
            'right': self.fit(right_X, right_y, depth + 1)
        }

    def predict(self, X, tree=None):
        if tree is None:
            tree = self.tree
        if isinstance(tree, dict):
            if X[tree['feature']] <= tree['threshold']:
                return self.predict(X, tree['left'])
            else:
                return self.predict(X, tree['right'])
        else:
            return tree

    def train(self, X, y):
        self.tree = self.fit(X, y)

# Example usage:
# X = np.array([[2.8, 0.8], [1.2, 1.5], [2.6, 0.9], [1.8, 0.6], [3.5, 2.2]])
# y = np.array([0, 1, 0, 1, 0])
# dt = DecisionTree(max_depth=2)
# dt.train(X, y)
# print(dt.predict([3, 1]))
