"""
Project: Snake Game
Author: Gal Levi
Version: 2

This script implements the main functionality of the Snake game using the Turtle library.
It initializes the game window, handles user inputs, and manages game logic such as snake movement, food spawning, collision detection, and scoring.

Features:
    - Initializes the game window with a menu for difficulty selection.
    - Controls snake movement with keyboard inputs.
    - Detects collisions with food, walls, and the snake's body.
    - Updates the scoreboard and allows the player to restart the game after a game over.
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from menu import Menu
import time

# this function is used to disable listening for key inputs
def dont_move():
    pass

# movement enabling and disabling function
def enable_movement():
    """
    Enables the snake's movement by binding keyboard keys to the corresponding movement methods.
    """
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

def disable_movement():
    """
    Disables the snake's movement by binding keyboard keys to a no-op function.
    """
    screen.onkey(dont_move, "Up")
    screen.onkey(dont_move, "Down")
    screen.onkey(dont_move, "Left")
    screen.onkey(dont_move, "Right")


# Constants for game configuration
DIFFICULTY_FACTOR = 40
EDGE = 290
TOP_EDGE = 250
CLOSE_TO_ITSELF = 10
CLOSE_TO_FOOD = 15

# sets up the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

menu = Menu() # initializes the game menu

screen.onscreenclick(menu.menu_button_clicked) # sets up click events for menu selection
screen.listen()

# waits for the user to choose a difficulty
while menu.difficulty == -1:
    screen.update()
    time.sleep(0.2)

# sets the game speed based on chosen difficulty
difficulty = menu.difficulty / DIFFICULTY_FACTOR

snake = Snake()
food = Food()
scoreboard = ScoreBoard(menu.difficulty - 1)

enable_movement() # # enables the snake's movement controls
menu.countdown() # displays a countdown to start the game

game_is_on = True
while game_is_on: # Main game loop
    screen.update()
    time.sleep(difficulty)

    # snake movement
    snake.move_forward()

    # snake collision with food
    if snake.snake_head.distance(food) < CLOSE_TO_FOOD:
        snake.extend()
        scoreboard.increase()
        food.respawn()

    # snake collision with the wall
    if (
        snake.snake_head.xcor() >= EDGE or # collision with right wall
        snake.snake_head.xcor() <= -EDGE or # collision with left wall
        snake.snake_head.ycor() >= TOP_EDGE or # collision with top wall
        snake.snake_head.ycor() <= -EDGE # collision with bottom wall
        ):
        game_is_on = False


    # snake collision with its own body
    for part in snake.snake_body[1:]:
        if snake.snake_head.distance(part) < CLOSE_TO_ITSELF:
            game_is_on = False

    # game over handling
    if not game_is_on:
        disable_movement() # disables snake movement
        snake.reset()
        scoreboard.reset()
        menu.play_again() # presents the play again menu
        screen.onscreenclick(menu.play_again_button_clicked) # sets up click events for play again options
        while menu.play_again_val == -1: # waits for the user to select an option
            screen.update()
            time.sleep(0.2)
        if menu.play_again_val == 0: # if the user wants to play again
            game_is_on = True
            menu.countdown()
            enable_movement()

        menu.play_again_val = -1 # resets play again value for the next round

