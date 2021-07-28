import numpy as np
import sys
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Lasso

n = 10

X = np.zeros((2*n, 5))
y_train = np.zeros((n, 1))


st = sys.stdin.readlines()


for i in range(n):
    X[i] = st[i].split()[:5]
    y_train[i] = st[i].split()[5:]


for i in range(n, 2*n):
    X[i] = st[i].split()[:5]

X_train = X[:n]
X_test = X[n:]

poly = PolynomialFeatures(2)
X_train = poly.fit_transform(X_train)
X_test = poly.transform(X_test)

reg = Lasso().fit(X_train, y_train)
predicts = reg.predict(X_test)
print(predicts)
for i in predicts.tolist():
    print(i)

print('cool_reg')