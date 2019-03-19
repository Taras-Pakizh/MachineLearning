import pandas as pd
import numpy as np

from sklearn.datasets import fetch_lfw_pairs
from PIL import Image

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 

import interface as ui

#Main ---------------
def main():
    ui.btn.bind("<Button-1>", Run)
    ui.root.mainloop()

#Run event
def Run(e):

    neighbors = ui.ScaleNeighbors.get()
    photos = ui.ScalePhotos.get()
    testSize = ui.ScaleTestSize.get()

    try:
        bunch = fetch_lfw_pairs()
        DataTrain, DataTest, TargetTrain, TargetTest = train_test_split(bunch.data, bunch.target, test_size = testSize)

        learner = KNeighborsClassifier(n_neighbors = neighbors)
        learner.fit(DataTrain, TargetTrain)
        TargetPredict = learner.predict(DataTest)
        
        figure = plt.figure()
        figure.canvas.set_window_title('K = %i' % neighbors)

        index = 0
        rows, cols = GetGrid(photos)

        while index < photos:
            plt.subplot(rows, cols, index + 1)
            plt.axis('off')
            images = np.empty([62, 94])
            images[:, :47] = DataTest[index][:2914].reshape(62, 47)
            images[:, 47:] = DataTest[index][2914:].reshape(62, 47)
            plt.imshow(images, interpolation='nearest')
            plt.title('Predict: ' + str(bunch.target_names[TargetPredict[index]]) + "\nTrue: " + str(bunch.target_names[TargetTest[index]]))
            index += 1

        plt.subplot(rows, cols, index + 1)
        plt.axis('off')
        plt.imshow(np.zeros(62*94).reshape(62, 94), cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Accuracy: ' + str(learner.score(DataTest, TargetTest)))

        plt.show()
    
    except Exception as e:
        print(e)

def GetGrid(photos):
    count = photos + 1
    if count < 4:
        return (1, 3)
    elif count < 7:
        return (2, 3)
    elif count < 9:
        return (2, 4)
    else:
        return (3, 4)

if __name__ == "__main__":
    main()