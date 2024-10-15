"""
Pong Game Ball

This script defines a `Ball` class for the Pong game, utilizing Python's Turtle graphics library.
The `Ball` class manages the behavior of the ball in the game, including movement, bouncing, speed adjustments, and resetting.

Key Features:
-------------
1. **Ball Movement**:
   - The ball moves across the screen, updating its position based on its current speed and direction.

2. **Bouncing**:
   - The ball bounces off the top and bottom walls by reversing its y-direction.
   - When the ball collides with a paddle, it reverses its x-direction and accelerates.

3. **Speed Control**:
   - The ball's speed increases with each paddle bounce until it reaches a predefined speed limit.
   - The ball's speed is reset when it respawns after a point is scored.

4. **Respawn**:
   - After a point is scored, the ball respawns at the center of the screen with its speed reset and its x-direction reversed.

Constants:
----------
- **CENTER**: The ball's respawn location, defined as the center of the screen (0, 0).
- **SPEED_FACTOR**: The factor by which the ball's speed increases after a paddle bounce.
- **SPEED_LIMIT**: The maximum speed the ball can reach.
- **DEFAULT_SPEED**: The starting speed of the ball.

Classes:
--------
1. **Ball**:
   - Inherits from the `Turtle` class and handles the ball's movement, bounces, speed changes, and respawn behavior.

Usage:
------
- The `move()` method updates the ball's position on the screen.
- The `wall_bounce()` method reverses the ball's y-direction when it hits the top or bottom walls.
- The `paddle_bounce()` method reverses the x-direction and increases the ball's speed when it hits a paddle.
- The `respawn_ball()` method resets the ball to the center and resets its speed.
"""

from turtle import Turtle

CENTER = (0, 0)
SPEED_FACTOR = 1.1
SPEED_LIMIT = 0.035
DEFAULT_SPEED = 0.01

class Ball(Turtle):
    """
    A class to represent the ball in the Pong game.

    Attributes:
    -----------
    x_move : int
        The ball's horizontal movement speed and direction (positive for right, negative for left).
    y_move : int
        The ball's vertical movement speed and direction (positive for up, negative for down).
    ball_speed : float
        The current speed of the ball, starting at a default value and increasing after paddle bounces.
    """

    def __init__(self):
        """Initializes the Ball object with its shape, position, and initial movement settings."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.x_move = 100
        self.y_move = 100
        self.ball_speed = 0.01


    def move(self):
        """Moves the ball by updating its position based on the current speed and direction."""
        new_x = self.xcor() + self.x_move * self.ball_speed
        new_y = self.ycor() + self.y_move * self.ball_speed
        self.goto(x=new_x, y=new_y)

    def wall_bounce(self):
        """Reverses the ball's vertical direction when it collides with the top or bottom walls."""
        self.y_move = -self.y_move

    def reverse_x(self):
        """Reverses the ball's horizontal direction."""
        self.x_move = -self.x_move

    def paddle_bounce(self):
        """
        Reverses the ball's horizontal direction when it collides with a paddle
        and increases its speed if the speed limit has not been reached.
        """
        self.reverse_x()
        if self.ball_speed < SPEED_LIMIT:
            self.ball_speed *= SPEED_FACTOR

    def reset_speed(self):
        """Resets the ball's speed to the default speed."""
        self.ball_speed = DEFAULT_SPEED

    def respawn_ball(self):
        """
        Respawns the ball at the center of the screen, resets its speed,
        and reverses its horizontal direction to keep the game fair.
        """
        self.goto(CENTER)
        self.reset_speed()
        self.reverse_x()