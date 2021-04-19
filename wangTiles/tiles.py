#!usr/bin/env python
from scipy import *
from typing import *

class Map:
    def __init__(self, size: int):
       self.allTiles = [tile() for n in range(size)]
       self.adjacencyMatrix = rectangularGrid(size)

    def rectangular_grid(self, size: int):
        length = size*size
        matrix = numpy.zeros((length, length))

        for n in range(size):
            #self
            matrix[n][n] = 1
            #cross pattern: unsafe to set values outside matrix?
            matrix[n-1][n] = 1
            matrix[n+1][n] = 1
            matrix[n+size][n] = 1
            matrix[n-size][n] = 1

class Tile:
    def __init__(self, edges: int):
        #edgeColoring ought to be a tuple of duples (length, color)
        self.edgeColoring = []

    def get_edge(self, edge: int):
        return self.edgeColoring[edge]
    
    def set_edge_coloring(self, edge: int, edgeColor: Edge):
        self.edgeColoring[edge] = edgeColor

    class Edge:
    #define how to color edges
