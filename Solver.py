from .Board import Board

class Solver:

    def __init__(self, d, n):
        self.board = Board(d, n)

    def solve():
        # write method to solve minesweeper board here

    def drawBoard(self):
        int i, j;
        print('    ');
        for i in range(0,self.board.d):
            print(i + ' ');
        print("\n\n");
        for i in range(0, self.board.d):
            print(i)
            print(' |')
            for (j=0; j<SIDE; j++)
                c = ''
                if (self.board[i][j].shown == 0 and self.board[i][j].flagged):
                    c = ' F '
                else if (self.board[i][j].shown == 0):
                    c = ' - '
                else if (self.board[i][j].clue == -1):
                    c = ' * '
                else:
                    c = ' '+str(self.board[i][j].clue)+' '
                print(c + '|');
            print("\n");


# to generate a board via solver

# solver1 = Solver(4,3);
# board1 = solver.board;
# print(board1.layout)
