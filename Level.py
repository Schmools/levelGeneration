from Graph import *
from Tile import *


class Level:
    def __init__(self, Tiles, Height=10, Width=10, Tiling=None, Resources=None, Resource_Frequency=None):
        self.height = Height  # height of room
        self.width = Width  # width of room
        self.tiles = Tiles
        self.resources = []

        if Tiling is None:  # if no preset tiling
            self.tiling = Graph(self.height, self.width)  # generate a blank graph
            self.tiling.gen(self, self.tiles)  # generate tiling
        else:
            self.tiling = Tiling  # load preset tiling [graph object]

        if Resources is None:  # if no preset Resources matrix
            if Resource_Frequency is None:
                self.sync_resources_from_tiles()
            else:
                for i in range(self.height):
                    self.resources.append([])
                    for j in range(self.height):
                        self.resources[i].append(self.random_resource(Resource_Frequency))
                self.sync_resources_to_tiles()
        else:
            self.resources = Resources
            self.sync_resources_to_tiles()

    def random_resource(self, frq):  # takes resource frequency and spits out a resource list (can be empty)
        res = []
        pass

    def get_resource(self, row, col):
        return self.resources[row][col]

    def sync_resources_from_tiles(self):
        for i in range(self.height):  # for each # of rows
            self.resources.append([])  # add row
            for j in range(self.width):  # for each # of columns
                self.resources[i].append(
                    [self.tiling[i][j]])  # add resources from correspodning tile

    def sync_resources_to_tiles(self):
        for i in range(self.height):  # for each # of rows
            for j in range(self.width):  # for each # of columns
                self.tiling[i][j].set_resource(self.resources[i][j])  # add resources to correspodning tile
