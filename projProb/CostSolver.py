#!/usr/bin/python

import sys
import argparse
from Board import Board
from collections import deque
import random
from itertools import product


###########################  CONSTANTS  ###########################
TOPLEFTINDEX = 0
TOPINDEX = 1
TOPRIGHTINDEX= 2
LEFTINDEX = 3
RIGHTINDEX = 4
BOTTOMLEFTINDEX = 5
BOTTOMINDEX = 6
BOTTOMRIGHTINDEX = 7
###########################  CONSTANTS  ###########################

board = Board(0,0)

#These sets will be comprised of ints representing the cell on the board.
#For example, the number 4 on a board of dimension size 5 would represent the
#2d array element (0,4). 6 would be (1,2)
safeCells = set()
remainingCells = set()
minesFound = 0
minesSafelyFound = 0
allEquations = list()

def main():
    global board, safeCells, remainingCells, minesFound
    parser = argparse.ArgumentParser(description = 'MINESWEEPER')
    parser.add_argument('-d', '--dimension', help='Dimension of the board', required = True)
    parser.add_argument('-n', '--NumberOfMines', help='Number of mines', required = True)
    args = vars(parser.parse_args())
    d = int(args['dimension'])
    n = int(args['NumberOfMines'])
    initialize(d, n)

def initialize(d, n):

    global board, safeCells, remainingCells, minesSafelyFound, minesFound

    minesFound = 0
    minesSafelyFound = 0

    board = Board(d, n)
    for i in range(0, board.d*board.d):
        remainingCells.add(i)

    drawBoard()
    return solve()

#returns the coordinate of a cell given a num. E.g: 6 = (1,2)
def getCoordinates(num):
    global board, safeCells, remainingCells
    row = num // board.d
    col = num % board.d
    return row, col

def solve():
    # write method to solve minesweeper board here
    global board, safeCells, remainingCells, minesFound, minesSafelyFound
    while(len(remainingCells) > 0):
        simulateTurn()


    print("Total number of Mines Safely Identified: " + str(minesSafelyFound) + " Out of: " + str(board.n))

    return minesSafelyFound, minesFound

def simulateTurn():
    global board, safeCells, remainingCells, minesFound, minesSafelyFound, allEquations

    queriedCell  = -1
    QCells = []
    areSafe = False
    if(len(safeCells) == 0):
        queriedCell = random.randint(0, board.d*board.d-1)
    else:

        foundOne = False
        for cell in safeCells:
            QCells, areSafe = findNeighboringSafesOrMines(cell)
            if(len(QCells) > 0):
                #Found a neighboring cell that can be conclusively identified as safe or a mine
                foundOne = True
                break
        if(foundOne == False):
            #Could not find any safe cells from single clues. Will not use the constraint equations to look at relationships between cells to identify mines/safe cells
            foundNewCells = SolveConstraintEquations()
            if(foundNewCells == True):
                print("FOUND STUFF USING EQUATIONS")
                return
            #Could not find any cells that can conclusively be identified as safe
            #Thus, we are choosing at random from the remainingCells set
            else:
                #queriedCell = random.choice(tuple(remainingCells))
                configList = list()
                masterConfigList = list()
                configList = determineConfigs(allEquations, configList, masterConfigList)
                queriedCell = calculateProbabliites(configList)
                print("PROBABILITIESSSS, CELL CHOSEN: " + str(queriedCell))

    if(queriedCell > -1):
        #we don't have a list of cells to query, just one
        qCellRow, qCellCol = getCoordinates(queriedCell)
        print("Queried Cell: " + str(queriedCell))
        print("Queried Cell Clue: " + str(board.layout[qCellRow][qCellCol].clue))
        if(board.layout[qCellRow][qCellCol].clue == 0):
            #DFSOnZeros takes care of opening the necessary cells
            DFSOnZeros(queriedCell)
        else:
            if(board.layout[qCellRow][qCellCol].clue == -1):
                #we opened a mine unknowingly
                openCell(queriedCell, False)
            else:
                #we opened a non  mine (second parameter could be true or false, doesn't matter)
                openCell(queriedCell, True)
    else:
        for query in QCells:
            qCellRow, qCellCol = getCoordinates(query)
            if(board.layout[qCellRow][qCellCol].shown == True):
                #We don't want to call openCell() on an already opened cell
                continue
            elif(board.layout[qCellRow][qCellCol].clue == 0):
                #We want to open all neighboring cells of a 0 clue cell and since
                #DFSOnZeros calls openCell() by itself, we don't want to call openCell()
                #more than once on the same cell
                DFSOnZeros(query)
            else:
                openCell(query, True)
    drawBoard()

#should take in the number of a cell and update all 8 of it's neighbors with the
#necessary information. In this method, the given cell should be shown (opened) already
#it only changes each NEIGHBORS'S identifiedSafes, hiddenSquares, and identifiedMines values
#WHEN YOU OPEN A CELL, YOU SHOULD RUN THIS METHOD ON THE CELL
def updateNeighbors(cellNum):
    global board, safeCells, remainingCells, minesFound, minesSafelyFound
    cellRow, cellCol = getCoordinates(cellNum)

    NeighborsList = getNeighborIndices(cellNum)

    if(board.layout[cellRow][cellCol].clue == -1):
        #mine
        for i in range(0, 8):
            neighbor = NeighborsList[i]
            if(neighbor == -1):
                continue
            nRow, nCol = getCoordinates(neighbor)
            board.layout[nRow][nCol].hiddenSquares -= 1
            board.layout[nRow][nCol].identifiedMines += 1
    else:
        #not a mine
        for i in range(0, 8):
            neighbor = NeighborsList[i]
            if(neighbor == -1):
                continue
            nRow, nCol = getCoordinates(neighbor)
            board.layout[nRow][nCol].identifiedSafes += 1
            board.layout[nRow][nCol].hiddenSquares -= 1


#takes in cellNum and returns a list of neighboring cell numbers
#if a number is -1, then it is not indexable
def getNeighborIndices(cellNum):
    global board
    cellRow, cellCol = getCoordinates(cellNum)

    #topLeft, top, topRight, left, right, bottomLeft, bottom, bottomRight
    Neighbors = [-1,-1,-1,-1,-1,-1,-1,-1]

    #topLeft
    if(cellRow > 0 and cellCol > 0):
        Neighbors[TOPLEFTINDEX] = cellNum-board.d-1
    #top
    if(cellRow != 0):
        Neighbors[TOPINDEX] = cellNum-board.d
    #topRight
    if(cellRow != 0 and cellCol < board.d-1):
        Neighbors[TOPRIGHTINDEX] = cellNum-board.d+1
    #left
    if(cellCol != 0):
        Neighbors[LEFTINDEX] = cellNum-1
    #right
    if(cellCol < board.d-1):
        Neighbors[RIGHTINDEX] = cellNum+1
    #bottomLeft
    if(cellRow < board.d-1 and cellCol > 0):
        Neighbors[BOTTOMLEFTINDEX] = cellNum + board.d-1
    #bottom
    if(cellRow < board.d-1):
        Neighbors[BOTTOMINDEX] = cellNum + board.d
    #bottomRight
    if(cellRow < board.d-1 and cellCol < board.d-1):
        Neighbors[BOTTOMRIGHTINDEX] = cellNum + board.d + 1

    return Neighbors

#This method takes in a cellNum and opens that cell and performs all necessary
# functions when opening a cell such as updating its neighbors and the safeCells
# and remainingCells sets. If the safelyIdentified parameter is True and the clue is -1,
# then it will increment minesSafelyFound, otherwise if it is False and the
# clue is a -1, then minesSafelyFound will not be incremented. safelIdentified doesn't
# matter if the cell is not a mine
def openCell(cellNum, safelyIdentified):
    global board, safeCells, remainingCells, minesFound, minesSafelyFound, allEquations
    cellRow, cellCol = getCoordinates(cellNum)

    if(board.layout[cellRow][cellCol].shown == True):
        #Error catching, don't remove
        print("There may be a problem here. openCell() is being called more than once on cellNum: " + str(cellNum))
        print("ENDING OPENCELL() ABRUPTLY")
        return
    board.layout[cellRow][cellCol].shown = True
    if(board.layout[cellRow][cellCol].clue == -1):
        #cell is a mine
        if(safelyIdentified == True):
            allEquations = removeCellFromAllEquations(cellNum, True, allEquations)
            minesFound += 1
            minesSafelyFound += 1
            board.layout[cellRow][cellCol].flagged = True
        else:
            minesFound += 1
            allEquations = removeCellFromAllEquations(cellNum, True, allEquations)
    else:
        #cell is not a mines

        if(board.layout[cellRow][cellCol].clue != 0):
            #you don't need to add cells with clue = 0 to safe cells because
            #safe cells is only used to pick the next cell to query. It is never
            #useful to query on a cell whose clue is zero because when we do find
            #such a cell, we already dfs on all its neighboring zeros
            createConstraintEquation(cellNum)
            allEquations = removeCellFromAllEquations(cellNum, False, allEquations)
            safeCells.add(cellNum)
    remainingCells.remove(cellNum)
    updateNeighbors(cellNum)
    printAllEquations()

#This method takes in a cellNum as parameter and returns a tuple: (list of cells that
#can be conclusively identified as either all safe or all mines, True for all safe and False for all mines)
#if it cannot find any such list, it returns an empty list and the other part of the tple doesn't matter
# return Value: (list of cells, True or False indicating all safe or all mines)
def findNeighboringSafesOrMines(cellNum):
    global board, safeCells, remainingCells, minesFound, minesSafelyFound
    cellRow, cellCol = getCoordinates(cellNum)
    Neighbors = []
    clue = board.layout[cellRow][cellCol].clue
    identifiedSafes = board.layout[cellRow][cellCol].identifiedSafes
    hiddenSquares = board.layout[cellRow][cellCol].hiddenSquares
    identifiedMines = board.layout[cellRow][cellCol].identifiedMines

    allSafes = False
    if(clue - identifiedMines == hiddenSquares):
        allSafes = False
    elif( (8 - clue) - identifiedSafes == hiddenSquares):
        allSafes = True
    else:
        return Neighbors, True
    nList = getNeighborIndices(cellNum)
    for i in nList:
        if(i == -1):
            continue
        iRow, iCol = getCoordinates(i)
        if(board.layout[iRow][iCol].shown == False):
            Neighbors.append(i)
    return Neighbors, allSafes

#This recursive method assumes that the input cellNum of the first call
#(the nonrecursive call) is a cell where the clue is 0
#It will open all cells, using DFS, that are connected to this cell and
#that can be identified as safe
#THE INPUT CELLNUM MUST NOT HAVE ALREADY BEEN ADDED TO SAFECELLS SET
def DFSOnZeros(cellNum):
    global board, safeCells, remainingCells, minesFound, minesSafelyFound

    cellRow, cellCol = getCoordinates(cellNum)

    if(cellNum not in remainingCells):
        #You don't want to run openCell on a cell that is already open since you
        #don't want to update your knowledge base twice ( updateNeighbors()
        #cannot be run more than once on a given cell)
        return

    #second parameter here is true since we know that we will never hit a mine in this method
    openCell(cellNum, True)

    if(board.layout[cellRow][cellCol].clue > 0):
        return  #cannot dfs on a nonzero (positive and non mine) clue

    NeighborsList = getNeighborIndices(cellNum)

    if(NeighborsList[TOPLEFTINDEX] != -1):
        DFSOnZeros(NeighborsList[TOPLEFTINDEX])
    if(NeighborsList[TOPINDEX] != -1):
        DFSOnZeros(NeighborsList[TOPINDEX])
    if(NeighborsList[TOPRIGHTINDEX] != -1):
        DFSOnZeros(NeighborsList[TOPRIGHTINDEX])
    if(NeighborsList[LEFTINDEX] != -1):
        DFSOnZeros(NeighborsList[LEFTINDEX])
    if(NeighborsList[RIGHTINDEX] != -1):
        DFSOnZeros(NeighborsList[RIGHTINDEX])
    if(NeighborsList[BOTTOMLEFTINDEX] != -1):
        DFSOnZeros(NeighborsList[BOTTOMLEFTINDEX])
    if(NeighborsList[BOTTOMINDEX] != -1):
        DFSOnZeros(NeighborsList[BOTTOMINDEX])
    if(NeighborsList[BOTTOMRIGHTINDEX] != -1):
        DFSOnZeros(NeighborsList[BOTTOMRIGHTINDEX])

#Should take in a cell Number and create a constraint equation for that cell based on its neighbors.
#The new equation will be added to the global list of all the equations.
def createConstraintEquation(cellNum):
    global board, allEquations
    row, col = getCoordinates(cellNum)
    NeighborsList = getNeighborIndices(cellNum)
    for icell in NeighborsList:
        if (icell == -1):
            continue
        iRow, iCol = getCoordinates(icell)

        # If a neighbour is already flagged, then do not add it to the equation but subtract the constraint value by 1
        if (board.layout[iRow][iCol].flagged == True):
            board.layout[iRow][iCol].constraintValue -=1
            continue

        #If neighbor is already a mine then do not add but subtract the constraint value
        if (board.layout[iRow][iCol].shown == True and board.layout[iRow][iCol].clue == -1):
            board.layout[row][col].constraintValue -=1
            continue

        # If a neighbour is already shown, then do not add it to the equation.
        if (board.layout[iRow][iCol].shown == True):
            continue
            
        board.layout[row][col].addConstraintVariable(icell)

    #Adding the newly created equation for a cell to the global list of equations
    allEquations.append([board.layout[row][col].constraintEquation, board.layout[row][col].constraintValue])

#This method will take all the equations in the global list of equations and try to solve as many as it can to find new safe cells of mines to open or flag respectively
def SolveConstraintEquations():
    global allEquations, board
    # Sort all equations in increasing order of their length
    allEquations = sorted(allEquations, key = lambda x: len(x[0]))

    #resolve the subsets of equations
    for e1 in allEquations:
        for e2 in allEquations:

            if e1 == e2 or not e1[0] or not e2[0] or not e1[1] or not e2[1]:
                continue

            # Check if the equation is a subset of the other equations
            if set(e1[0]).issubset(set(e2[0])):
                e2[0] = list(set(e2[0]) - set(e1[0]))
                e2[1] -= e1[1]
                continue

            # Check if the equation is a superset of the other equations
            if set(e2[0]).issubset(set(e1[0])):
                e1[0] = list(set(e1[0]) - set(e2[0]))
                e1[1] -= e2[1]

    # After resolving subsets, check if now we can get mine and non-mine variables
    # from the equations.
    return findNewSafeOrMines()

def findNewSafeOrMines():
    global board, allEquations
    changes = False
    for eq in allEquations:

        #If the equation is empty  or there are no more vairables remove it
        if (len(eq) == 0 or len(eq[0]) == 0):
            allEquations.remove(eq)
            continue

        #If the value for the equation is 0 all mines have been found and the rest of the neighbors are safeCells
        if eq[1] == 0:
            changes = True
            allEquations.remove(eq)
            for cells in eq[0]:
                row, col = getCoordinates(cells)
                if(board.layout[row][col].clue == 0):
                    DFSOnZeros(cells)
                else:
                    openCell(cells, True)

            continue

        #If the number of variables in the equation is equal to value then all cells in the equations are mines.
        if(len(eq[0]) == eq[1]):
            changes = True
            allEquations.remove(eq)
            for cells in eq[0]:
                openCell(cells, True)
    return changes

def SolveConstraintEquations2(currEqList):
    # Sort all equations in increasing order of their length
    currEqList = sorted(currEqList, key = lambda x: len(x[0]))

    #resolve the subsets of equations
    for e1 in currEqList:
        for e2 in currEqList:

            if e1 == e2 or not e1[0] or not e2[0] or not e1[1] or not e2[1]:
                continue

            # Check if the equation is a subset of the other equations
            if set(e1[0]).issubset(set(e2[0])):
                e2[0] = list(set(e2[0]) - set(e1[0]))
                e2[1] -= e1[1]
                continue

            # Check if the equation is a superset of the other equations
            if set(e2[0]).issubset(set(e1[0])):
                e1[0] = list(set(e1[0]) - set(e2[0]))
                e1[1] -= e2[1]

    # After resolving subsets, check if now we can get mine and non-mine variables
    # from the equations.
    return currEqList

def findNewSafeOrMines2(currEqList):
    newDiscoveredCells = list()
    changes = False
    for eq in currEqList:

        #If the equation is empty  or there are no more vairables remove it
        if (len(eq) == 0 or len(eq[0]) == 0):
            currEqList.remove(eq)
            continue

        #If the value for the equation is 0 all mines have been found and the rest of the neighbors are safeCells
        if eq[1] == 0:
            changes = True
            currEqList.remove(eq)
            for cells in eq[0]:
                newDiscoveredCells.append([cells, 0])
            continue

        #If the number of variables in the equation is equal to value then all cells in the equations are mines.
        if(len(eq[0]) == eq[1]):
            changes = True
            currEqList.remove(eq)
            for cells in eq[0]:
                newDiscoveredCells.append([cells, 1])
    return newDiscoveredCells, currEqList

def removeCellFromAllEquations(cellNum, isMine, currentEq):
    global board
    for eq in currentEq:
        if cellNum in eq[0]:
            #print("Removing cell " + str(cellNum) + " From equation: " + str(eq[0]))
            eq[0].remove(cellNum)
            if isMine:
                #print("Cell was a mine, substracting 1")
                eq[1] -=1
            if(len(eq[0]) == 0):
                currentEq.remove(eq)
    return currentEq

def determineConfigs(currEqList, currConfigList, masterConfigList):
    global allEquations, allSafes, board
    if(len(currEqList) == 0):
        # print("CONFIG LIST TO BE APPENDED TO MAIN LIST")
        # print(currConfigList)
        masterConfigList.append(currConfigList)
        return masterConfigList
    # print("THIS IS THE CURRENT EQ:")
    # print(currEqList)
    copyMineEq = deepCopyEquations(currEqList)
    # print("THIS IS DEEP COPY")
    # print(copyMineEq)
    chosenCell = copyMineEq[0][0][0]
    copyMineEq = removeCellFromAllEquations(chosenCell, True, copyMineEq)
    configMine = deepCopyConfigs(currConfigList)
    configMine.append([chosenCell, 1])
    copyMineEq = SolveConstraintEquations2(copyMineEq)
    newlyFoundCells, copyMineEq = findNewSafeOrMines2(copyMineEq)
    for values in newlyFoundCells:
        configMine.append(values)
    masterConfigList = determineConfigs(copyMineEq, configMine, masterConfigList)


    copySafeEq = deepCopyEquations(currEqList)
    chosenCell = copySafeEq[0][0][0]
    copySafeEq = removeCellFromAllEquations(chosenCell, False, copySafeEq)
    configSafe = deepCopyConfigs(currConfigList)
    configSafe.append([chosenCell, 0])
    copySafeEq = SolveConstraintEquations2(copySafeEq)
    newlyFoundCells, copySafeEq = findNewSafeOrMines2(copySafeEq)
    for values in newlyFoundCells:
        configSafe.append(values)
    masterConfigList = determineConfigs(copySafeEq, configSafe, masterConfigList)

    return masterConfigList

def calculateProbabliites(configList):
    global board, remainingCells
    allCells = {}
    foundProbableCell = False
    # print(configList)
    for config in configList:
        for cell in config:
            if cell[1] == 1:
                if cell[0] in allCells.keys():
                    allCells[cell[0]] = allCells[cell[0]] + 1
                else:
                    allCells[cell[0]] = 1
            elif cell[0] not in allCells.keys():
                 allCells[cell[0]] = 0
    totalConfig = len(configList)
    cellToPick = -1
    lowestProbability = 1;
    for cell in allCells:
        allCells[cell] = float(allCells[cell] / totalConfig)
        if allCells[cell] < lowestProbability:
            lowestProbability = allCells[cell]
            cellToPick = cell
            foundProbableCell = True

    if (lowestProbability > 0.5 or cellToPick == -1):
        print("ALL PROBS GREATER THAN 0.5")
        for i in range (0,board.d * board.d):
            if(i in remainingCells and i not in allCells):
                foundProbableCell = True
                cellToPick = i
                break

    if(foundProbableCell == False):
        print("CHOOSEING ANY REMAIING CELL")
        for cell in remainingCells:
            cellToPick = cell
            break

    return cellToPick

#Prints out all the current constraint equations for the board
def printAllEquations():
    global board, allEquations
    for csp in allEquations:
        x = ''
        for cells in csp[0]:
            row, col = getCoordinates(cells)
            x += '(' + str(row) + ',' + str(col) + '), '
        x += ' = ' + str(csp[1])
        print(x)
        print('\n')

#Creates a deep copy of tyhe master list of constraint equations
def deepCopyEquations(equationList):
    newEquationList = list()
    for eq in equationList:
        variables = list()
        for var in eq[0]:
            variables.append(var)
        newEquationList.append([variables, eq[1]])
    return newEquationList

#Creates a deep copy of a configuration of a set of cells
def deepCopyConfigs(currConfigList):
    newConfigList = list()
    for cells in currConfigList:
        newConfigList.append([cells[0], cells[1]])
    return newConfigList

def drawBoard():
    global board, safeCells, remainingCells
    print(' ')
    columns = ' '
    for i in range(0, board.d):
        columns = columns + '    ' + str(i) + ' '
    print(columns)
    for i in range(0, board.d):
        x = str(i) + ' | '
        for j in range(0, board.d):
            if j >= 10:
                c = ' '
            else:
                c = ''
            if (board.layout[i][j].flagged == True):
                c = c + ' F '
            elif (board.layout[i][j].shown == False):
                c = c + ' - '
            elif (board.layout[i][j].clue == -1):
                c = c + ' * '
            else:
                c = c + ' '+str(board.layout[i][j].clue)+' '
            x = x + c + ' | '
        print(x)
        print("\n")

# to generate a board via solver

# solver1 = Solver(4,3);
# board1 = solver.board;
# print(board1.layout)

if __name__ == "__main__":
    main()
