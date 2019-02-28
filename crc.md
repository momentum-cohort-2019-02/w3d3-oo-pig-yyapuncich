# Class Responsibility Collaborator Model
# Pig

From Wikipedia page:
    
    - Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to 'hold':

    - If the player rolls a 1, they score nothing and it becomes the next player's turn.
    If the player rolls any other number, it is added to their turn total and the player's turn continues.
    If a player chooses to "hold", their turn total is added to their score, and it becomes the 
    next player's turn.
    The first player to score 100 or more points wins.


## Classes Needed

### Game

Responsibilities:

- Keeps track of which Player is next
- Keeps track of leading Score/Player
- Clear turn_totals if Dice rolls 1 (or add 0)
- Adds successful turn_totals to player score
- Declares Winner
- Asks to play again

Attributes:

- player_totals
- turn_totals
- comp_player
- pers_player
- current_winner/goal

Collaborators:

- Game
- Player 1
- Player 2

*should there be 2 Player classes?*
### ComputerPerson

Responsibilities:

- Rolls Dice
- Holds
- Calculates turn_total

Attributes:
- name
- score
- rolls_dice

Collaborators:

- Game

### PersonPerson

Responsibilities:

- Rolls Dice
- Holds
- Calculates turn_total

Attributes:
- name
- score
- rolls_dice

Collaborators:

- Game

<!-- ### Dice

Responsibilities:

- Rolls Random Side

Attributes:

- sides

Collaborators:

- Game
- Player 1
- Player 2 -->

<!-- ### Winner

Responsibilities:

- Check score against total needed to win
- Continues game
- Ends game

Collaborators:

- Game
- Player 1
- Player 2 -->