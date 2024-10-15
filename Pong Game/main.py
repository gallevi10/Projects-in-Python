"""
Project: Pong Game

Author: Gal Levi

Version: 1

Description:
------------
This is the main entry point for the Pong game project.
It initializes the game components, including paddles, ball, scoreboard, and game menu, and manages the game loop.

The game begins by prompting the user to choose a game mode (1 Player or 2 Players).
If the user selects the 1 Player mode, they are also asked to choose a difficulty level (Easy, Medium, or Hard) for the computer opponent.
The game uses Python's Turtle graphics for visualization.

Key Features:
-------------
1. **Game Modes**:
   - Single-player: The player competes against the computer with adjustable difficulty.
   - Two-player: Two players control separate paddles and compete against each other.

2. **Game Components**:
   - Paddles are controlled manually by player(s) or automatically by the computer.
   - The ball moves around the screen, bouncing off the walls and paddles.
   - A scoreboard keeps track of each player's points.

3. **Game Loop**:
   - The game loop continues until one player reaches the maximum score, which ends the game.

4. **Collision Detection**:
   - The ball bounces off the walls and paddles, and if a paddle misses the ball, the opposing player earns a point.

Classes Used:
-------------
- `Paddle`: Manages the movement and control of the paddles.
- `Ball`: Manages the ball's movement, speed, and bouncing behavior.
- `Scoreboard`: Displays and updates the players' scores.
- `Menu`: Displays the game menu and handles user input for game mode and difficulty selection.

How to Play:
------------
1. Choose the game mode using the on-screen buttons.
   - For 1 Player mode, select a difficulty level for the computer.
2. Use the following keys to control the paddles:
   - Left player (if applicable): 'w' to move up, 's' to move down.
   - Right player: Arrow Up to move up, Arrow Down to move down.
3. The game ends when one player reaches the maximum score.

"""


from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from menu import Menu
import time

# Constants
RIGHT_PAD_LOC = (350, 0)
LEFT_PAF_LOC = (-350, 0)
CENTER_BOTTOM_Y = -280

screen = Screen()

# Court setup
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
menu = Menu()

screen.listen()

# Waits for the user to choose the game mode
menu.choose_mode()
screen.onscreenclick(menu.mode_button_clicked)
while menu.mode == -1: # while the user still not clicked a button
    screen.update()
    time.sleep(0.1)

if menu.mode == 0: # if the user chose to play with the computer
    # Waits for the user to choose a difficulty
    menu.choose_diff()
    screen.onscreenclick(menu.diff_button_clicked)
    while menu.difficulty == -1:
        screen.update()
        time.sleep(0.1)


# Creating the broken line in the middle
curr_line_y = CENTER_BOTTOM_Y
for i in range(20):
    new_line = Turtle()
    new_line.shape("square")
    new_line.penup()
    new_line.speed("fastest")
    new_line.shapesize(stretch_wid=1, stretch_len=0.5)
    new_line.setx(10)
    new_line.sety(curr_line_y)
    curr_line_y += 30




# Initialising objects
right_paddle = Paddle(RIGHT_PAD_LOC)
left_paddle = Paddle(LEFT_PAF_LOC)
scoreboard = Scoreboard()
ball = Ball()

# Paddles control movement
if menu.mode == 1: # there is two players
  screen.onkeypress(key="w", fun=left_paddle.up)
  screen.onkeypress(key="s", fun=left_paddle.down)

screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # The player chose to play against the computer
    if menu.mode == 0:
        left_paddle.move(menu.difficulty)

    # Collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -285:
        ball.wall_bounce()

    # Collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() >= 330 or
        ball.distance(left_paddle) < 50 and ball.xcor() <= -330):
        ball.paddle_bounce()

    # The ball was missed by one of the paddles
    # Left player point
    if ball.xcor() > 390:
        scoreboard.l_increase()
        ball.respawn_ball()

    # Right player point
    if ball.xcor() < -390:
        scoreboard.r_increase()
        ball.respawn_ball()

    if scoreboard.win():
        game_is_on = False




screen.exitonclick()