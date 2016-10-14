import numpy as np

# graph class


class StaticGraph(object):
    '''
    Class for a graph which does not have the flexibility to add/remove vertices or edges.
    The adjacency matrix of the graph must be specified at initialization.
    '''

    def __init__(self,adjMat,vertices=None):
        self.setAdjMat(adjMat)
        if vertices is None:
            self.setVertices([x for x in range(self.getAdjMat().shape[0])])
        else:
            self.setVertices(vertices)

    def setAdjMat(self,adjMat):
        '''
        Sets the adjacency matrix for the graph. 
        Assumes that the adjacency matrix takes the form of either a Python list or a numpy array. 
        Throws a type error if neither type is provided.
        '''
        if type(adjMat) is list:
            self.__adjMat = np.array(adjMat)
        else:
            self.__adjMat = adjMat

    def getAdjMat(self):
        '''
        Returns the adjacency matrix of the graph
        '''
        return self.__adjMat

    def setVertices(self,vertices):
        '''
        Sets the array of vertices of the graph.
        '''
        if type(vertices) is list:
            self.__vertices = np.array(vertices)
        else:
            self.__vertices = vertices

    def getVertices(self):
        '''
        Gets the array of vertices of the graph.
        '''
        return self.__vertices

    def neighbors(self,vertex):
        '''
        Returns a numpy array containing all of the vertices which are adjacent to vertex.
        '''
        indices1 = np.where(self.getAdjMat()[vertex,:] == 1)
        indices2 = np.where(self.getAdjMat()[:,vertex] == 1)
        return np.union1d(self.getVertices()[indices1],self.getVertices()[indices2])
        

class DirectedStaticGraph(StaticGraph):
    '''
    A directed static graph is a static graph but with the flexibility that the adjacency matrix of the graph need not be symmetric. 
     ie. self.getAdjMat()[i,j] = 1,   if i -> j
                                 0 ,  otherwise
    '''
    def getNext(self,vertex):
        ''' Returns the vertices pointed to by vertex'''
        indices = np.where(self.getAdjMat()[vertex,:] == 1)
        return self.getVertices()[indices]

    def getPrev(self,vertex):
        ''' Returns the vertices which have edges pointing to vertex'''
        indices = np.where(self.getAdjMat()[:,vertex] == 1)
        return self.getVertices()[indices]



