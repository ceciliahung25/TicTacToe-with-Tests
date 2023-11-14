import unittest
from logic import Board, RandomBot

class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = Board()
        board.grid = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(board.get_winner(), 'X')

    # TODO: Test other functions from logic.py!

if __name__ == '__main__':
    unittest.main()
