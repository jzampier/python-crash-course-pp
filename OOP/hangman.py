"""Hangman game"""

import random

from hang_class import Forca


def generate_random_word():
    """Generates random words from a given file

    Returns:
        a random word from a given file
    """
    with open('words.txt', 'rt') as f:
        # Comment:
        word_database = f.readlines()
    return word_database[random.randint(0, len(word_database))].strip()
    # end open file


def main():
    "Main function of app"
    game = Forca(generate_random_word())
    # While game is running, show status, ask for a letter and try to guess it
    while not game.finish_game():
        game.show_game_status()
        chosen_letter = input('\nType a letter: ')
        game.guess(chosen_letter)

    if game.determine_player_won():
        print('\n Gratz! You won the game!!!!')
    else:
        print('\nGameover!!! You failed!!!')
        print('The correct word was:' + game.word)
    print('\nIt was good to play with you \n')


if __name__ == "__main__":
    main()
