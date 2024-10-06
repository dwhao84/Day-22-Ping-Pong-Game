"""
width = 20
height = 20
x_pos = 0
y_pos = 0
"""
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.speed("slow") # Adjust the ball's speed.
        print(self.xcor(), self.ycor())
        
    def bounce(self):
        self.y_move *= -1 # a = a * -1
        self.speed("slow")
