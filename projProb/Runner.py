from __future__ import division
import csv
import math
import ImprovedSolver
import CostSolver

#This class is used to create and run tests for the minimizing cost and risk solvers vs the basic mine sweeper solver agent from project 2.
def main():

    # file = open('basicAgentPerformance.csv', 'w+')
    #
    # #Places results for the basic solver in the basicAgentPErformance.csv file
    # with open('basicAgentPerformance.csv', 'w') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Mine Density", "Average Cost"])
    #
    #     dimension = 15 #dimension of HARD Minesweeper board
    #     mineDensity = 0.05 # starting mine density
    #
    #     while mineDensity <= 0.95: # will test mine densities up to a density of 0.9
    #
    #       iterations = 10
    #
    #       totalMines = 0
    #       totalCost = 0
    #
    #       for trial in range(0,iterations): #Run trials with each mine density 10 times
    #
    #         no_mines = int(math.ceil(dimension*dimension*mineDensity))
    #
    #         minesSafelyFound, minesFound = ImprovedSolver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results
    #
    #         #writer.writerow([mineDensity, no_mines-minesSafelyFound])
    #
    #         totalCost += no_mines-minesSafelyFound #calculate the total cost over all tests for a certain density
    #         #totalMines += minesFound #calculate the total number of mines found over all tests for a certain density
    #
    #       averageFinalCost = totalCost / iterations #caluculate average final cost
    #
    #       writer.writerow([mineDensity, averageFinalCost]) #write data entry into csv file
    #
    #       mineDensity += 0.05
    #
    # file = open('minCostAgentPerformance.csv', 'w+')

    #Places results for the minimizing cost solver in the minCostAgentPerformance.csv file
    # with open('minCostAgentPerformance.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     #writer.writerow(["Mine Density", "Average Cost"])
    #
    #     dimension = 15 #dimension of HARD Minesweeper board
    #     mineDensity = 0.45 # starting mine density
    #
    #     while mineDensity <= 0.95: # will test mine densities up to a density of 0.9
    #
    #       iterations = 10
    #
    #       totalMines = 0
    #       totalCost = 0
    #
    #       for trial in range(0,iterations): #Run trials with each mine density 10 times
    #
    #         no_mines = int(math.ceil(dimension*dimension*mineDensity))
    #
    #         minesSafelyFound, minesFound = CostSolver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results
    #
    #         #writer.writerow([mineDensity, no_mines-minesSafelyFound])
    #
    #         totalCost += no_mines-minesSafelyFound #calculate the total cost over all tests for a certain density
    #         #totalMines += minesFound #calculate the total number of mines found over all tests for a certain density
    #
    #       averageFinalCost = totalCost / iterations #caluculate average final cost
    #
    #       writer.writerow([mineDensity, averageFinalCost]) #write data entry into csv file
    #
    #       mineDensity += 0.05

    # file = open('minRiskAgentPerformance.csv', 'w+')

    #Places results for the minimizing risk solver in the minCostAgentPerformance.csv file
    with open('minRiskAgentPerformance.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["Mine Density", "Average Cost"])

        dimension = 15 #dimension of HARD Minesweeper board
        mineDensity = 0.05 # starting mine density

        while mineDensity <= 0.95: # will test mine densities up to a density of 0.9

          iterations = 10

          totalMines = 0
          totalCost = 0

          for trial in range(0,iterations): #Run trials with each mine density 10 times

            no_mines = int(math.ceil(dimension*dimension*mineDensity))

            minesSafelyFound, minesFound = RiskSolver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results

            #writer.writerow([mineDensity, no_mines-minesSafelyFound])

            totalCost += no_mines-minesSafelyFound #calculate the total cost over all tests for a certain density
            #totalMines += minesFound #calculate the total number of mines found over all tests for a certain density

          averageFinalCost = totalCost / iterations #caluculate average final cost

          writer.writerow([mineDensity, averageFinalCost]) #write data entry into csv file

          mineDensity += 0.05


if __name__ == "__main__":
    main()
