import numpy as np

# graph class


class StaticGraph(object):
    # Class for a graph which does not have the flexibility to add/remove vertices
    #   or edges.
    # The adjacency matrix of the graph must be specified at initialization

    def __init__(self,adjMat):
        self.setAdjMat(adjMat)
        self.setVertices([x for x in range(shape(adjMat))[0]])

    def setAdjMat(self,adjMat):
        # setter for self.__adjMat
        if type(adjMat) is list:
            self.__adjMat = np.array(adjMat)
        else:
            self.__adjMat = adjMat

    def getAdjMat(self):
        # getter for self.__adjMat
        return self.__adjMat

    def setVertices(self,vertices):
        # setter for self.__vertices
        if type(vertices) is list:
            self.__vertices = np.array(vertices)
        else:
            self.__vertices = vertices

    def getVertices(self):
        # getter for self.__vertices
        return self.__vertices

    def neighbors(self,vertex):
        # gets vertices adjacent to vertex
        indices = np.where(self.getAdjMat()[vertex,:] == 1 
                            or self.getAdjMat()[:,vertex] == 1)
        return self.getVertices()[indices]
        


class DirectedStaticGraph(StaticGraph):
    # A directed static graph is a static graph but with the flexibility that 
    # the adjacency matrix of the graph need not be symmetric. 
    # ie. self.getAdjMat()[i,j] = 1,   if i -> j
    #                             0 ,  otherwise

    def getNext(self,vertex):
        # gets the vertices which are pointed to by x
        indices = np.where(self.getAdjMat()[vertex,,:] == 1)
        return self.getVertices()[indices]

    def getPrev(self,vertex):
        # gets the vertices which point to x
        indices = np.where(self.getAdjMat()[:,vertex] == 1)
        return self.getVertices()[indices]


