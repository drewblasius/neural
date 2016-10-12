# graph class


class Graph(object):
    # The graph object assumes that you pass in a adjacency vertex matrix
    def __init__(self,adjList=None):
        if adjList is None:
            self.setAdjList({})
        else:
            self.setAdjList(adjList)
        self.setVertexTable({})
        self.setEdgeTable({})

    def setVertexTable(self,vertexTable):
        self.__vertexTable = vertexTable

    def getVertexTable(self):
        return self.__vertexTable

    def setEdgeTable(self,edgeTable):
        self.__edgeTable = edgeTable

    def getEdgeTable(self):
        return self.__edgeTable

    def setAdjList(self,adjList):
        self.__adjList = adjList

    def getAdjList(self):
        return self.__adjList

    def adjacent(self,x,y):
        return (y in self.getAdjList()[x])

    def neighbors(self,x):
        return self.getAdjList()[x]

    def addVertex(self,x):
        if x not in self.getAdjList():
            self.getAdjList()[x] = []

    def addEdge(self,x,y):
        if y not in self.getAdjList()[x]:
            self.getAdjList()[x].append(y)
            self.getAdjList()[y].append(x)

    def removeEdge(self,x,y):
        if y in self.getAdjList()[x]:
            self.getAdjList()[x].remove(y)
            self.getAdjList()[y].remove(x)

    def setVertexValue(self,x,value):
        self.getVertexTable()[x] = value

    def getVertexValue(self,x):
        return self.getVertexTable()[x]

    def setEdgeValue(self,x,y,value):
        self.getEdgeTable()[(x,y)] = value

    def getEdgeValue(self,x,y):
        return self.getEdgeTable()[(x,y)]


class DirectedGraph(Graph):
    def addEdge(self,x,y):
        if y not in self.getAdjList()[x]:
            self.getAdjList()[x].append(y)

    def removeEdge(self,x,y):
        if y in self.getAdjList()[x]:
            self.getAdjList()[x].remove(y)


class LayeredGraph(DirectedGraph):
    def __init__(self,adjList=None):
        # initializes the layer map
        super().__init__(adjList)
        self.setLayerMap([])

    def setLayerMap(self,layerMap):
        self.__layerMap = layerMap
        
    def getLayerMap(self):
        return self.__layerMap


class NeuralNetwork(LayeredGraph):
    # Class for implementing a neural network
    # The neural network is represented as a graph with layers, and operates
    # layer by layer in a feed-forward fashion.
    # The output data, errors are stored within the neurons, themselves.


    # TBD
    def __init__(self,adjList=None,neuronType=None):
        super().__init__(adjList)
        pass

    def pipe(self,vertex):
        # Takes output data from a single vertex and pipes it to the next vertices
        nextVertexList = self.neighbors(vertex)
        output         = self.getVertexValue(vertex).getOutput()
        for nextVertex in nextVertexList:
            self.getVertexValue(nextVertex).addToInput(output)

    def setInputLayer(self,inputData):
        # sets the first layer of the layer map to input
        inputLayer = self.getLayerMap()[0]
        for i in range(len(inputLayer)):
            vertex = inputLayer[i]
            self.getVertexValue(vertex).setInput(inputData[i]) # setting input data of each neuron

    def compute(self,inputData):
        self.setInputLayer(inputData)                         # setting up input layer
        for vertexLayer in self.getLayerMap():
            for vertex in vertexLayer:
                self.getVertexValue(vertex).compute() # each neuron does a computation
                self.pipe(vertex)                     # pipes data to next layer of neurons
        
    def backpropagation(self,trainingData,learningRate):
        for [example,result] in trainingData:
            self.compute(example)
            self.getOutputError(result)
            self.getHiddenError()
            self.updateWeights(learningRate)

    def getOutputError(self,example):
        # computes the error for output layer neurons
        outputLayer = self.getLayerMap()[-1]
        index = 0
        for vertex in outputLayer:
            output = self.getVertexValue(vertex).getOutput()
            actual = example[index]
            error = output * (1 - output) * (actual - output)
            self.getVertexValue(vertex).setError(error)    

    def getHiddenError(self):
        layerMap = self.getLayerMap()
        n = len(layerMap)
        for layerNum in range(n-2,0,-1):
            layer = layerMap[layerNum]
            for vertex in layer:
                downstreamSum = self.getDownstreamSum(vertex)
                output  = self.getVertexValue(vertex).getOutput()
                error  = output * (1 - output) * downstreamSum
                self.getVertexValue(vertex).setError(error)
        
    def getDownstreamSum(self,vertex):
        downstreamSum = 0
        weightIndex   = 1
        neuron = self.getVertexValue(vertex) 
        for nextVertex in self.neighbors(vertex):
            downstreamSum +=  neuron[weightIndex] * self.getVertexValue(nextVertex).getError()
            weightIndex += 1
        return downstreamSum

    def updateWeights(self,learningRate):
        for layer in self.getLayerMap():
            for vertex in layer:
                weightIndex = 1
                neuron = self.getVertexValue(vertex)
                for nextVertex in self.neighbors(vertex):
                    delta = learningRate * self.getVertexValue(vertex).getError() * \
                            self.getVertexValue(vertex).getInput()
                    neuron[weightIndex] = neuron[weightIndex] + delta
                    weightIndex += 1


