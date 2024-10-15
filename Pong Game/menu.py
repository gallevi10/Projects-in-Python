"""
Pong Game Menu

This script creates an interactive menu for a Pong game using Python's Turtle graphics library.
The menu allows the user to choose between different game modes (1 Player or 2 Players) and
difficulty levels (Easy, Medium, Hard).

Key Features:
-------------
1. **Menu Display**:
   - A welcome message is displayed at the top of the screen.
   - The user is prompted to select a mode (1 Player or 2 Players).
   - After the mode is selected, the user is prompted to choose a difficulty level (Easy, Medium, Hard).

2. **Buttons**:
   - The game mode and difficulty selection options are presented as buttons drawn using Turtle.
   - Button positions and sizes are defined as constants to ensure easy modification and customization.

3. **User Interaction**:
   - User clicks are detected on the buttons to set the game mode and difficulty level.
   - Once a button is clicked, the selection is stored, and the screen is cleared for the next step.

Constants:
----------
- Fonts, button sizes, and screen locations are predefined for consistent formatting and layout.
- These constants can be modified easily to adjust the look and feel of the menu.

Classes:
--------
1. **Menu**:
   - Inherits from the `Turtle` class and manages the drawing of the menu, buttons, and the handling
     of user interactions.
   - It has methods for displaying the game mode and difficulty options, drawing buttons, and detecting
     button clicks.

Usage:
------
- The user clicks on one of the mode buttons, which triggers a stored mode value.
- Afterward, the difficulty selection menu appears, and the user can select a difficulty.
- The `mode` and `difficulty` attributes store the selected values for use in starting the game.
"""

from turtle import Turtle

#Constants
WELCOME_FONT = ("David", 30, "normal")
CHOICE_FONT = ("David", 24, "normal")
MODE_BUTTON_FONT = ("David", 32, "normal")
DIFF_BUTTON_FONT = ("David", 20, "normal")
WELCOME_LOC = (0, 220)
CHOICE_LOC = (0, 170)
MODE_BUTTON_LENGTH = 200
MODE_BUTTON_WIDTH = 100
DIFF_BUTTON_LENGTH = 120
DIFF_BUTTON_WIDTH = 60
MODE_BUTTON_LOC = [(-250, 20), (50, 20)]
MODE_BUTTONS_TEXT = ["1 Player", "2 Players"]
DIFF_BUTTON_LOC = [(-220, 80), (-70, 80), (80, 80)]
DIFF_BUTTONS_TEXT = ["Easy", "Medium", "Hard"]

class Menu(Turtle):
    """
    A class to represent a graphical menu using the Turtle module for a Pong game.

    This menu allows the user to select between game modes and difficulty levels
    by interacting with on-screen buttons.

    Attributes:
    -----------
    mode : int
        The game mode selected by the user (-1 by default, 0 for '1 Player', 1 for '2 Players').
    difficulty : int
        The game difficulty selected by the user (-1 by default, 1 for 'Easy', 2 for 'Medium', 3 for 'Hard').
    """

    def __init__(self):
        """ Initializes the Menu object with default mode and difficulty settings. """
        super().__init__()
        self.mode = -1
        self.difficulty = -1
        self.penup()
        self.speed("fastest")
        self.hideturtle()


    def choose_mode(self):
        """
        Displays the mode selection menu with buttons for '1 Player' and '2 Players'.
        The buttons are drawn on the screen with associated text.
        """
        self.goto(WELCOME_LOC)
        self.write(arg="Welcome to my Pong game", align="center",font=WELCOME_FONT)
        self.goto(CHOICE_LOC)
        self.write(arg="Please choose a mode:", align="center",font=CHOICE_FONT)
        for i in range(2):
            self.create_button(MODE_BUTTON_LOC[i], MODE_BUTTONS_TEXT[i],MODE_BUTTON_LENGTH,  MODE_BUTTON_WIDTH, MODE_BUTTON_FONT)


    def choose_diff(self):
        """
        Displays the difficulty selection menu with buttons for 'Easy', 'Medium', and 'Hard'.
        The buttons are drawn on the screen with associated text.
        """
        self.goto(CHOICE_LOC)
        self.write(arg="Please choose a difficulty:", align="center",font=CHOICE_FONT)
        for i in range(3):
            self.create_button(DIFF_BUTTON_LOC[i], DIFF_BUTTONS_TEXT[i],DIFF_BUTTON_LENGTH,  DIFF_BUTTON_WIDTH, DIFF_BUTTON_FONT)


    def create_button(self, location, text, length, width, font):
        """
        Draws a button with specified parameters and writes a label inside it.

        Parameters:
        -----------
        location : tuple
            The (x, y) coordinates of the button's bottom-left corner.
        text : str
            The text to be displayed inside the button.
        length : int
            The length of the button (horizontal size).
        width : int
            The width of the button (vertical size).
        font : tuple
            The font used to display the button's text (tuple format: (font name, size, style)).
        """
        self.goto(location)
        self.pendown()
        # Creates the button structure
        for i in range(2):
            self.forward(length)
            self.left(90)
            self.forward(width)
            self.left(90)
        self.penup()
        # Writes the text in the button
        button_center = (location[0] + length/2, location[1] + width/4)
        self.goto(button_center)
        self.write(arg=text, align="center", font=font)



    def mode_button_clicked(self,x, y):
        """
        Checks if the user's click (x, y) falls inside one of the mode buttons ('1 Player' or '2 Players').
        If a mode button is clicked, the selected mode is stored, and the screen is cleared.

        Parameters:
        -----------
        x : int
          The x-coordinate of the click.
        y : int
          The y-coordinate of the click.
        """
        for i in range(2):
            if (MODE_BUTTON_LOC[i][0] < x < MODE_BUTTON_LOC[i][0] + MODE_BUTTON_LENGTH and
                    MODE_BUTTON_LOC[i][1] < y < MODE_BUTTON_LOC[i][1] + MODE_BUTTON_WIDTH):
                self.mode = i
                self.clear()


    def diff_button_clicked(self,x, y):
        """
        Checks if the user's click (x, y) falls inside one of the difficulty buttons ('Easy', 'Medium', 'Hard').
        If a difficulty button is clicked, the selected difficulty is stored, and the screen is cleared.

        Parameters:
        -----------
        x : int
            The x-coordinate of the click.
        y : int
            The y-coordinate of the click.
        """
        for i in range(3):
            if (DIFF_BUTTON_LOC[i][0] < x < DIFF_BUTTON_LOC[i][0] + DIFF_BUTTON_LENGTH and
                    DIFF_BUTTON_LOC[i][1] < y < DIFF_BUTTON_LOC[i][1] + DIFF_BUTTON_WIDTH):
                self.difficulty = i + 1
                self.clear()
