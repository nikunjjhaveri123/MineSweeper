import random
import numpy as np

class Board:

  def __init__(self, d, n):

      self.d = d
      self.n = n
      self.layout = np.zeros((self.d, self.d))

      mineLocations = random.sample(range(1, self.d*self.d), self.n)

      for i in mineLocations:
          column = i % self.d
          row = i // self.d
          self.layout[row][column] = -1

      for i in range(0, self.d):
          for j in range(0, self.d):
              adjacentMineCount = 0

              if (self.layout[i][j].clue == -1):
                  continue

              if (i > 0):
                  if (self.layout[i-1][j].clue == -1):
                      adjacentMineCount += 1

              if (i < self.d - 1):
                  if (self.layout[i+1][j].clue == -1):
                      adjacentMineCount += 1

              if (j > 0):
                  if (self.layout[i][j-1].clue == -1):
                      adjacentMineCount += 1

              if (j < self.d - 1):
                  if (self.layout[i][j+1].clue == -1):
                      adjacentMineCount += 1

              if (i > 0 and j > 0):
                  if (self.layout[i-1][j-1].clue == -1):
                      adjacentMineCount += 1

              if (i > 0 and j < self.d - 1):
                  if (self.layout[i-1][j+1].clue == -1):
                      adjacentMineCount += 1

              if (i < self.d - 1 and j > 0):
                  if (self.layout[i+1][j-1].clue == -1):
                      adjacentMineCount += 1

              if (i < self.d - 1 and j < self.d - 1):
                  if (self.layout[i+1][j+1].clue == -1):
                      adjacentMineCount += 1

              hiddenCells = 8
              if(i == 0 or j == 0)
                  hiddenCells = 3;
              self.layout[i][j] = Cell(adjacentMineCount, 0, hiddenCells, 0, 0, 0)
