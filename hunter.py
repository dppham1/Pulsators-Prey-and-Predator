# A Hunter is both a Mobile_Simulton and a Pulsator: it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    view = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, 0, 5)
        self.randomize_angle()
        
    def update(self, model):
        stomach = Pulsator.update(self, model)
        close_prey = model.find(lambda item: self.distance((item._x, item._y)) <= Hunter.view and isinstance(item, Prey))
        shortest_dist = 200
        follow = None
        if len(close_prey) >= 1:
            for preys in close_prey:
                if self.distance(preys.get_location()) < shortest_dist:
                    shortest_dist = self.distance(preys.get_location())
                    follow = preys
            self.set_angle(atan2(follow._y - self._y, follow._x - self._x))
        self.move()
        return stomach
        
        
        