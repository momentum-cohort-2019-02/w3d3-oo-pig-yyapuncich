import random

class PlayerOne:
    """
    Computer player that will play against the user.
    """
    
    def __init__(self, name, current_score=0):
        """
        Computer player will roll die, and automatically select to roll again or hold for each turn. They will display their turn totals after each turn.
        """
        self.name = name
        self.current_score = current_score

class PlayerTwo:
    """
    Human player that will play against computer. They will choose by user input each turn to roll, or hold. Score totals will display after each turn. 
    """

    def __init__(self, name, current_score=0):
        self.name = name
        self.current_score = current_score

# class Game:
# """
# Controls the flow of the game: keeps track of scores, who's turn it is, who wins, and if you want to play again. The goal is to reach 100 points.
# """

#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#         self.current_player = None

#     def begin_game(self):

if __name__ == "__main__":
    pass