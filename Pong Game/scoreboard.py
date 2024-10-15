"""
Pong Game Scoreboard

This script defines a `ScoreBoard` class for keeping track of and displaying the scores
of the players in a Pong game using Python's Turtle graphics library.

Key Features:
-------------
1. **Score Tracking**:
   - The `ScoreBoard` class maintains scores for both the left and right players.
   - It provides methods to increase the scores and refresh the display.

2. **Score Display**:
   - The scores for both players are shown on the screen at predefined locations.
   - The display is refreshed every time a player's score changes.

3. **Win Condition**:
   - When either player reaches the maximum score (10 by default), a win message is displayed
     at the center of the screen.
   - The game ends when one player reaches the predefined `MAX_SCORE`.

Constants:
----------
- **RIGHT_SCORE_LOC** and **LEFT_SCORE_LOC**: Predefined positions for displaying the right and left players' scores.
- **SCORE_FONT**: The font style used for displaying the scores.
- **WIN_FONT**: The font style used for displaying the "Game Over" and winning player message.
- **MAX_SCORE**: The number of points a player needs to win the game (default is 10).

Classes:
--------
1. **ScoreBoard**:
   - Inherits from the `Turtle` class and manages the display of player scores and win messages.
   - Contains methods for increasing player scores, refreshing the display, and checking for a winner.

Usage:
------
- The `l_increase()` and `r_increase()` methods are used to increment the left and right players' scores, respectively.
- The `win()` method checks if either player has won the game by reaching the maximum score and displays the winner.
"""

from turtle import Turtle
from ball import CENTER

# Constants
RIGHT_SCORE_LOC = (120, 200)
LEFT_SCORE_LOC = (-120, 200)
SCORE_FONT = ("Arial", 52, "normal")
WIN_FONT = ("Arial", 40, "bold")
MAX_SCORE = 10

class Scoreboard(Turtle):
    """
    A class to represent the scoreboard for a Pong game.

    Attributes:
    -----------
    r_score : int
        The score of the right player (starts at 0).
    l_score : int
        The score of the left player (starts at 0).
    """

    def __init__(self):
        """Initializes the Scoreboard with scores set to 0 and draws the initial score display."""
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.refresh_score()


    def l_increase(self):
        """Increases the left player's score by 1 and refreshes the score display."""
        self.l_score += 1
        self.refresh_score()


    def r_increase(self):
        """Increases the right player's score by 1 and refreshes the score display."""
        self.r_score += 1
        self.refresh_score()


    def refresh_score(self):
        """Clears the current score display and redraws the updated scores."""
        self.clear()
        self.goto(RIGHT_SCORE_LOC)
        self.write(arg=f"{self.r_score}", font=SCORE_FONT)
        self.goto(LEFT_SCORE_LOC)
        self.write(arg=f"{self.l_score}", font=SCORE_FONT)


    def win(self):
        """
        Checks if either player has reached the maximum score.
        If so, displays a win message and ends the game.

        Returns:
        --------
        bool
            True if a player has won, otherwise False.
        """
        if self.l_score == MAX_SCORE:
            self.goto(CENTER)
            self.color("red")
            self.write(arg=" " * 12 + f"Game Over\nLeft player is the winner", align="center", font=WIN_FONT)
        elif self.r_score == MAX_SCORE:
            self.goto(CENTER)
            self.color("blue")
            self.write(arg=" " * 12 + f"Game Over\nRight player is the winner", align="center", font=WIN_FONT)
        else:
            return False

        return True