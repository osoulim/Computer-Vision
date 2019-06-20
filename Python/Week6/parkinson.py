import glob as gb
from sklearn.neighbors import KNeighborsClassifier
from skimage import feature
import cv2
import numpy as np

def read_dataset(drawType = "spiral",is_test = False):
    folderName = "testing" if is_test else "training"
    files_healthy = gb.glob("files/dataset/%s/%s/healthy/*" % (drawType, folderName))
    files_parkinson = gb.glob("files/dataset/%s/%s/parkinson/*" % (drawType, folderName))

    trainX, trainY = [], []

    for address in files_healthy:
        img = cv2.imread(address)
        img = cv2.resize(img, (250, 250))
        hog = feature.hog(img)
        trainX.append(hog)
        trainY.append(0)
    
    for address in files_parkinson:
        img = cv2.imread(address)
        img = cv2.resize(img, (250, 250))
        hog = feature.hog(img)
        trainX.append(hog)
        trainY.append(1)
    return (np.array(trainX), np.array(trainY))

trainX, trainY = read_dataset("wave", False)
testX, testY = read_dataset("wave", True)
print(trainX.shape, trainY.shape)

classifier = KNeighborsClassifier(5)
classifier.fit(trainX, trainY)


print("accuracy is: %f" % classifier.score(testX, testY))
