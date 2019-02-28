import numpy as np

class Generator:
    def GetVector(self, n, choise):
        if choise == 0:
            return np.random.random_sample(n)
        elif choise == 1:
            floatArray = np.random.random_sample(n)
            intArray = np.random.random_integers(-10, 10, n)
            return floatArray * intArray
        elif choise == 2:
            return np.random.random_integers(-10, 10, n)
        elif choise == 3:
            return np.random.random_integers(0, 20, n)
        elif choise == 4:
            return np.random.random_integers(0, 50, n)

    def GetMatrix(self, rows, cols, choise):
        if choise == 0:
            return np.random.random_sample((rows, cols))
        elif choise == 1:
            floatArray = np.random.random_sample((rows, cols))
            intArray = np.random.random_integers(-10, 10, (rows, cols))
            return floatArray * intArray
        elif choise == 2:
            return np.random.random_integers(-10, 10, (rows, cols))
        elif choise == 3:
            return np.random.random_integers(0, 20, (rows, cols))
        elif choise == 4:
            return np.random.random_integers(0, 50, (rows, cols))




