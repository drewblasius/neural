import numpy as np
from Graph import MetaLayeredGraph

class Neuron(object):
    # Simple class for a neuron. The neuron's main job is computation.
    # The neuron class has methods for getting and setting weights and has a dot operation which is
    # universal in all classes.

    def __init__(self,numWeights=None):
        if numWeights is None:
            self.setWeights(None)
        else:
            self.setWeights([0]*numWeights)
        self.clearInputCache()

    def setWeights(self,weights):
        # Sets weights
        if type(weights) is np.ndarray or weights is None:
            self.__weights = weights
        elif type(weights) is list:
            self.__weights = np.array(weights)
        else:
            raise TypeError("Expected weights to be of type list or np.ndarray")

    def getWeights(self):
        # Gets weights
        return self.__weights

    def __setitem__(self,index,value):
        weights = self.getWeights()
        weights[index] = value
        self.setWeights(weights)

    def __getitem__(self,index):
        return self.getWeights()[index]

    def setInputCache(self,inputCache):
        self.__inputCache = inputCache

    def getInputCache(self):
        return self.__inputCache

    def clearInputCache(self):
        self.setInputCache([])

    def addInput(self,x):
        cache = self.getInputCache()
        self.setInputCache(cache.append(x))

    def dot(self,x):
        # Given an input vector x, computes w.x
        if type(x) is list:
            x = np.array( [1] + x )
        elif type(x) is np.ndarray:
            x = np.concatenate((np.array([1]),x))
        else:
            raise TypeError("Expected weights to be of type list or np.ndarray")

        return np.dot(x,self.getWeights()

    def operate(self):
        # Takes data from input cache and then clears input cache
        x = self.getInput()
        output = self.function(x)
        self.clearInputCache()

    def function(self,x):
        pass


class Perceptron(Neuron):
    def function(self,x):
        if self.dot(x) > 0:
            return 1
        else:
            return -1


class Sigmoid(Neuron):
    def function(self,x):
        net = self.dot(x)
        return 1 / (1 + np.exp(-net))




if __name__ == '__main__':
    # Neuron testing block
    """
    print('>>x = Neuron()')
    x = Neuron()
    print('>>x.getWeights() -> None')
    print(x.getWeights())
    print('>>x.getNext() -> None')
    print(x.getNext())
    print('>>x.getPrev() -> None')
    print(x.getPrev())
    x.setWeights([0,1,2])
    print('>>x.getWeights() -> [0 1 2]')
    print(x.getWeights())
    print('>>x[1] -> 1')
    print(x[1])
    print('>>x[1] = 5')
    x[1] = 5
    print('>>x.getWeights() -> [0 5 2]')
    print(x.getWeights())
    print('>>x.dot([1,2]) -> 9')
    print(x.dot([1,2]))
    print('>>x.dot(np.array([1,2])) -> 9')
    print(x.dot(np.array([1,2])))
    """
