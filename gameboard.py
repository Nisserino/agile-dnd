class GameBoard:

    def create_board(self, size):
        board = [['X' for j in range(size)] for i in range(size)]
        return board

    def print_board(self, board):
        for r in board:
            print(" ".join(r))

    def add_marker(self, board, cord, marker):
        board[cord[0]][cord[1]] = marker
        return board






