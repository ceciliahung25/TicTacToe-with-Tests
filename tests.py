import unittest
from logic import Board, RandomBot
from cli import choose_player_type
from unittest.mock import patch

class TestTicTacToe(unittest.TestCase):

    def test_game_initialized_with_empty_board(self):
        board = Board()
        self.assertEqual(board.grid, [[None, None, None], [None, None, None], [None, None, None]])

    def test_players_assigned_unique_piece(self):
        with patch('builtins.input', side_effect=['1']):
            player1 = choose_player_type()
        with patch('builtins.input', side_effect=['2']):
            player2 = choose_player_type()
        self.assertNotEqual(player1, player2)

    def test_after_one_player_plays_other_has_turn(self):
        board = Board()
        with patch('builtins.input', side_effect=['1']):
            player1 = choose_player_type()
        player2 = board.other_player(player1)
        self.assertNotEqual(player1, player2)

    def test_winning_end_of_games_detected(self):
        board = Board()
        # Set up a winning scenario
        board.grid = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            ['O', None, 'X'],
        ]
        self.assertEqual(board.get_winner(), 'X')

    def test_draw_games_identified(self):
        board = Board()
        # Set up a draw scenario
        board.grid = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertTrue(all(cell is not None for row in board.grid for cell in row))
        self.assertIsNone(board.get_winner())

    @patch('builtins.input', side_effect=['1'])
    def test_players_can_play_only_in_viable_spots(self, mock_input):
        board = Board()
        player = choose_player_type()
        row, col = 0, 0
        board.grid[row][col] = 'X'
        with self.assertRaises(ValueError):
            board.grid[row][col] = player

    def test_correct_game_winner_detected(self):
        board = Board()
        # Set up a winning scenario
        board.grid = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            ['O', None, 'X'],
        ]
        self.assertEqual(board.get_winner(), 'X')

if __name__ == '__main__':
    unittest.main()
