"""Class file"""


class Forca:
    """teste"""

    def __init__(self, word):
        self.word = word
        self.wrong_letters = []
        self.correct_letters = []

    def guess(self, letter):
        """check if is the given letter belongs to the given word"""
        if letter in self.word and letter not in self.correct_letters:
            self.correct_letters.append(letter)
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
        else:
            # invalid letter
            return False
        # valid letter
        return True

    def finish_game(self):
        """sumary_line"""
        return (
            True
            if self.determine_player_won() or (len(self.wrong_letters) >= 5)
            else False
        )

    def determine_player_won(self):
        """sumary_line"""
        return True if '_' not in self.show_hidden_word() else False

    def show_hidden_word(self):
        """sumary_line"""
        status = ''
        for letter in self.word:
            if letter not in self.correct_letters:
                status += '_'
            else:
                status += letter
        return status

    def show_game_status(self):
        """sumary_line"""
        palco = ['', 'O', 'O-', 'O-|', 'O-|-', 'O-|-<']
        print('\n======= Hangman =======')
        print(palco[len(self.wrong_letters)])
        print(f'Word: {self.show_hidden_word()}')
        print('\nWrong Letters: ')
        for letter in self.wrong_letters:
            print(
                letter,
            )
        print('\nCorrect Letters: ')
        for letter in self.correct_letters:
            print(
                letter,
            )
