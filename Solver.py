from Board import Board

class Solver:

    def __init__(self, d, n):
        self.board = Board(d, n)
        drawBoard(self)

    def solve():
        a = 1
        # write method to solve minesweeper board here

    def drawBoard(self):
        print('    ');
        for i in range(0,self.board.d):
            print(i + ' ');
        print("\n\n");
        for i in range(0, self.board.d):
            print(i)
            print(' |')
            for j in range(0, self.board.d):
                c = ''
                if (self.board[i][j].shown == 0 and self.board[i][j].flagged):
                    c = ' F '
                elif (self.board[i][j].shown == 0):
                    c = ' - '
                elif (self.board[i][j].clue == -1):
                    c = ' * '
                else:
                    c = ' '+str(self.board[i][j].clue)+' '
                print(c + '|')
            print("\n")


# to generate a board via solver

# solver1 = Solver(4,3);
# board1 = solver.board;
# print(board1.layout)
