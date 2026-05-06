from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

# load a simple dataset
data = load_diabetes()
X = data.data
y = data.target

# train a linear regression model
model = LinearRegression()
model.fit(X, y)

# predict on the first 5 samples
print(model.predict(X[:5]))