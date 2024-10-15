"""
Pong Game Paddle

This script defines a `Paddle` class for the Pong game using Python's Turtle graphics library.
The `Paddle` class handles the movement of the paddles in the game, allowing them to move up and down
within the boundaries of the screen.
The paddles can be controlled manually or move automatically based on a provided speed.

Key Features:
-------------
1. **Paddle Movement**:
   - Paddles can move up and down based on user input or automated movement.
   - Paddles are constrained to the boundaries of the screen to prevent them from moving off-screen.

2. **Automatic Paddle Movement**:
   - The `move()` method allows paddles to automatically move up and down at a specified speed.
   - The paddle changes direction upon reaching the top or bottom screen boundary.

3. **Manual Control**:
   - The `up()` and `down()` methods allow manual control of the paddle, moving it up or down by a fixed amount.

Classes:
--------
1. **Paddle**:
   - Inherits from the `Turtle` class and manages the movement of a paddle in the Pong game.
   - Includes methods for moving the paddle up or down and for automatically adjusting its position.

Usage:
------
- The `up()` and `down()` methods are used to manually move the paddle up or down.
- The `move()` method enables automatic movement of the paddle at a given speed.
"""

from turtle import Turtle


class Paddle(Turtle):
    """
    A class to represent a paddle in the Pong game.

    Attributes:
    -----------
    going_up : bool
        A flag to track the direction of the automatic movement (True for up, False for down).
    """

    def __init__(self, paddle_location):
        """
        Initializes the Paddle object at the given location and sets its shape and initial direction.

        Parameters:
        -----------
        paddle_location : tuple
            The (x, y) coordinates where the paddle is initially placed on the screen.
        """
        super().__init__()
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(paddle_location)
        self.going_up = True


    def up(self):
        """ Moves the paddle upward by 40 units, ensuring it stays within the screen's top boundary. """
        if self.ycor() < 220:
            self.sety(self.ycor() + 40)


    def down(self):
        """ Moves the paddle downward by 40 units, ensuring it stays within the screen's bottom boundary. """
        if self.ycor() > -220:
            self.sety(self.ycor() -40)


    def move(self, speed):
        """
        Automatically moves the paddle up and down at a given speed, bouncing off the top and bottom boundaries.

        Parameters:
        -----------
        speed : int
            The speed factor controlling how fast the paddle moves.
        """
        if self.ycor() < 220 and self.going_up:
            self.sety(self.ycor() + 5 * speed)
        else:
            self.going_up = False

        if self.ycor() > -220 and not self.going_up:
            self.sety(self.ycor() - 5 * speed)
        else:
            self.going_up = True
