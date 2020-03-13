from __future__ import division
import csv
import math
import Solver
import ImprovedSolver


def main():

    file = open('basicAgentPerformance.csv', 'w+')

    with open('basicAgentPerformance.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Mine Density", "Average Final Score"])

        dimension = 22 #closest to dimension of HARD Minecraft board
        mineDensity = 0.01

        while mineDensity <= 0.99:

          totalFinalScores = 0

          iterations = 10

          totalMines = 0
          totalSafeMines = 0

          for trial in range(0,iterations):

            no_mines = int(math.ceil(dimension*dimension*mineDensity))

            minesSafelyFound, minesFound = Solver.initialize(dimension, no_mines)

            totalSafeMines += minesSafelyFound
            totalMines += minesFound

          averageFinalScore = totalSafeMines / totalMines

          writer.writerow([mineDensity, averageFinalScore])

          mineDensity += 0.01

    file = open('improvedAgentPerformance.csv', 'w+')

    with open('improvedAgentPerformance.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Mine Density", "Average Final Score"])

        dimension = 22 #closest to dimension of HARD Minecraft board
        mineDensity = 0.01

        while mineDensity <= 0.99:

          totalFinalScores = 0

          iterations = 10

          totalMines = 0
          totalSafeMines = 0

          for trial in range(0,iterations):

            no_mines = int(math.ceil(dimension*dimension*mineDensity))

            minesSafelyFound, minesFound = ImprovedSolver.initialize(dimension, no_mines)

            totalSafeMines += minesSafelyFound
            totalMines += minesFound

          averageFinalScore = totalSafeMines / totalMines

          writer.writerow([mineDensity, averageFinalScore])

          mineDensity += 0.01

if __name__ == "__main__":
    main()
