import glob as gb
from sklearn.neighbors import KNeighborsClassifier
from skimage import feature
import cv2
import numpy as np
import random

def read_dataset(drawType = "spiral",is_test = False):
    folderName = "testing" if is_test else "training"
    files_healthy = gb.glob("files/dataset/%s/%s/healthy/*" % ("*", folderName))
    files_parkinson = gb.glob("files/dataset/%s/%s/parkinson/*" % ("*", folderName))

    trainX, trainY = [], []
    size = (250, 250)
    for address in files_healthy:
        img = cv2.imread(address)
        img = cv2.resize(img, size)
        hog = feature.hog(img)
        trainX.append(hog)
        trainY.append(0)
    
    for address in files_parkinson:
        img = cv2.imread(address)
        img = cv2.resize(img, size)
        hog = feature.hog(img)
        trainX.append(hog)
        trainY.append(1)
    return (np.array(trainX), np.array(trainY))

trainX, trainY = read_dataset("wave", False)
print(trainX.shape, trainY.shape)

classifier = KNeighborsClassifier(5)
classifier.fit(trainX, trainY)

tests = gb.glob("files/dataset/*/testing/*/*")
random.shuffle(tests)
for address in tests: 
    img = cv2.imread(address)
    img = cv2.resize(img, (250, 250))
    hog = feature.hog(img)
    pred = classifier.predict([hog])
    res = "Healthy" if pred[0] == 0 else "Parkinson"
    color = (0, 255, 0) if pred[0] == 0 else (0, 0, 255)
    cv2.putText(img, res ,(10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 3)
    cv2.imshow("result", img)
    cv2.waitKey(2000)
