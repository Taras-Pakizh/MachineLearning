from sklearn.datasets import load_boston
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    boston = load_boston()
    reg = LinearRegression()

    DataTrain, DataTest, TargetTrain, TargetTest = train_test_split(boston.data, boston.target, test_size = 0.25)

    reg.fit(DataTrain, TargetTrain)

    TargetPredict = reg.predict(DataTest)

    plt.subplots()
    plt.axis([TargetTest.min(), TargetTest.max(), TargetTest.min(), TargetTest.max()])
    plt.scatter(TargetTest, TargetPredict, edgecolors=(0, 0, 0), color='red')
    plt.plot([TargetTest.min(), TargetTest.max()], [TargetTest.min(), TargetTest.max()], 'b--', lw=3)
    plt.xlabel('Real')
    plt.ylabel('Predicted')
    plt.show()

if __name__ == '__main__':
    main()