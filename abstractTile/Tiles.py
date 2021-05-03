#!usr/bin/env python
from scipy import *
from typing import *

class Map:
    def __init__(self, size: int):
       self.allTiles = [Tile() for n in range(size)]
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

        return matrix

class Tile:
    def __init__(self, edgeColouring = None):
        #edgeColouring ought to be a list of edges (an edge being a list of duples:length, colour)
        self.edgeColouring: list[Edge] = edgeColouring
        self.player: bool

    def get_edge(self, edge: int) -> Edge:
        return self.edgeColouring[edge]

    def is_player_here(self) -> bool:
        return self.player

    class Edge:
    #define how to colour edges
        def __init__(self, colourList):
            self.colourList: list[tuple[int, tuple[int, int, int]]] = colourList
            #                       length^  ^colour(R,G,B)
