import random

class ComputerPerson:
    """
    Computer player that will play against the user.
    """
    
    def __init__(self, name, current_score=0):
        """
        Computer player will roll die, and automatically select to roll again or hold for each turn. They will display their turn totals after each turn.
        """
        self.name = name
        self.current_score = current_score

    def current_score(game, turn_total):
        """
        Keep track of the player's total score by adding all the turn_total values as the game progresses
        """
        pass

    def choose():
        """
        Returns value of hold or roll depending on random choice.
        """
        choices = ['HOLD', 'ROLL']
        return random.choice(choices)


class PersonPerson:
    """
    Human player that will play against computer. They will choose by user input each turn to roll, or hold. Score totals will display after each turn. 
    """

    def __init__(self, name, current_score=0):
        self.name = name
        self.current_score = current_score
    
    def current_score(game, turn_total):
        """
        Keep track of the player's total score by adding all the turn_total values as the game progresses
        """
        pass

    def choose():
        """
        Returns value of hold or roll depending on user input.
        """
        pass

class Game:
    """
    Controls the flow of the game: keeps track of scores, who's turn it is, who wins, and if you want to play again. The goal is to reach 100 points.
    """

    def __init__(self, choose, current_winner):
        self.current_player = None
        self.current_winner = None
        self.choose = None

    def roll_die():
        """
        Roll dice for random result range 1-6. Return the number.
        """
        return random.randint(1,6)

    def begin_game(self):
        """
        Allow PersonPerson and CompterPerson to roll die. The largest number gets to go first and roll!
        """
        pass

    def turn_total(dice_roll):
        """
        For each turn the player will roll dice. If they don't roll a 1 they will add all the numbers for a turn_total. Otherwise add 0 to the turn_total
        """
        pass

if __name__ == "__main__":
    pass