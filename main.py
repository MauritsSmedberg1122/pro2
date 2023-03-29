import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Turtle Crossing")
screen.tracer(0)

player_turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
game_is_on = True

if __name__ == "__main__":
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        
        # Skriv resten av spelet
        
        
        # För att checka collision mellan bilar och sköldpaddan
        # använd spelar_turtle.distance("bil") < 20, om detta är sant så har man krockat
    
    screen.exitonclick()