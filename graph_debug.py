debug = 2
import Graph as g

# Graph debugging portion
if __name__ == '__main__' and debug==0:
	print("Graph debugging")
	x = g.Graph()
	x.addVertex(0)
	x.addVertex(1)
	x.addVertex(2)
	x.addVertex(3)
	x.addEdge(0,1)
	x.addEdge(0,2)
	x.addEdge(0,3)
	x.addEdge(1,2)
	x.setVertexValue(0,'red')
	x.setVertexValue(1,'blue')
	print(x.getVertexValue(0))
	print(x.getVertexValue(1))
	x.setVertexValue(0,'green')
	print(x.getVertexValue(0))
	print(x.getAdjList())

# Directed Graph debugging portion
if __name__ == '__main__' and debug == 1:
	print("DirectedGraph debugging")
	x = g.DirectedGraph()
	x.addVertex(0)
	x.addVertex(1)
	x.addVertex(2)
	x.addVertex(3)
	x.addEdge(0,1)
	x.addEdge(0,2)
	x.addEdge(0,3)
	x.addEdge(1,2)
	x.setVertexValue(0,'red')
	x.setVertexValue(1,'blue')
	print(x.getVertexValue(0))
	print(x.getVertexValue(1))
	x.setVertexValue(0,'green')
	print(x.getVertexValue(0))
	print(x.getAdjList())

if __name__ == '__main__' and debug == 2:
	print("LayeredGraph debugging")
	x = g.LayeredGraph()
	x.addVertex(0)
	x.addVertex(1)
	x.addVertex(2)
	x.addVertex(3)
	x.addEdge(0,1)
	x.addEdge(0,2)
	x.addEdge(0,3)
	x.addEdge(1,2)
	x.setVertexValue(0,'red')
	x.setVertexValue(1,'blue')
	print(x.getVertexValue(0))
	print(x.getVertexValue(1))
	x.setVertexValue(0,'green')
	print(x.getVertexValue(0))
	print(x.getAdjList())
	x.getLayerMap().append([1,2])
	x.getLayerMap().append([3,0])
	print(x.getLayerMap())