from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-90, 270)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"score = {self.score}"  , font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(-90,0)
        self.write("GAME OVER" , font= ("Courier",24,"normal"))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
