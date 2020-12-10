class GameBoard:

    def __init__(self, size):
        self.board = self.create_board(size)

    def create_board(self, size):
        board = [['X' for j in range(size)] for i in range(size)]
        return board

    def print_board(self):
        for r in self.board:
            print(" ".join(r))

    def add_marker(self, cord, marker):
        self.board[cord[0]][cord[1]] = marker
