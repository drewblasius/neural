
class Neuron(object):

	def __init__(self,threshold=None):
		self.setThreshold(threshold)

	def setThreshold(self,threshold):
		self.__threshold = threshold

	def getThreshold(self):
		return self.__threshold

	def activate(self,data):
		# abstract method for subclasses
		pass

	def getError(self,data):
		# abstract method to be subclassed
		pass


class Perceptron(Neuron):
	def activate(self,data):
		if data > self.getThreshold():
			return 1
		else:
			return 0

	def getError(self,data):
		pass


class Sigmoid(Neuron):
	def activate(self,data):
		s = data - self.getThreshold()
		return 1 / (1 + np.exp(-s))

	def getError(self,data):
		pass


class ArcTanhSigmoid(Neuron):
	def activate(self,data):
		pass

	def getError(self,data):
		pass


class Pipe(Neuron):
	def activate(self,data):
		pass

	def getError(self,data):
		return 1
		