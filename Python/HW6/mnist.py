import cv2
import numpy as np
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
from joblib import dump, load
from pathlib import Path

clf_save = Path("files/svm.save")
if not clf_save.exists():
    mnist_dataset = datasets.fetch_openml("mnist_784")  # 28 * 28 images

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

image = cv2.imread("files/digit1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



cv2.imshow("Number", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
