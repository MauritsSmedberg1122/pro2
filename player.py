from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        
    def move(self):
        """
            Flyttar på spelaren.
        """
        pass
    
    def check_win(self):
        """
            Kontrollera ifall spelaren är över mållinjen.
            Om ja så bör nivån börja om och bli svårare.
        """
        pass
        
    