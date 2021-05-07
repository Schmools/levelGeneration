from Graph import *
from Tile import *


class Level:
    def __init__(self, Tiles, Height=10, Width=10, Tiling=None, Resources=None, Resource_Frequency=None,
                 Function=Graph.random_choose(), Player_location=None):
        self.height = Height  # height of room
        self.width = Width  # width of room
        self.tiles = Tiles
        self.resources = []
        self.function = Function
        self.noTiling = False
        self.player_loc = Player_location

        if Tiling is None:  # if no preset tiling
            self.tiling = Graph(self.height, self.width)  # generate a blank graph
            self.tiling.gen(self.tiles, self.function)  # generate tiling
        else:
            self.tiling = Tiling  # load preset tiling [graph object]

        if not self.noTiling:
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

    def update_player_loc(self):
        for i in self.height:
            for j in self.width:
                if self.tiling[i][j].is_player_here():
                    self.player_loc = (i, j)
                    return

    def random_resource(self, frq):  # takes resource frequency and spits out a resource list (can be empty)
        res = []
        pass

    def re_gen(self):
        self.tiling = Graph(self.height, self.width)  # generate a blank graph
        self.tiling.gen(self.tiles, self.function)  # generate tiling

    def update_function(self, funct):
        self.function = funct

    def get_function(self):
        return self.function

    def get_resource(self, row, col):
        return self.resources[row][col]

    def sync_resources_from_tiles(self):
        for i in range(self.height):  # for each # of rows
            self.resources.append([])  # add row
            for j in range(self.width):  # for each # of columns
                self.resources[i].append(
                    [self.tiling.matrix[i][j]])  # add resources from correspodning tile

    def sync_resources_to_tiles(self):
        for i in range(self.height):  # for each # of rows
            for j in range(self.width):  # for each # of columns
                self.tiling[i][j].set_resource(self.resources[i][j])  # add resources to correspodning tile

    def where_player_goes(self):
        arr = []
        for i in range(self.height):
            arr.append([])
            for j in range(self.width):
                arr[i].append(self.tiling[i][j].canGo)
        return arr  # returns an array representing where the player can and can't go in the map (true/false)

    def map_player_pov(self):
        arr = []
        for i in range(self.height):
            arr.append([])
            for j in range(self.width):
                if self.tiling[i][j].is_player_here():
                    arr[i].append(2)
                elif self.tiling[i][j].canGo:
                    arr[i].append(1)
                else:
                    arr[i].append(0)
        return arr  # returns an array representing where the player is (2), can (1) and can't (0) go
