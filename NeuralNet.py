import numpy as np

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


class Network(object):
    # Collection of neurons arranged in an acyclic fashion
    # The Neurons are responsible for computing outputs given inputs, 
    # while the network class manages passing data in between network layers
    # The Network does so as follows:
    # 	- Keeps track of the neuron layers via a 2d array, where the indices are given by 
    #		(layerNumber,neuronNumber), and the first and last layers are all None
    # 	- Keeps track of the connections via a directed adjacency list which tells us which neurons
    # 		feed to which neurons

    def __init__(self,adjList):
        pass

    def setAdjList(self,adjList):
    	# 2D Array which gives us the graph structure
    	self.__adjList = adjList

    def getAdjList(self):
    	return self.__adjList

    def setNeuronMap(self,neuronMap):
        # 2D Array which give us the neuron structure
    	self.__neuronMap = neuronMap

    def getNeuronMap(self):
    	return self.__neuronMap

    def getNewDataMap(self):
        pass

    def setNewDataMap(self,dataMap):
        pass

    def pipeData(self,layerIndex,dataLayer):
        # pipes data to the next neuron given the current neuron's layerIndex and dataIndex
        adjLayer  = self.getAdjList()[layerIndex]
        dataIndex = 0
        for data in dataLayer:
            indexList = adjLayer[dataIndex] # produces a list of indices to which the data must be piped
            for index in indexList:
                [targetLayer,targetIndex] = index
                self.getNeuronMap()[targetLayer][targetIndex].addInput(data)
            dataIndex += 1

        # indexList = self.getAdjList()[layerIndex][dataIndex]
        # for index in indexList:
        #     [targetLayer, targetIndex] = index
        #     self.getNeuronMap()[targetLayer][targetIndex].addInput(item)

    def operateLayer(self,layerIndex):
        dataLayer = []
        for neuron in self.getNeuronMap()[layerIndex]:
            dataLayer.append(neuron.operate())
        return dataLayer

    def operate(self,inputData):
    	# Expects input data to be a list of data
        # Preallocating is necessary, but can be figured out later
        dataMap = self.getNewDataMap()
    	dataMap[0] = inputData
    	layerIndex = 0
    	for dataLayer in dataMap:	

            # Piping the data to the next neuron(s)
    		self.pipeData(layerIndex,dataLayer)
            # Operating on the piped data
            newLayer = self.operateLayer(layerIndex + 1)
            dataMap[layerIndex+1] = newLayer

        return dataMap

    def backpropagation(self,trainingDataSet,trainingDataResults):
        for i in range(len(trainingDataSet)):
            # operate on the data to get outputs at each step
            errorMap  = getNewDataMap()
            outputMap = self.operate(trainingDataSet[i]) 
            tData     = trainingDataResults[i]              # training data for this particular training example
            
            # computing error on output units
            self.getOutputError(outputMap,tData,errorMap)
            # computing error on hidden units
            self.getHiddenError(outputMap,tData,errorMap)
            

    def getOutputError(self,outputMap,tData,errorMap):
        outputLayer = outputMap[-1]
        for j in range(len(outputLayer)):
            errorMap[-1][j] = outputLayer[j] * (1 - outputLayer[j]) * (tData[j] - ouputLayer[j])

    def getHiddenError(self,outputMap,tData,errorMap):
        for j in range(len(outputMap)-2,0,1):
                for k in range(len(outputMap[j])):
                    downstreamSum = self.getDownstreamSum(j,k,outputMap,errorMap)
                    errorMap[j][k] = outputMap[j][k] * (1 - outputMap[j][k]) * downstreamSum

    def getDownstreamSum(self,j,k,outputMap,errorMap): # not finished!!!
        # here, I noticed that we're required to actually maintain an adjacency list of the dual graph, too.
        # could be problematic/hard to implement, but not for now
        downstreamSum = 0
        for [downLayer,downIndex] in self.getAdjList()[j][k]:
            downstreamSum += errorMap[downLayer][downIndex] * # self.getNeuronMap()[downLayer][downIndex] 
        return downstreamSum





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
