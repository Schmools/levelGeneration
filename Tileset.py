from Tile import *


class Tileset:

    def __init__(self,
                 length=10):  # param1=, param2=, param3=, etc.""" --> a bunch more params would be here to generate the tileset
        self.len = length
        self.set = []
        for i in range(len):
            set.append(Tile())
