class Tile:

    def __init__(self, t=None, r=None, b=None, l=None):
        self.borders = []
        self.borders.append(t) #add top tile
        self.borders.append(r) #add right tile
        self.borders.append(b) #add bottom tile
        self.borders.append(l) #add lower tile

    def set(self, tile):
        for i in range(4):
            self.borders[i] = tile.borders[i] #set border to the borders of the tile passed in

    def top(self):
        return self.borders[0] #return top border

    def right(self):
        return self.borders[1] #return right border

    def bottom(self):
        return self.borders[2] #return bottom border

    def left(self):
        return self.borders[3] #return left border

    def showBorders(self):
        print(self.borders, end=" ")#print without making a new line