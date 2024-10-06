from turtle import Turtle
CENTER = "center"
FONT = "courier", 80, "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        # turtle.write()
        # This function is used to write text at the current turtle position.
        self.write(self.left_score, align=CENTER, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=CENTER, font=FONT)

    def right_side_got_score(self):
        self.right_score += 1
        self.update_scoreboard()
    
    def left_side_got_score(self):
        self.left_score += 1
        self.update_scoreboard()
        
    
    