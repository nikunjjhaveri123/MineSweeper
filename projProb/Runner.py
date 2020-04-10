from __future__ import division
import csv
import math
import ImprovedSolver
import CostSolver
import RiskSolver
import ImprovedProbabilitySolver
import time

#This class is used to create and run tests for the minimizing cost and risk solvers vs the basic mine sweeper solver agent from project 2.
def main():

    bonusMinCostInRisk()
    #bonusMinRiskInCost()

    # #Places results for the basic solver in the basicAgentPErformance.csv file
    # with open('basicAgentPerformance.csv', 'w') as file:
    # #with open('basicAgentRiskPerformance.csv', 'w') as file:
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
    #       totalUnknownSqCount = 0
    #
    #       for trial in range(0,iterations): #Run trials with each mine density 10 times
    #
    #         no_mines = int(math.ceil(dimension*dimension*mineDensity))
    #
    #         minesSafelyFound, unknownSqCount = ImprovedSolver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results
    #
    #         #writer.writerow([mineDensity, no_mines-minesSafelyFound])
    #
    #         totalCost += no_mines-minesSafelyFound #calculate the total cost over all tests for a certain density
    #         totalUnknownSqCount += unknownSqCount
    #         #totalMines += minesFound #calculate the total number of mines found over all tests for a certain density
    #
    #       averageFinalCost = totalCost / iterations #caluculate average final cost
    #       averageunknownSqCost = totalUnknownSqCount / iterations
    #
    #       writer.writerow([mineDensity, averageFinalCost]) #write data entry into csv file
    #       #writer.writerow([mineDensity, averageunknownSqCost]) #write data entry into csv file
    #
    #       mineDensity += 0.05

    #file = open('minCostAgentPerformance.csv', 'w+')

    # #Places results for the minimizing cost solver in the minCostAgentPerformance.csv file
    # with open('minCostAgentPerformance.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     #writer.writerow(["Mine Density", "Average Cost"])
    #
    #     dimension = 15 #dimension of HARD Minesweeper board
    #     mineDensity = 0.75 # starting mine density
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

    # # file = open('minRiskAgentPerformance.csv', 'w+')
    #
    # #Places results for the minimizing risk solver in the minCostAgentPerformance.csv file
    # with open('minRiskAgentPerformance.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     #writer.writerow(["Mine Density", "Average Cost"])
    #
    #     dimension = 15 #dimension of HARD Minesweeper board
    #     mineDensity = 0.3 # starting mine density
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
    #         minesSafelyFound, unknownSqCount = RiskSolver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results
    #
    #         #writer.writerow([mineDensity, no_mines-minesSafelyFound])
    #
    #         totalCost += unknownSqCount #calculate the total cost over all tests for a certain density
    #         #totalMines += minesFound #calculate the total number of mines found over all tests for a certain density
    #
    #       averageFinalCost = totalCost / iterations #caluculate average final cost
    #
    #       writer.writerow([mineDensity, averageFinalCost]) #write data entry into csv file
    #
    #       mineDensity += 0.05

    # #Places results for the improved probability solver in the improvedProbAgentPerformance.csv file
    # with open('improvedProbAgentPerformance.csv', 'a') as file:
    #     writer = csv.writer(file)
    #     #writer.writerow(["Mine Density", "Average Cost"])
    #
    #     dimension = 15 #dimension of HARD Minesweeper board
    #     mineDensity = 0.55 # starting mine density
    #
    #     while mineDensity <= 0.95: # will test mine densities up to a density of 0.9
    #
    #       iterations = 5
    #
    #       totalMines = 0
    #       totalCost = 0
    #
    #       for trial in range(0,iterations): #Run trials with each mine density 10 times
    #
    #         no_mines = int(math.ceil(dimension*dimension*mineDensity))
    #
    #         minesSafelyFound, unknownSqCount = ImprovedProbabilitySolver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results
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

def bonusMinRiskInCost():
    #Places results for the minimizing cost solver in the minCostAgentPerformance.csv file
    with open('minRiskInCostPerformance.csv', 'a') as file:
        writer = csv.writer(file)
        #writer.writerow(["Mine Density", "Average Cost"])

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

def bonusMinCostInRisk():
  #Places results for the minimizing risk solver in the minCostAgentPerformance.csv file
  with open('minCostInRiskPerformance.csv', 'a') as file:
      writer = csv.writer(file)
      #writer.writerow(["Mine Density", "Average Cost"])

      dimension = 15 #dimension of HARD Minesweeper board
      mineDensity = 0.05 # starting mine density

      while mineDensity <= 0.95: # will test mine densities up to a density of 0.9

        iterations = 10

        totalMines = 0
        totalCost = 0

        for trial in range(0,iterations): #Run trials with each mine density 10 times

          no_mines = int(math.ceil(dimension*dimension*mineDensity))

          minesSafelyFound, unknownSqCount = CostSolver.initialize(dimension, no_mines) # will utilize the basic solver agent in the Solver.py class to geenrate the board and solve it and return the results

          #writer.writerow([mineDensity, no_mines-minesSafelyFound])

          totalCost += unknownSqCount #calculate the total cost over all tests for a certain density
          #totalMines += minesFound #calculate the total number of mines found over all tests for a certain density

        averageFinalCost = totalCost / iterations #caluculate average final cost

        writer.writerow([mineDensity, averageFinalCost]) #write data entry into csv file

        mineDensity += 0.05

if __name__ == "__main__":
    main()
