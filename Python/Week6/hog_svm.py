import cv2
import numpy as np
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
from joblib import dump, load
from pathlib import Path

clf_save = Path("files/svm.save")
if not clf_save.exists():
    mnist_dataset = datasets.fetch_openml("mnist_784") # 28 * 28 images

    features = np.array(mnist_dataset.data, "uint8")
    labels = np.array(mnist_dataset.target, "int")

    print("read dataset")

    hog_list = []
    for image in features:
        hog_list.append(hog(image.reshape(28, 28)))

    print("create hogs")

    classifier = LinearSVC()
    classifier.fit(hog_list, labels)

    print("train model")

    dump(classifier, "files/svm.save")

else:
    classifier = load("files/svm.save")

image = cv2.imread("files/digit2.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 95, 255, cv2.THRESH_BINARY_INV)
thresh = cv2.dilate(thresh, np.ones((10, 10)))
_, cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    M = cv2.moments(c)
    if M["m00"] < 500:
        continue
    x, y, w, h = cv2.boundingRect(c)
    number = image[y: y + h, x : x + w]
    number = cv2.resize(number, (28, 28))
    number_hog = hog(number)
    res = classifier.predict([number_hog])
    cv2.putText(image, str(res[0]), (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    

cv2.imshow("Number", image)
cv2.waitKey(0)
cv2.destroyAllWindows()