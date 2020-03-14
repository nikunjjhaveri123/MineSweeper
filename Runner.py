from __future__ import division
import csv
import math
import Solver
import ImprovedSolver

#This class is used to create and run tests for the basic mine sweeper solver agent and the improved mine sweeper solver agent.
def main():

    file = open('basicAgentPerformance.csv', 'w+')

    #Places results for the basic solver in the basicAgentPErformance.csv file
    with open('basicAgentPerformance.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Mine Density", "Average Final Score"])

        dimension = 22 #closest to dimension of HARD Minecraft board
        mineDensity = 0.01 # starting mine density

        while mineDensity <= 0.99: # will test mine densities up to a density of 0.99

          totalFinalScores = 0

          iterations = 10

          totalMines = 0
          totalSafeMines = 0

          for trial in range(0,iterations): #Run trials with each mine density 10 times

            no_mines = int(math.ceil(dimension*dimension*mineDensity))

            minesSafelyFound, minesFound = Solver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results

            totalSafeMines += minesSafelyFound #calculate the total number of mines safely found over all tests for a certain density
            totalMines += minesFound #calculate the total number of mines found over all tests for a certain density

          averageFinalScore = totalSafeMines / totalMines #caluculate average final score

          writer.writerow([mineDensity, averageFinalScore]) #write data entry into csv file

          mineDensity += 0.01

    file = open('improvedAgentPerformance.csv', 'w+')

    #Places results for the basic solver in the improvedAgentPErformance.csv file
    with open('improvedAgentPerformance.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Mine Density", "Average Final Score"])

        dimension = 22 #closest to dimension of HARD Minecraft board
        mineDensity = 0.01 # starting mine density

        while mineDensity <= 0.99: #will test mine densities up to 0.99

          totalFinalScores = 0

          iterations = 10

          totalMines = 0
          totalSafeMines = 0

          for trial in range(0,iterations): #Run trials with each mine density 10 times

            no_mines = int(math.ceil(dimension*dimension*mineDensity))

            minesSafelyFound, minesFound = ImprovedSolver.initialize(dimension, no_mines) # will utilize the improved solver agent in the ImprovedSolver.py class to geenrate the board and solve it and return the results

            totalSafeMines += minesSafelyFound #calculate the total number of mines safely found over all tests for a certain density
            totalMines += minesFound #calculate the total number of mines found over all tests for a certain density

          averageFinalScore = totalSafeMines / totalMines #caluclate the average final score

          writer.writerow([mineDensity, averageFinalScore]) #write data entry into csv file

          mineDensity += 0.01

if __name__ == "__main__":
    main()
