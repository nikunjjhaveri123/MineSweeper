#!/usr/bin/python

import sys
import argparse
from Board import Board
from collections import deque
import random

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
    simulateTurn()

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
    if(len(safeCells) == 0):
        queriedCell = random.randint(0, board.d*board.d-1)

    print("Queried Cell: " + str(queriedCell))
    updateNeighbors(queriedCell)

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

    topLeftIndex = 0
    topIndex = 1
    topRightIndex = 2
    leftIndex = 3
    rightIndex = 4
    bottomLeftIndex = 5
    bottomIndex = 6
    bottomRightIndex = 7
    #topLeft, top, topRight, left, right, bottomLeft, bottom, bottomRight
    Neighbors = [-1,-1,-1,-1,-1,-1,-1,-1]

    #topLeft
    if(cellRow > 0 and cellCol > 0):
        Neighbors[topLeftIndex] = cellNum-board.d-1
    #top
    if(cellRow != 0):
        Neighbors[topIndex] = cellNum-board.d
    #topRight
    if(cellRow != 0 and cellCol < board.d-1):
        Neighbors[topRightIndex] = cellNum-board.d+1
    #left
    if(cellCol != 0):
        Neighbors[leftIndex] = cellNum-1
    #right
    if(cellCol < board.d-1):
        Neighbors[rightIndex] = cellNum+1
    #bottomLeft
    if(cellRow < board.d-1 and cellCol > 0):
        Neighbors[bottomLeftIndex] = cellNum + board.d-1
    #bottom
    if(cellRow < board.d-1):
        Neighbors[bottomIndex] = cellNum + board.d
    #bottomRight
    if(cellRow < board.d-1 and cellCol < board.d-1):
        Neighbors[bottomRightIndex] = cellNum + board.d + 1

    return Neighbors

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

if __name__ == "__main__":
    main()

# to generate a board via solver

# solver1 = Solver(4,3);
# board1 = solver.board;
# print(board1.layout)
