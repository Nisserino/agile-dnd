import unittest


class TestGameboard(unittest.TestCase):
    def setUp(self):
        self.board = GameBoard()
        self.board1 = self.board.create_board(4)

    def test_create(self):
        self.assertEqual(self.board1, [['X' for j in range(4)] for i in range(4)])

    def test_marker(self):
        self.assertEqual(self.board.add_marker(self.board1, [1, 2], 'O'), [['X', 'X', 'X', 'X'], ['X', 'X', 'O', 'X'],
            ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X']])
