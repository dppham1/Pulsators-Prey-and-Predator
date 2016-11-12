# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey):
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Ball.radius*2, Ball.radius*2, 0, 5)
        self.randomize_angle()
        
    def update(self, model):
        self.move()
        
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0] - Ball.radius,\
                           self.get_location()[1] - Ball.radius,\
                           self.get_location()[0] + Ball.radius,\
                           self.get_location()[1] + Ball.radius, fill = 'blue')