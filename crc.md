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

- Keeps track of which Player turn it is
- Keep track of leading Score/Player
- Declare Winner
- Ask to play again

Collaborators:

- Player 1
- Player 2
- Score

### Player 1

Responsibilities:

- Rolls Dice
- Holds

Collaborators:

- Dice
- Score

### Player 2

Responsibilities:

- Rolls Dice
- Holds

Collaborators:

- Dice
- Score

### Dice

Responsibilities:

- Rolls Random Side

Collaborators:

- Player 1
- Player 2
- Score

### Score

Responsibilities:

- Keep track of turn totals
- Clear turn totals if Dice rolls 1
- Adds successful turn to player total
- Keeps track of player totals

Collaborators:

- Player 1
- Player 2
- Dice

### Winner

Responsibilities:

- Check score against total needed to win
- Continues game
- Ends game

Collaborators:

- Score
- Player 1
- Player 2