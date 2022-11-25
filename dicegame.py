from random import randint
from time import strftime
 
class Player:

   def __init__(self, name, score=0, wins=0, lastroll=0):
    """
    sets all paramters to 0 besides name. 
    """
    """
    Attribut
    Name : str
    Score : int
    Wins : int
    Lastroll: int, default 0
    """

    self.Name = name 
    self.Score = score
    self.Wins = wins
    self.Lastroll = lastroll

    pass

   def __str__(self):
    
       
       return f"Player name is: {self.Name}, and his score is: {self.Score}."
    
   def add_score(self, points):
       
       self.Score =+ points
       pass
       """
       Adding poing to score 
        """
   def resets_core(self):
       
       self.Score = 0
       pass
       """
        Sets the score to 0
       """
   def win(self):
       
       self.Wins =+ 1 
       pass
  
   def roll(self):
    '''
    Add 1 point for the player that wins 
    '''
       
       r_dice = randint (1,6)
       self.Lastroll = r_dice 
       pass
    '''
    The function that rolls the dice and saves it in Lastroll
    '''
def roll_dice(obj1):
    
    #obj1 = exampleplayer1
    #exampleplayer1.roll()
    obj1.roll()
    #obj2.roll()
    pass


def main():
    
    #Task 2

    # exampleplayer1 = Player("Ahmad") # Fyll i Player
    # exampleplayer2 = Player("Maurits")
    # roll_dice(exampleplayer1, exampleplayer2)
    # exampleplayer1.add_score(exampleplayer1.Lastroll)
    # exampleplayer2.add_score(exampleplayer2.Lastroll)

    # if exampleplayer1.Score > exampleplayer2.Score:
    #     exampleplayer1.win()
    # elif exampleplayer2.Score > exampleplayer1.Score:
    #     exampleplayer2.win()
    # else:
    #     print("Tie")

    # print(exampleplayer1.__str__(), " wins: ",exampleplayer1.Wins)
    # print(exampleplayer2.__str__(), " wins: ", exampleplayer2.Wins)

    #Task 3

    players = int(input("How many players should play?: "))

    all_players_scores = []
    for number in range(players):
        current_player = Player(input("Enter the name of the player: "))
        roll_dice(current_player) 
        current_player.add_score(current_player.Lastroll) 
        roll_dice(current_player) 
        current_player.add_score(current_player.Lastroll)
        all_players_scores.append(current_player)

    all_players_scores.sort(key=lambda x: x.Score, reverse=True)

    place = 1
    for plyr in all_players_scores[:3]:
        print(f"{plyr.Name} came in place: {place}, with a score of: {plyr.Score}")
        place +=1 
if __name__ == "__main__":
    main()