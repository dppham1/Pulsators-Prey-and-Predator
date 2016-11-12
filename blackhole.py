# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.radius*2, Black_Hole.radius*2)
        
    def contains(self, xy):
        return self._width/2 > self.distance(xy) and self._height/2 > self.distance(xy)
    
    def update(self, model):
        prey = model.find(lambda item: isinstance(item, Prey))
        cobj = model.find(lambda item: self.contains(item.get_location()))
        for n in prey:
            if n in cobj:
                model.remove(n)
        return {i for i in prey if i in cobj}
    
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0] - int(self.get_dimension()[0]/2),\
                           self.get_location()[1] - int(self.get_dimension()[1]/2),\
                           self.get_location()[0] + int(self.get_dimension()[0]/2),\
                           self.get_location()[1] + int(self.get_dimension()[1]/2), fill = 'black')
        
        
        
        