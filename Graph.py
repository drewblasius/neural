# graph class

class Graph(object):
	# The graph object assumes that you pass in a adjacency vertex matrix
	def __init__(self,adjList=None):
		self.setAdjList(adjList)
		self.setVertexTable({})
		sefl.setEdgeTable({})
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


