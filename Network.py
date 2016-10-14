import numpy as np


class Network(object):

	# NEW STRUCTURAL ORGANIZATION - FASTER THAN PREVIOUS VERSION 
	
	# Contains the following member variables:
	# self.__weights : n x n weight matrix, where n is the total number of vertices in the graph. 
	#					self.__weights[i][j] is the weight connecting vertex i to vertex j.
	# self.__data : 1 x n array of data.
	# self.__inputLength : an integer representing the length of expected input data
	# self.__outputLength : an integer representing the length of exepcted output data
	# self.__neurons : 1 x (n-k) array of neuron objects, where k is the length of input data
	# self.__activeVertices : 1 x (n-k) array of vertex indices in active layer 
	#			ie. neurons = self.data[(activeLayer,)] 

	def __init__(self,inputLength=None,outputLength=None):
		self.setInputLength(inputLength)
		self.setOutputLength(outputLength)

	# begin getter/setter methods
	def setWeights(self,weights):
		# sets self.__weights
		self.__weights = weights

	def getWeights(self):
		# gets self.__weights
		return self.__weights

	def setNeurons(self,neurons):
		# sets self.__neurons
		self.__neurons = neurons

	def getNeurons(self):
		# gets self.__neurons
		return self.__neurons

	def setData(self,data):
		# sets self.__data
		self.__data = data

	def getData(self):
		# gets data
		return self.__data

	def setInputLength(self,inputLength):
		# sets self.__inputLength
		self.__inputLength = inputLength

	def getInputLength(self):
		# gets self.__inputLength
		return self.__inputLength

	def setOutputLength(self,outputLength):
		# sets output length
		self.__outputLength = outputLength

	def getOutputLength(self):
		#gets output length
		return self.__outputLength

	def setInputLayer(self,inputData):
		# sets input layer of data
		if self.getInputLength() is None:
			self.setInputLength(len(inputData))
		elif len(inputData) != self.getInputLength():
			raise ValueError("InputData must have same length as self.inputLength")
		self.getData()[:self.getInputLength()] = inputData

	def setLearningRate(self,learningRate):
		# sets learning rate
		self.__learningRate = learningRate

	def getLearningRate(self):
		# gets learning rate
		return self.__learningRate

	def getOutputLayer(self):
		# gets output layer of data
		if self.getOutputLength() is None:
			raise ValueError("OutputLength must be set before operation.")
		return self.getData()[-self.getOutputLength():]

	def getActiveVertices(self):
		# gets array of active vertices
		if self.getInputLength() is None:
			raise ValueError("Input length must be set prior to operation")
		return self.getVertices()[self.inputLength():]

	def getOutputVertices(self):
		# gets output vertices
		if self.getOutputLength() is None:
			raise ValueError("Output length must be set prior to operation.")
		return self.getVertices()[-self.getOutputLength():]
	# end getter/setter methods

	def compute(self,inputData):
		self.setInputLayer(inputData)
		for vertex in self.getActiveVertices():
			self.getData()[vertex] = self.activate(vertex,self.dot(vertex))
		return self.getOutputLayer()

	# begin support methods for self.compute()
	def dot(self,vertex):
		inData = self.getData()[np.where(self.getAdjMat()[:,vertex] == 1)] # get input data
		weights = self.getWeights()[:,vertex] # get weights
		return np.dot(inData,weights)

	def activate(self,vertex,data):
		# computes the activation function of the neuron located at vertex
		return self.getNeurons()[vertex].activate(data)
	# end support methods for self.compute()	

	def backpropagation(self,exampleInput,exampleOutput):
		self.compute(exampleInput)
		self.compute(exampleInput)
		self.getOuputError(exampleOutput)
		self.getHiddenError()
		self.updateWeights()

	# begin support methods for backpropagation
	def getOutputError(self,exampleOutput):
		index = 0
		for vertex in self.getOutputVertices():
			neuron = self.getNeurons()[vertex]
			output = self.getData()[vertex]
			self.getErrors()[vertex] = neuron.getError(output) * (output - exampleOutput[index])
			index += 1

	def getHiddenError(self):
		for vertex in self.getHiddenVertices():
			neuron = self.getNeurons()[vertex]
			output = self.getData()[vertex]
			downstream = self.getDownstreamVertices()
			self.getErrors()[vertex] = neuron.getError(output) * np.dot(
				self.getErrors()[downstream],self.getWeights()[vertex,downstream])

	def updateWeights(self):
		deltaWeights = self.getLearningRate() * np.outer(self.getData(),self.getErrors())
		self.setWeights(self.getWeights() + deltaWeights)

	def getDownstreamVertices(self,vertex):
		# returns vertices immediately downstream from vertex
		return self.getVertices()[np.where(self.getAdjMat()[vertex,:] == 1)]

	# end support methods for backpropagation

if __name__ == '__main__':
	x = Network()
	x.setData(np.zeros(10))
	x.setInputLayer(np.array([1,2,3]))

	print(x.getData())