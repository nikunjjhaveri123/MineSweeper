import random

class Cell:

    def __init__(self, clue, detectedSafe, hiddenSpaces, detectedMines):
        self.clue = clue
        self.detectedSafe = detectedSafe
        self.hiddenSpaces = hiddenSpaces
        self.detectedMines = detectedMines
