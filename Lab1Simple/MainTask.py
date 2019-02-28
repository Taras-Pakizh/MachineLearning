import numpy as np
import sys

class MainTask:

    def __init__(self, array):
        if not isinstance(array, np.ndarray):
            raise Exception("MainTask __init__ get as parameter numpy.ndarray instance")
        self.array = array

    #task1
    def TaskVector(self, x, y):
        if self.array.ndim != 1:
            raise Exception("TaskVector works with 1 dimention array")
        result = 0
        check = False
        for item in self.array:
            if item < 0:
                check = True
                break
            if item >= x and item <= y:
                result += 1
        if check:
            return result
        else:
            return 0

    #task2
    def TaskMatrix(self):
        if self.array.ndim != 2:
            raise Exception("TaskMatrix works with 2 dimention array")

        current = [0, 0]
        Min = sys.maxsize
        columnMin = -1
        rows, cols = self.array.shape

        while current[0] < rows:
            current[1] = 0
            while current[1] < cols:
                if self.array[tuple(current)] > 0 and self.array[tuple(current)] < Min:
                    Min = self.array[tuple(current)]
                    columnMin = np.copy(current[1])
                current[1] += 1
            current[0] += 1

        if Min == 0:
            return self.array, -1

        if columnMin == cols - 1:
            return self.array, columnMin

        column = np.copy(self.array[:, columnMin])
        self.array[:, columnMin] = self.array[:, cols - 1]
        self.array[:, cols - 1] = column

        return self.array, columnMin



