from Graph import *
from Tile import *


class Level:
    def __init__(self, Tiles, Height=10, Width=10, Tiling=None, Resources=None, Resource_Frequency=None,
                 Function=Graph.random_choose, Player_location=None):
        self.height = Height  # height of room
        self.width = Width  # width of room
        self.tiles = Tiles  # tileset
        self.resources = []  # array of resources
        self.function = Function  # function to be used within map/tiling generation
        self.noTiling = False  # if there is no tiling made
        self.player_loc = Player_location  # player location

        if Tiling is None:  # if no preset tiling
            self.tiling = Graph(self.height, self.width)  # generate a blank graph
            self.tiling.gen(self.tiles, self.function)  # generate tiling
        else:
            self.tiling = Tiling  # load preset tiling [graph object]

        if not self.noTiling:
            if Resources is None:  # if no preset Resources matrix
                if Resource_Frequency is None:  # if no set resource frequency
                    self.sync_resources_from_tiles()  # sync the resources from the tiles
                else:  # if there is a set resource frequency
                    for i in range(self.height):  # going through the height of the level
                        self.resources.append([])  # appends a row
                        for j in range(self.width):  # for the width of the level
                            self.resources[i].append(self.random_resource(
                                Resource_Frequency))  # possibly appends a resource there depending on the resource frequency
                    self.sync_resources_to_tiles()  # syncs the resources from the level array to the tiles
            else:  # if there is a set resource array
                self.resources = Resources  # set resources to be the passed matrix
                self.sync_resources_to_tiles()  # sync the resources from our level matrix to the tiles

    def update_player_loc(self):
        for i in self.height:  # go through the height of the level
            for j in self.width:  # go through the width of the level
                if self.tiling[i][j].is_player_here():  # if the player is at the tile
                    self.player_loc = (i, j)  # set the player location to the location of that tile
                    return  # no need to continue

    def random_resource(self, frq):  # takes resource frequency and spits out a resource list (can be empty)
        res = []
        pass  # not written at the moment but would take the resource frequency and spit out a list of resources (none to however many could be stored in the tile)

    def re_gen(self):  # regenerate a tiling
        self.tiling = Graph(self.height, self.width)  # generate a blank graph
        self.tiling.gen(self.tiles, self.function)  # generate tiling

    def update_function(self, funct): #update the function for tile generation based on the parameter
        self.function = funct

    def get_function(self): #getter function for the function
        return self.function

    def get_resource(self, row, col): #getter function for resource from a tile
        return self.resources[row][col]

    def sync_resources_from_tiles(self): #syncs resources to level matrix from tile
        for i in range(self.height):  # for each # of rows
            self.resources.append([])  # add row
            for j in range(self.width):  # for each # of columns
                self.resources[i].append(
                    [self.tiling.matrix[i][j]])  # add resources from correspodning tile

    def sync_resources_to_tiles(self): #syncs resources from level matrix to tile
        for i in range(self.height):  # for each # of rows
            for j in range(self.width):  # for each # of columns
                self.tiling[i][j].set_resource(self.resources[i][j])  # add resources to correspodning tile

    def where_player_goes(self): #array of where player can go
        arr = [] #empty array
        for i in range(self.height):#go through height of room
            arr.append([]) #add row
            for j in range(self.width): #go through width
                arr[i].append(self.tiling[i][j].canGo) #add whether of not you can go there from the tiling
        return arr  # returns an array representing where the player can and can't go in the map (true/false)

    def map_player_pov(self): #map from player perspective
        arr = [] #empty map
        for i in range(self.height): #go through height
            arr.append([]) # add row
            for j in range(self.width): #go through width
                if self.tiling[i][j].is_player_here(): #if player is there, add 2
                    arr[i].append(2)
                elif self.tiling[i][j].canGo: #otherwise if they can go there, add 1
                    arr[i].append(1)
                else: #otherwise add 0
                    arr[i].append(0)
        return arr  # returns an array representing where the player is (2), can (1) and can't (0) go
