import numpy as np 
import cv2
import glob as gb
from skimage.feature import hog
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier


img_shape = (32, 32)
img_size = 32 * 32
categories = ("airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck")

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def extract_cifar_batch(file):
    dic = unpickle(file)
    data, labels = dic[b'data'], dic[b'labels']
    images = []
    for img_data in data:
        temp = np.zeros((1024, 3), 'uint8')
        R, G, B = img_data[0: img_size], img_data[img_size: 2*img_size], img_data[2*img_size: ]
        temp[..., 0], temp[..., 1], temp[..., 2] = B, G, R
        images.append(temp.reshape((32, 32, 3)))
    return data, labels

batchs = gb.glob("files/cifar10/data_batch_*")
tests = gb.glob("files/cifar10/test_batch*")

trainX, trainY = [], []
for file in batchs:
    data, labels = extract_cifar_batch(file)
    for index in range(len(data)):
        trainX.append(data[index])
        trainY.append(labels[index])
        
trainX, trainY = map(np.array, (trainX, trainY))
testX, testY = map(np.array, extract_cifar_batch(tests[0]))

print(trainX.shape, trainY.shape, testX.shape, testY.shape)

KnnClassifier = KNeighborsClassifier()
KnnClassifier.fit(trainX, trainY)
print(KnnClassifier.score(testX, testY))