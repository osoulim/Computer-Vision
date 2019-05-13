import cv2
import glob
import random
import numpy as np
# Emotion list
emojis = ["neutral", "anger", "contempt", "disgust",
          "fear", "happy", "sadness", "surprise"]
# Initialize fisher face classifier
fisher_face = cv2.face.FisherFaceRecognizer_create()

data = {}
# Function defination to get file list, randomly shuffle it and split 67/33


def getFiles(emotion):
    files = glob.glob("final_dataset\\%s\\*" % emotion)
    random.shuffle(files)
    training = files[:int(len(files)*0.67)]  # get first 67% of file list
    prediction = files[-int(len(files)*0.33):]  # get last 33% of file list
    return training, prediction


def makeTrainingAndValidationSet():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emojis:
        training, prediction = getFiles(emotion)
        # Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item)  # open image
            # convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # append image array to training data list
            training_data.append(gray)
            training_labels.append(emojis.index(emotion))

        for item in prediction:  # repeat above process for prediction set
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray)
            prediction_labels.append(emojis.index(emotion))

    return training_data, training_labels, prediction_data, prediction_labels


def runClassifier():
    training_data, training_labels, prediction_data, prediction_labels = makeTrainingAndValidationSet()

    print("training fisher face classifier suing the training data")
    print("size of training set is:", len(training_labels), "images")
    fisher_face.train(training_data, np.asarray(training_labels))

    print("classification prediction")
    counter = 0
    right = 0
    wrong = 0
    for image in prediction_data:
        pred, conf = fisher_face.predict(image)
        if pred == prediction_labels[counter]:
            right += 1
            counter += 1
        else:
            wrong += 1
            counter += 1
    return ((100*right)/(right + wrong))


# Now run the classifier
metascore = []
for i in range(0, 10):
    right = runClassifier()
    print("got", right, "percent right!")
    metascore.append(right)

print("\n\nend score:", np.mean(metascore), "percent right!")
