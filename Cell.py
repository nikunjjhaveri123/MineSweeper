import random

class Cell:

    def __init__(self, clue, identifiedSafes, hiddenSquares, identifiedMines, flagged, shown):

        #int: the total number of mines surrounding this cell
        self.clue = clue

        #int: the number of identified safe cells surrounding this cell
        self.identifiedSafes = identifiedSafes

        #the number hidden square surrounding this cell (no. of unopened  cells)
        self.hiddenSquares = hiddenSquares

        #int: number of mines identified
        self.identifiedMines = identifieddMines

        #boolean: if you flag this cell
        self.flagged = flagged

        #boolean: whether this cell has been clicked on or not (we know if it is safe or not)
        self.shown = shown
