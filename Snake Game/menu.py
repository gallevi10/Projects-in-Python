"""
Snake Game Menu

This script implements the menu system for a Snake game using Python's Turtle library.
It provides options for the player to choose a difficulty level and to either restart or exit the game after a game-over.
The Menu class handles the visual components and button interactions.

Classes:
    - Menu: Handles the creation and display of the game's main menu, difficulty selection, and play-again options.

Features:
    - Displays a welcome message and difficulty selection buttons.
    - Launches the game with a countdown timer.
    - Displays a "Game Over" message with options to retry or exit.
    - Allows interaction via mouse clicks to select buttons.
"""

import turtle
import time

# Constants for fonts, button sizes, and positions
WELCOME_FONT = ("David", 30, "normal")
CHOICE_FONT = ("David", 24, "normal")
MENU_BUTTON_FONT = ("David", 14, "normal")
PLAY_AGAIN_BUTTON_FONT = ("David", 18, "normal")
PLAY_AGAIN_FONT = ("David", 30, "normal")
LAUNCH_FONT = ("David", 72, "normal")
WELCOME_LOC = (0, 220)
CHOICE_LOC = (0, 170)
GAME_OVER_LOC = (0, 180)
MENU_BUTTON_LENGTH = 80
MENU_BUTTON_WIDTH = 40
PLAY_AGAIN_BUTTON_LENGTH = 140
PLAY_AGAIN_BUTTON_WIDTH = 60
MENU_BUTTONS_LOC = [(-260, 110), (-150, 110), (-40, 110), (70, 110), (180, 110)]
PLAY_AGAIN_BUTTONS_LOC = ((-160, 100), (30, 100))
PLAY_AGAIN_BUTTONS_TEXT = ("Try again", "Exit")
MENU_BUTTONS_TEXT = ["Hardest", "Hard", "Normal", "Easy", "Easiest"]


class Menu(turtle.Turtle):
    """
    A class to represent the game menu.

    This class inherits from turtle.Turtle and handles creating buttons, displaying text, and responding to mouse clicks.
    It manages the difficulty selection and the play-again menu after a game over.
    """
    def __init__(self):
        """
        Initializes the Menu object by setting up the turtle properties and drawing the menu.
        """
        super().__init__()
        self.difficulty = -1 # stores the selected difficulty level (-1 means not selected)
        self.play_again_val = -1 # stores the selection after Game Over
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.create_menu() # draws the main menu


    def create_menu(self):
        """
        Displays the welcome message and difficulty selection buttons.
        """
        self.goto(WELCOME_LOC)
        self.write(arg="Welcome to my Snake game", align="center",font=WELCOME_FONT)
        self.goto(CHOICE_LOC)
        self.write(arg="Please choose a difficulty", align="center",font=CHOICE_FONT)

        # creates the buttons for difficulty levels
        for i in range(5):
            self.create_button(MENU_BUTTONS_LOC[i], MENU_BUTTONS_TEXT[i], MENU_BUTTON_LENGTH, MENU_BUTTON_WIDTH, MENU_BUTTON_FONT)

    def play_again(self):
        """
        Displays the "Game Over" message and play-again buttons (Try Again or Exit).
        """
        self.goto(GAME_OVER_LOC)
        self.write(arg="Game Over", align="center", font=("Arial", 40, "normal"))

        # creates buttons for "Try Again" and "Exit"
        for i in range(2):
            self.create_button(PLAY_AGAIN_BUTTONS_LOC[i], PLAY_AGAIN_BUTTONS_TEXT[i], PLAY_AGAIN_BUTTON_LENGTH, PLAY_AGAIN_BUTTON_WIDTH, PLAY_AGAIN_BUTTON_FONT)

    def create_button(self, location, text, length, width, font):
        """
        Draws a rectangular button at the given location with the specified text and dimensions.

        Args:
            location (tuple[float, float]): (x, y) coordinates of the button's top-left corner.
            text (str): The text to display on the button.
            length (int): The length of the button.
            width (int): The width of the button.
            font (tuple[str, int, str]): The font to use for the button text.
        """
        self.goto(location)
        self.pendown()
        for i in range(2):
            self.forward(length)
            self.left(90)
            self.forward(width)
            self.left(90)
        self.penup()
        button_center = (location[0] + length/2, location[1] + width/4)
        self.goto(button_center)
        self.write(arg=text, align="center", font=font)


    def menu_button_clicked(self,x, y):
        """
        Detects if a difficulty selection button was clicked based on the x, y coordinates of the click.

        Args:
            x (float): The x-coordinate of the mouse click.
            y (float): The y-coordinate of the mouse click.
        """
        for i in range(5):
            if (MENU_BUTTONS_LOC[i][0] < x < MENU_BUTTONS_LOC[i][0] + MENU_BUTTON_LENGTH and
                    MENU_BUTTONS_LOC[i][1] < y < MENU_BUTTONS_LOC[i][1] + MENU_BUTTON_WIDTH):
                self.difficulty = i + 1 # sets the difficulty based on the button clicked
                self.clear() # clears the screen to launch the game

    def play_again_button_clicked(self,x, y):
        """
        Detects if the "Try Again" or "Exit" button was clicked based on the x, y coordinates of the click.

        Args:
            x (float): The x-coordinate of the mouse click.
            y (float): The y-coordinate of the mouse click.
        """
        for i in range(2):
            if (PLAY_AGAIN_BUTTONS_LOC[i][0] < x < PLAY_AGAIN_BUTTONS_LOC[i][0] + PLAY_AGAIN_BUTTON_LENGTH and
                    PLAY_AGAIN_BUTTONS_LOC[i][1] < y < PLAY_AGAIN_BUTTONS_LOC[i][1] + PLAY_AGAIN_BUTTON_WIDTH):
                self.play_again_val = i
                self.clear()


    def countdown(self):
        """
        Displays a countdown from 3 to 1 and then shows "GO!" to start the game.
        """
        self.goto(0, 0)
        for i in range(3, 0, -1):
            self.write(arg=f"{i}", align="center", font=LAUNCH_FONT)
            turtle.update()
            time.sleep(1)
            self.clear()
        self.write(arg="GO!", align="center", font=LAUNCH_FONT)
        turtle.update()
        time.sleep(1)
        self.clear()

