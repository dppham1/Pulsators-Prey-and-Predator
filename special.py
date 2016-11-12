# My special is a new object that is purple, with a radius of 15.
# Every cycle it creates either a new ball or a floater at its location.


from simulton import Simulton
from ball import Ball
from floater import Floater
from random import random

class Special(Simulton):
    radius = 15
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Special.radius*2, Special.radius*2)
        
    
    def update(self, model):
        if random() <= .5:
            model.add(Ball(self._x, self._y))
        else:
            model.add(Floater(self._x, self._y))
        
        
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0] - int(self.get_dimension()[0]/2),\
                           self.get_location()[1] - int(self.get_dimension()[1]/2),\
                           self.get_location()[0] + int(self.get_dimension()[0]/2),\
                           self.get_location()[1] + int(self.get_dimension()[1]/2), fill = 'purple')
        
        
        