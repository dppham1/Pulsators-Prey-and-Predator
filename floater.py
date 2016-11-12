# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage

from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.radius*2, Floater.radius*2, 0, 5)
        self.randomize_angle()
        
    def update(self, model):
        rint = random()
        new_speed, new_angle = random() - .5, random() - .5
        if rint <= .3:
            if self.get_speed() + new_speed >= 3 and self.get_speed() + new_speed <= 7:
                self.set_velocity(self.get_speed() + new_speed, self.get_angle() + new_angle)
            else:
                self.set_angle(self.get_angle() + new_angle)
        self.move()
            
        
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0] - Floater.radius,\
                           self.get_location()[1] - Floater.radius,\
                           self.get_location()[0] + Floater.radius,\
                           self.get_location()[1] + Floater.radius, fill = 'red')
        
        