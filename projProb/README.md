# MineSweeper

Authors: Nikunj Jhaveri
         Kaushal Parikh
         Miraj Patel
         Nirav Patel

This project is a representation of the game mine sweeper. Our program uses Board.py and Cell.py classes to represent the entire minesweeper board and each of the individual cells. There are two solvers associated with this project, a basic one and an improved run. Both solvers will solve the board to completion. If a mine it detonated it will only record the action and continue to solve the rest of the board. The final score of each solver is based on number of mines safely identified out of total number of mines.

To run a basic solver the user must run the Solver.py file:
EX: "python Solver.py -d [dimension] -n [number of mines]"

To run a improved solver the use the ImprovedSolver.py file:
EX: "python ImprovedSolver.py -d [dimension] -n [number of mines]"

The user can run the Runner.py file which will generate several boards for both the basic solver and the improved solver and export the results into a csv file.
