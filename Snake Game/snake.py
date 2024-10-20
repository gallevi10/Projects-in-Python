"""
Snake for Snake Game

This script defines the `Snake` class, which manages the snake's body in the Snake game.
It handles the creation, movement, extension, and reset of the snake, as well as the control of its direction.
The snake is represented as a series of turtle objects.

Classes:
    - Snake: A class to manage the snake's body, movement, and direction.

Features:
    - Creates an initial snake of three segments.
    - Moves the snake forward while following its head.
    - Extends the snake by adding a new segment at the tail.
    - Resets the snake's position and state.
    - Allows direction changes while preventing the snake from reversing onto itself.

"""


from turtle import Turtle

# Constants for snake movement and segment positioning
NEXT_PART_POSITION = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    """
    A class to manage the Snake in the Snake game.

    The `Snake` class creates a snake composed of turtle segments that can move, extend, and change direction.
    The snake cannot reverse onto itself and can be reset to its initial state.
    """

    def __init__(self):
        """
        Initializes the Snake object, creating the initial snake segments and setting the head reference.
        """
        self.snake_body = [] # list to store the segments of the snake
        self.create_snake()  # creates the initial snake body
        self.snake_head = self.snake_body[0] # references to the head of the snake

    def create_snake(self):
        """
        Creates the initial snake consisting of three segments placed horizontally.
        """
        x_cor = 0
        for i in range(3):
            self.add_part((x_cor, 0))
            x_cor -= NEXT_PART_POSITION


    def move_forward(self):
        """
        Moves the snake forward by updating the position of each segment to follow the segment ahead of it.
        """
        for rev_part in range(len(self.snake_body) - 1, 0, -1): # starts from the last segment
            new_x = self.snake_body[rev_part - 1].xcor()
            new_y = self.snake_body[rev_part - 1].ycor()
            self.snake_body[rev_part].goto(new_x, new_y) # moves the current segment to the next segment position

        self.snake_head.forward(MOVE_DISTANCE) # moves the head forward


    def add_part(self, position):
        """
        Adds a new segment to the snake at the specified position.

        Args:
            position (tuple[float, float]): The (x, y) coordinates where the new segment will be placed.
        """
        snake_part = Turtle(shape="square")
        snake_part.penup()
        snake_part.color("White")
        snake_part.goto(position)
        self.snake_body.append(snake_part)


    def extend(self):
        """
        Extends the snake by adding a new segment at the current position of the last segment.
        """
        self.add_part(self.snake_body[-1].position())


    def reset(self):
        """
        Resets the snake to its initial state by hiding all segments and recreating the snake.
        """
        for part in self.snake_body:
            part.hideturtle()
        self.snake_body.clear()
        self.__init__()

    def right(self):
        """
        Changes the direction of the snake head to the right if it is not already facing left.
        """
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        """
        Changes the direction of the snake head to up if it is not already facing down.
        """
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def left(self):
        """
        Changes the direction of the snake head to the left if it is not already facing right.
        """
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def down(self):
        """
        Changes the direction of the snake head to down if it is not already facing up.
        """
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

