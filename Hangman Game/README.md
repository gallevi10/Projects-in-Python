# Hangman Game

## Overview

This is an implementation of the classic Hangman game.<br>
In this game, the player tries to guess a secret word one letter at a time.<br>
The player is allowed a limited number of incorrect guesses before the hangman is fully drawn, leading to a loss.<br>
The game features colorful ASCII art, customizable secret words, and user input validation.

## Modules and Functions

### 1. `hangman_logo()`
Displays the game's logo and the maximum number of tries.

### 2. `color_func(HANGMAN_PHOTO)`
Colors the current hangman ASCII art based on the number of incorrect guesses.

### 3. `check_valid_input(letter_guessed, old_letters_guessed)`
Validates the player's guessed letter based on specific conditions.

### 4. `try_update_letter_guessed(letter_guessed, old_letters_guessed)`
Updates the list of previously guessed letters if the guess is valid.

### 5. `show_hidden_word(secret_word, old_letters_guessed)`
Displays the current state of the secret word with correctly guessed letters revealed and others as underscores.

### 6. `check_win(secret_word, old_letters_guessed)`
Checks whether the player has successfully guessed the entire secret word.

### 7. `print_hangman(num_of_tries)`
Returns the appropriate hangman ASCII art based on the number of incorrect guesses.

### 8. `choose_word()`
Allows the player to choose a secret word from a file based on an index input.

### 9. `hangman_func()`
The core function that runs the Hangman game loop, managing the game’s flow, checking guesses, and determining win/loss outcomes.

### 10. `main()`
The main entry point for the game, initializing the game and offering restart options.

## Requirements

- Python 3.x
- `colorama` module for colored output in the terminal

## How to Play

1. Run the script.
2. Enter the file path containing the list of possible secret words when prompted.
3. Enter the index of the word you'd like to be the secret word.
4. Guess letters one by one until you either win by guessing the word or lose by exhausting the number of tries.
