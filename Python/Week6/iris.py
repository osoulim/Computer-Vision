import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# data = pd.read_csv("files/iris.data")
data = load_iris("files/iris.data")
features = data[0]
labels = data[1]

X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size = 0.33)

classifier = KNeighborsClassifier(3)
classifier.fit(X_train, Y_train)

print("accuracy: %f" % classifier.score(X_test, Y_test))

