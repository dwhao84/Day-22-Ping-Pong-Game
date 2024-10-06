"""
1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
6. Keep score
"""
import time

"""
paddle = 短槳
paddle:
    width = 20
    height = 100
    x_pos = 350
    y_pos = 0
can move the paddle by using 20px each of time.
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) # Turn off the animation in turtle.

# 建立paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# 建立ball
ball = Ball()

screen.listen() # 監聽螢幕
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # Refresh the state for screen.
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce() # Call bounce method.
screen.exitonclick()

