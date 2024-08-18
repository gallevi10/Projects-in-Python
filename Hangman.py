"""
Hangman Game

This is a console-based implementation of the classic Hangman game,
where the player tries to guess a secret word one letter at a time.
The player is allowed a limited number of incorrect guesses before the hangman is fully drawn,leading to a loss.
The game includes features such as colored ASCII art, customizable secret words, and user input validation.

Modules and Functions:
-----------------------
1. hangman_logo(): 
   Displays the game's logo and the maximum number of tries.

2. color_func(HANGMAN_PHOTO):
   Colors the current hangman ASCII art based on the number of incorrect guesses.

3. check_valid_input(letter_guessed, old_letters_guessed):
   Validates the player's guessed letter based on specific conditions.

4. try_update_letter_guessed(letter_guessed, old_letters_guessed):
   Updates the list of previously guessed letters if the guess is valid.

5. show_hidden_word(secret_word, old_letters_guessed):
   Displays the current state of the secret word with correctly guessed letters revealed and others as underscores.

6. check_win(secret_word, old_letters_guessed):
   Checks whether the player has successfully guessed the entire secret word.

7. print_hangman(num_of_tries):
   Returns the appropriate hangman ASCII art based on the number of incorrect guesses.

8. choose_word():
   Allows the player to choose a secret word from a file based on an index input.

9. hangman_func():
   The core function that runs the hangman game loop, managing the game’s flow, checking guesses, and determining win/loss outcomes.

10. main():
    The main entry point for the game, initializing the game and offering restart options.

Requirements:
--------------
- Python 3.x
- colorama module for colored output in the terminal

How to Play:
------------
1. Run the script.
2. Enter the file path containing the list of possible secret words.
3. Enter the index of the word you'd like to be the secret word.
4. Guess letters one by one until you either win by guessing the word or lose by exhausting the number of tries.

Author: Gal Levi
Version: 2.0

"""

def hangman_logo():
    """This function is the logo of the game.
    :return: LOGO and number of tries
    :rtype: string"""
    HANGMAN_ASCII_ART = " _    _\n| |  | |\n| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\\n| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                     __/ |                      \n                    |___/\n"
    MAX_TRIES = "Number of tries you've got: 6"
    print('Before playing this game, make sure colorama is installed.\n\n')
    print(HANGMAN_ASCII_ART, ('\n\n' + MAX_TRIES))


def color_func(HANGMAN_PHOTO):
    """This function painting the photos of the hangman
    :param HANGMAN_PHOTO: The current photo of the hangman
    :type HANGMAN_PHOTO: string
    :return: colored photo
    :rtype: string"""
    import colorama
    from colorama import init
    init()
    from colorama import Fore, Back, Style
    if HANGMAN_PHOTO == HANGMAN_PHOTOS['hang2']:
        print(Fore.BLUE + HANGMAN_PHOTO)  #Paints the photo in blue
    elif HANGMAN_PHOTO == HANGMAN_PHOTOS['hang3']:
        print(Fore.GREEN + HANGMAN_PHOTO)  #Paints the photo in green
    elif HANGMAN_PHOTO == HANGMAN_PHOTOS['hang4']:
        print(Fore.YELLOW + HANGMAN_PHOTO)  #Paints the photo in yellow
    elif HANGMAN_PHOTO == HANGMAN_PHOTOS['hang5']:
        print(Fore.CYAN + HANGMAN_PHOTO)  #Paints the photo in cyan
    elif HANGMAN_PHOTO == HANGMAN_PHOTOS['hang6']:
        print(Fore.MAGENTA + HANGMAN_PHOTO)  #Paints the photo in magenta
    elif HANGMAN_PHOTO == HANGMAN_PHOTOS['hang7']:
        print(Fore.RED + HANGMAN_PHOTO)  #Paints the photo in red
    print(Style.RESET_ALL)


def check_valid_input(letter_guessed, old_letters_guessed):
    """This function return False/True if the letter which typed meets the conditions.
    :param letter_guessed: The letter which typed in.
    :param old_letters_guessed: All letters which typed in so far.
    :type letter_guessed: string
    :return: False or True
    :rtype: bool"""
    letter_guessed_lower = letter_guessed.lower()
    letter_guessed_is_alpha = letter_guessed.isalpha()
    if (len(letter_guessed) > 1) or letter_guessed_is_alpha == False or (letter_guessed_lower in old_letters_guessed):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """This function updating true letters to old letters list.
    :param letter_guessed: The letter which typed in.
    :param old_letters_guessed: All letters which typed in so far.
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: False or True
    :rtype: bool"""
    list_old_letters_sorted = sorted(old_letters_guessed)
    old_letters_sorted_with_arrows = ' -> '.join(list_old_letters_sorted) #The old letters guessed list
    if check_valid_input(letter_guessed, old_letters_guessed) == False:
        print('\nX\nTYPING ERROR\n')
        print("List of all your letters you've entered:\n", old_letters_sorted_with_arrows, '\n')
        return False
    else:
        old_letters_guessed += [letter_guessed]
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    """This function takes the param secret_word and changed it to bottom dashes according the number of the letters.
    If the player guessed the correct letter it changes back to the letter.
    :param secret_word: The chosen secret word.
    :param old_letters_guessed: All letters which typed in so far.
    :type secret_word: string
    :type old_letters_guessed: list
    :return: bottom dashes at the length of the secret word
    :rtype: string"""
    secret_word_lower = secret_word.lower()
    secret_word_list = list(secret_word_lower)
    pre_result = ''
    for secret_letter in secret_word_list:
        if secret_letter in old_letters_guessed:
            pre_result += secret_letter
        elif secret_letter not in old_letters_guessed:
            secret_letter = '_'
            pre_result += secret_letter
    pre_result_list = list(pre_result)
    result = ' '.join(pre_result_list)
    return result


def check_win(secret_word, old_letters_guessed):
    """This function returns a boolean value.
    If old_letters_guessed contains the letters in the secret word,
    the func returns 'True' and 'False' if not.
    :param secret_word: The chosen secret word.
    :param old_letters_guessed: All letters which typed in so far.
    :type secret_word: string
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool"""
    if ' '.join(secret_word) == show_hidden_word(secret_word, old_letters_guessed):
        return True
    else:
        return False


hang1 = 'x-------x\n'
hang2 = '\n\tx-------x\n\t|\n\t|\n\t|\n\t|\n\t|\n'
hang3 = '\n\tx-------x\n\t|\t|\n\t|\t0\n\t|\n\t|\n\t|\n'
hang4 = '\n\tx-------x\n\t|\t|\n\t|\t0\n\t|\t|\n\t|\n\t|\n'
hang5 = '\n\tx-------x\n\t|\t|\n\t|\t0\n\t|      /|\\\n\t|\n\t|\n'
hang6 = '\n\tx-------x\n\t|\t|\n\t|\t0\n\t|      /|\\\n\t|      /\n\t|\n'
hang7 = '\n\tx-------x\n\t|\t|\n\t|\t0\n\t|      /|\\\n\t|      / \\\n\t|\n'
HANGMAN_PHOTOS = {'hang1': hang1, 'hang2': hang2, 'hang3': hang3, 'hang4': hang4, 'hang5': hang5, 'hang6': hang6, 'hang7': hang7}


def print_hangman(num_of_tries):
    """This function returns photo of the hangman according the mistakes of the player
    :param num_of_tries: string of number which represent hangman photo
    :type num_of_tries: string
    :return: string of the hangman photos
    :rtype: string"""
    if num_of_tries == '1':
        return HANGMAN_PHOTOS['hang2']
    elif num_of_tries == '11':
        return HANGMAN_PHOTOS['hang3']
    elif num_of_tries == '111':
        return HANGMAN_PHOTOS['hang4']
    elif num_of_tries == '1111':
        return HANGMAN_PHOTOS['hang5']
    elif num_of_tries == '11111':
        return HANGMAN_PHOTOS['hang6']
    elif num_of_tries == '111111':
        return HANGMAN_PHOTOS['hang7']
    else:
        pass


def choose_word():
    """This function returns a secret word the player choose according the index.
    :return: the secret word
    :rtype: string"""
    import os
    global secret_word
    print('\n')
    file_path = input("Enter file path: ")  #The player types in the words-file's path he's got
    while os.path.exists(file_path) == False:  #Loop which checks if what that typed in is a exist path
        print('TYPING ERROR')
        file_path = input("Enter file path: ")
    print('\n')
    index = input("Enter a number: ")  #The player enters the number of the location of the word
    while index.isnumeric() == False:  #Loop which checks if what that typed in is a number
        print('TYPING ERROR')
        index = input("Enter a number: ")
    index = int(index)
    words_file = open(file_path,"r")
    words = words_file.read()
    words_file.close()
    words_list_duplicates = words.split()
    if index <= len(words_list_duplicates):
        chosen_secret_word = words_list_duplicates[index - 1]  #One version of the secret word
    elif index > len(words_list_duplicates):
        while index > len(words_list_duplicates):
            index = index - len(words_list_duplicates)
        chosen_secret_word = words_list_duplicates[index - 1]  #Second version of the secret word
    secret_word = chosen_secret_word.lower()


def hangman_func():
    """The hangman function
    :return: none"""
    choose_word()  #With this function the player choose the secret word he needs to guess
    print("\nlet's the game begin !!!\n")
    print(HANGMAN_PHOTOS['hang1'])  #Printing the first shape of the hangman
    Bottom_dash_num = len(secret_word)
    print("_ " * (Bottom_dash_num))  #Printing Bottom dashes at the length of the secret word
    old_letters_guessed = []  #The old letters the player guessed enters to this list
    num_of_tries = ''  #This string will rise if the player will wrong
    while check_win(secret_word, old_letters_guessed) == False:  #The main game loop
        print('\n')
        letter_guessed = input('Guess a letter:').lower()
        if letter_guessed not in secret_word and check_valid_input(letter_guessed, old_letters_guessed) == True:
            print("\nIncorrect :(")
            num_of_tries += '1'
            color_func(print_hangman(num_of_tries))  #Prints colored photos of the hangman
            try_update_letter_guessed(letter_guessed, old_letters_guessed)  #Updating true letters to old letters list
            if num_of_tries == '111111':
                print(show_hidden_word(secret_word, old_letters_guessed))  #Updating bottom dashes into correct letters
                print('\nLOSE\n')
                print('The word was:', secret_word.capitalize(),'\n')
                break
        elif check_valid_input(letter_guessed, old_letters_guessed) == False:
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
        elif letter_guessed in secret_word and check_valid_input(letter_guessed, old_letters_guessed) == True:
            print("\nCorrect !!! :)\n")
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
        print(show_hidden_word(secret_word, old_letters_guessed))
        if check_win(secret_word, old_letters_guessed) == True:
            print('\nWIN\n')


def main():
    """The main game function"""
    hangman_logo()  #Logo function
    exit_or_restart = ''
    while exit_or_restart != 'exit':  #Restart or exit loop
        hangman_func()  #Hangman function
        exit_or_restart = input('To exit type: "exit", to restart the game type anything: ')  #Restart or exit option to the game


if __name__ == "__main__":
    main()
