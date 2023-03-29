from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self) -> None:
        pass
    
    def create_car(self):
        """
            En metod som har en 1/6 sannolikhet att skapa en bil.
            Om bilen skapas så gör den det här som läggs i sin egna billista.
            
            Bilar kan vara slumpmässig färg.
            De bör vara en fyrkant.
            De bör ha en shapesize på wid 1 och len 3, kanske 2, du bestämmer.
            De börjar på koordinaten (300, -240 <= y <= 260).
            Bilarna borde titta vänster.
            
        """
        pass
    
    def move_cars(self):
        """
            Förflyttar alla bilar i billistan med den hastighet bilarna ska ha
            för nuvarande nivå.
        """
        pass
    
    def increase_speed(self):
        """
            Ökar hastigheten på samtliga bilar.
            Anropas när en nivå är avklarad.
        """
        pass