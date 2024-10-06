from turtle import Turtle

# 建立Paddle的superclass，並帶入Turtle作為subclass。
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(position)
    
    # 建立go_up的功能。
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y) # print out the ball's coordinate
    
    # 建立go_down的功能。
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)