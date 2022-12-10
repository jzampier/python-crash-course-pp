class Forca:
    """teste"""

    def __init__(self, word):
        self.word = word
        self.wrong_letters = ['b', 'c', 'd', 'p']
        self.correct_letters = ['a', 'r', 'o']


game = Forca('Arroz')
(print(letter) for letter in game.wrong_letters)
for letter in game.wrong_letters:
    print(letter)
