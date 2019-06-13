from sklearn.neighbors import KNeighborsClassifier
import numpy as np

feature = np.array([
    [1, 3],
    [0, 1],
    [1, 1.5],
    [1, 5],
    [0, 2],
    [0, 3.5]
])

label = np.array([1, 0, 1, 1, 0, 0])
labels = ["yes" if x == 1 else "no" for x in label]

model = KNeighborsClassifier(3)
model.fit(feature, labels)

pred = model.predict(np.array([[1, 2.5]]))
print(pred)
