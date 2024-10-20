"""
Snake Game Scoreboard

This script defines the `ScoreBoard` class, which manages the score display for the Snake game.
It keeps track of the current score, difficulty level, and the highest scores for each difficulty.
The scoreboard is updated dynamically as the game progresses, and the highest scores are saved to a file.

Classes:
    - ScoreBoard: A class that inherits from Turtle and handles scoring, displaying the current score and the highest score, and updating the highest score if a new record is set.

Features:
    - Displays the current score and the highest score for the selected difficulty.
    - Draws an upper boundary line on the game screen.
    - Reads highest scores from a file and updates them if a new record is set.
    - Resets the score and updates the display when the game ends.
    - Automatically handles score refreshes and screen updates during the game.
"""


from turtle import Turtle
from menu import MENU_BUTTONS_TEXT

# Constants for scoreboard position and the upper boundary line
TOP = (0, 260)
UPPER_LINE = (-300,250)

class ScoreBoard(Turtle):
    """
    A class to manage the score display in the Snake game.

    This class handles displaying the current score, the highest score for the selected difficulty, and the difficulty level itself.
    It also reads and writes the highest scores to a file (`data.txt`).
    """

    def __init__(self, difficulty):
        """
        Initializes the ScoreBoard object, sets up the initial score and difficulty, and reads the highest scores from a file.

        Args:
            difficulty (int): The current difficulty level selected by the player.
        """
        super().__init__()
        self.score = 0 # initializes the current score
        self.difficulty = difficulty # stores the selected difficulty level

        # Read the highest scores from a file and store them in a list
        with open("data.txt", mode = "r") as d:
            scores_str = d.readlines()
            self.highest_scores = [int(score.strip()) for score in scores_str]
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.refresh_score() # displays the initial scoreboard


    def increase(self):
        """
        Increases the current score by 1 and updates the display.
        """
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        """
        Clears the current scoreboard and redraws it with the updated score, highest score, and difficulty.
        """
        self.clear()

        # draws the upper boundary line
        self.goto(UPPER_LINE)
        self.pendown()
        self.pensize(width=2)
        self.forward(600)
        self.penup()

        # displays the current score, highest score for the current difficulty, and the difficulty level
        self.goto(TOP)
        self.write(arg=f"Score: {self.score} | "
                       f"Highest score: {self.highest_scores[self.difficulty]} | "
                       f"Difficulty: {MENU_BUTTONS_TEXT[self.difficulty]}",
                       align="center", font=("Arial", 20, "normal"))


    def reset(self):
        """
        Resets the current score to 0, updates the highest score if a new record is set, and saves the new scores to a file.
        """
        # checks if the current score is higher than the recorded highest score for the current difficulty
        if self.score > self.highest_scores[self.difficulty]:
            self.highest_scores[self.difficulty] = self.score # updates the highest score for the current difficulty
            with open("data.txt", mode="w") as d:

                # writes the updated highest scores back to the file
                for score in self.highest_scores:
                    d.write(f"{score}\n")
        self.score = 0
        self.refresh_score()
