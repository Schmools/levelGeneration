class Tile:

    def __init__(self, t=None, r=None, b=None, l=None, CanGo=True, res=[], Player=False):
        self.borders = []
        self.borders.append(t)  # add top edge
        self.borders.append(r)  # add right edge
        self.borders.append(b)  # add bottom edge
        self.borders.append(l)  # add lower edge
        self.resource = res  # right now resources are just a list but i would like to enforce some type of structure eventually so that the lists owuld all take the same form --> potentailly a list of numbers where each index represents a specific resource that is uniform
        self.player = Player
        self.canGo = CanGo  # whether or not the player can go there

    def set(self, tile):
        for i in range(4):
            self.borders[i] = tile.borders[i]  # set border to the borders of the tile passed in

    def top(self):
        return self.borders[0]  # return top border

    def right(self):
        return self.borders[1]  # return right border

    def bottom(self):
        return self.borders[2]  # return bottom border

    def left(self):
        return self.borders[3]  # return left border

    def showBorders(self):
        print(self.borders, end=" ")  # print without making a new line

    def get_resources(self):
        return self.resources

    def set_resources(self, Resources):
        self.resource = Resources

    def is_player_here(self):
        return self.player

    def player_arrive(self):
        if self.canGo:
            self.player = True

    def player_leave(self):
        self.player = False

    def abs_edge_difference(self, t2):
        diff = 0
        for i in range(4):
            diff += abs(self.borders[i] - t2.borders[i])
        return diff

    def signed_edge_difference(self, t2):
        diff = 0
        for i in range(4):
            diff += self.borders[i] - t2.borders[i]
        return diff
