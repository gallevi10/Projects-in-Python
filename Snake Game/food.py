"""
Snake Game food

This script defines the `Food` class, which generates food items for the Snake game.
The food can appear at random locations on the screen with random shapes and colors.
The food class inherits from the `Turtle` class and utilizes its functionalities for positioning and displaying the food.

Classes:
    - Food: A class to generate and manage food items for the Snake game.

Features:
    - Randomly generates a food item with a random color and shape.
    - Respawns the food at random locations on the game screen.
    - Supports different shapes (circle, triangle, square) and colors (yellow, red, purple, pink, blue, white, green).

"""

from turtle import Turtle
import random

# Constants for food shape and color options
SHAPES = ("circle", "triangle", "square")
COLORS = ("yellow", "red", "purple", "pink", "blue", "white", "green")
STRAIGHT = 90

class Food(Turtle):
    """
    A class to create and manage food for the Snake game.

    The `Food` class generates food with a random shape and color, and places it at random locations on the screen.
    The food size is reduced by 50% to fit better in the game grid.
    """

    def __init__(self):
        """
        Initializes the Food object, setting the shape, color, and location at random.
        The food is made smaller to fit the game grid better.
        """
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.respawn() # places the food at a random position upon initialization

    def respawn(self):
        """
        Respawns the food at a new random location on the screen with a new random color and shape.
        """
        random_color = random.choice(COLORS) # picks a random color for the food
        random_shape = random.choice(SHAPES) # picks a random shape for the food

        # if the shape is a triangle, set its orientation to face up
        if random_shape == "triangle":
            self.setheading(STRAIGHT)

        self.color(random_color)
        self.shape(random_shape)

        # sets the food to a random position within the screen boundaries
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 230))

