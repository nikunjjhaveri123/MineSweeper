#!/usr/bin/python

import sys
import argparse
from Board import Board

board = Board(0,0)

def main():
    parser = argparse.ArgumentParser(description = 'MINESWEEPER')
    parser.add_argument('-d', '--dimension', help='Dimension of the board', required = True)
    parser.add_argument('-n', '--NumberOFMines', help='Number of mines', required = True)
    args = vars(parser.parse_args())
    d = int(args['dimension'])
    n = int(args['NumberOFMines'])

    board = Board(d, n)
    drawBoard(board)

def solve():
    a = 1
    # write method to solve minesweeper board here

def drawBoard(board):
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
