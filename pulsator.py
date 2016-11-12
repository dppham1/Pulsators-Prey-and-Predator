# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    small_con = 30
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.count = 0
        
    def update(self, model):
        stomach = Black_Hole.update(self, model)
        self.count += 1
        if len(stomach) >= 1:
            self.change_dimension(2, 2)
            self.count = 0
        if self.count == Pulsator.small_con:
            self.change_dimension(-2, -2)
            self.count = 0
        if self._width == 0 and self._height == 0:
            model.remove(self)
        return stomach
            
        