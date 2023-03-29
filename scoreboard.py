from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
    def update_scoreboard(self):
        """
            Uppdaterar nuvarande bräde med poängen.
        """
        pass
    
    def game_over(self):
        """
            Skriver GAME OVER mitt på skärmen.        
        """
    
    def next_level(self):
        """
            Ökar nivån. Tar bort gamla scoreboarden. Skriver ut en ny.
        """