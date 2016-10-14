from Graph import StaticGraph,DirectedStaticGraph

if __name__ == '__main__':
    x = [[0,1,0],
         [0,0,1],
         [1,0,0]]
    # 0 points to 1
    # 1 points to 2
    # 2 points to 0
    z = DirectedStaticGraph(x)
    print(z.neighbors(2)) # should return (0,1)
    print(z.getVertices())
    print(z.getAdjMat())
    print(z.getNext(0))
    print(z.getNext(1))