#!/usr/bin/python

import sys
import argparse
from Board import Board
from collections import deque
import random

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


def main():
    global board, safeCells, remainingCells, minesFound
    parser = argparse.ArgumentParser(description = 'MINESWEEPER')
    parser.add_argument('-d', '--dimension', help='Dimension of the board', required = True)
    parser.add_argument('-n', '--NumberOfMines', help='Number of mines', required = True)
    args = vars(parser.parse_args())
    d = int(args['dimension'])
    n = int(args['NumberOfMines'])

    board = Board(d, n)
    for i in range(0, board.d*board.d):
        remainingCells.add(i)

    drawBoard()
    solve()

#returns the coordinate of a cell given a num. E.g: 6 = (1,2)
def getCoordinates(num):
    global board, safeCells, remainingCells
    row = num // board.d
    col = num % board.d
    return row, col

def solve():
    # write method to solve minesweeper board here
    global board, safeCells, remainingCells, minesFound, minesSafelyFound
    while(minesFound < board.n):
        simulateTurn()
        print("SafeCells for this turn are: " + str(safeCells))

    print("Total number of Mines Safely Identified: " + str(minesSafelyFound))
def simulateTurn():
    global board, safeCells, remainingCells, minesFound, minesSafelyFound

    # someRC = random.choice(tuple(remainingCells))
    # remainingCells.remove(someRC)
    # print("random choice from set is: " + str(someRC))
    # if(someRC in remainingCells):
    #     print("uhhhhh, it's still in there")
    # else:
    #     print("ai we gucci boss, it's not in there")

    queriedCell  = -1
    QCells = []
    areSafe = False
    if(len(safeCells) == 0):
        queriedCell = random.randint(0, board.d*board.d-1)
    else:
        foundOne = False
        for cell in safeCells:
            print("Finding Neighboring Safes or Mines for cellNum: " + str(cell))
            QCells, areSafe = findNeighboringSafesOrMines(cell)
            print("Returned cells: " + str(QCells))
            if(len(QCells) > 0):
                #Found a neighboring cell that can be conclusively identified as safe
                foundOne = True
                break
        if(foundOne == False):
            #Could not find any cells that can conclusively be identified as safe
            #Thus, we are choosing at random from the remainingCells set
            queriedCell = random.choice(tuple(remainingCells))

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
                openCell(query, areSafe)
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
            board.layout[nRow][nCol].identifiedMines -= 1
    else:
        #not a mine
        for i in range(0, 8):
            neighbor = NeighborsList[i]
            if(neighbor == -1):
                continue
            nRow, nCol = getCoordinates(neighbor)
            board.layout[nRow][nCol].identifiedSafes -= 1
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
    global board, safeCells, remainingCells, minesFound, minesSafelyFound
    cellRow, cellCol = getCoordinates(cellNum)

    if(board.layout[cellRow][cellCol].shown == True):
        #Error catching, don't remove
        print("There may be a problem here. openCell() is being called more than once on cellNum: " + str(cellNum))
        print("ENDING OPENCELL() ABRUPTLY")
        return
    board.layout[cellRow][cellCol].shown = True
    print("We set cellNum: " + str(cellNum) + " to be true")
    if(board.layout[cellRow][cellCol].clue == -1):
        #cell is a mine
        if(safelyIdentified == True):
            minesFound += 1
            minesSafelyFound += 1
            board.layout[cellRow][cellCol].flagged = True
        else:
            minesFound += 1
    else:
        #cell is not a mines
        if(board.layout[cellRow][cellCol].clue != 0):
            #you don't need to add cells with clue = 0 to safe cells because
            #safe cells is only used to pick the next cell to query. It is never
            #useful to query on a cell whose clue is zero because when we do find
            #such a cell, we already dfs on all its neighboring zeros
            safeCells.add(cellNum)
    remainingCells.remove(cellNum)
    updateNeighbors(cellNum)

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
        print("It returned this list of cells: " + str(Neighbors))
        return Neighbors, True
    nList = getNeighborIndices(cellNum)
    print("Cells are safe? " + str(allSafes))
    for i in nList:
        if(i == -1):
            continue
        iRow, iCol = getCoordinates(cellNum)
        print("iCellNum: " + str(i) + " shown status: " + str(board.layout[iRow][iCol].shown))
        if(board.layout[iRow][iCol].shown == False):
            Neighbors.append(i)
    print("It returned this full list of cells: " + str(Neighbors))
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
            c = ''
            if (board.layout[i][j].shown == False and board.layout[i][j].flagged == True):
                c = ' F '
            elif (board.layout[i][j].shown == False):
                c = ' - '
            elif (board.layout[i][j].clue == -1):
                c = ' * '
            else:
                c = ' '+str(board.layout[i][j].clue)+' '
            x = x + c + ' | '
        print(x)
        print("\n")

# to generate a board via solver

# solver1 = Solver(4,3);
# board1 = solver.board;
# print(board1.layout)

if __name__ == "__main__":
    main()
