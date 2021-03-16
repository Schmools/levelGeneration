#!/usr/bin/env python
from scipy import *

class map:
    def __init__(self, size):
       allTiles = [tile() for n in range(size)]
       adjacencyMatrix = rectangularGride(size)

    def rectangularGrid(self, size):
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

class tile:
    def __init__ (self, edges):
        #edgeColoring ought to be a list of duples (length, color)
        #figure out type hinting
        edgeColoring = []
