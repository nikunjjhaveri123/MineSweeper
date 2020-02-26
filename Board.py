import random

class Board:

  def __init__(self, d, n):

    self.d = d
    self.n = n
    self.layout = np.array(self.d, self.d)
    generateBoard()

  def generateBoard():

    mineLocations = random.sample(range(1, self.d*self.d), self.n)

    for i in mineLocations:
      column = i // self.d
      row = i % self.d

      self.layout[row][column] = -1
