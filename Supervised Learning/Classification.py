from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# load a simple classification dataset
data = load_iris()
X = data.data
y = data.target

# train a logistic regression classifier
clf = LogisticRegression(max_iter=200)
clf.fit(X, y)

# predict on the first 5 samples
print(clf.predict(X[:5]))