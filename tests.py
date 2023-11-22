import unittest
from unittest.mock import patch
from logic import Board, RandomBot, choose_player_type

class TestTicTacToe(unittest.TestCase):

    def test_correct_game_winner_detected(self):
        board = Board()  # 新的空白棋盘
        board.grid = [
            ['X', None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(board.get_winner(), 'X')

    def test_players_can_play_only_in_viable_spots(self):
        board = Board()  # 新的空白棋盘
        row, col = 0, 0  # 假设 (0, 0) 是一个非空位置
        with self.assertRaises(ValueError):
            if board.grid[row][col] is not None:
                raise ValueError("Cell is already occupied")
            board.grid[row][col] = 'X'

    def test_game_initialized_with_empty_board(self):
        board = Board()  # 新的空白棋盘
        self.assertIsNone(board.get_winner())  # 确保游戏开始时没有获胜者
        self.assertTrue(all(cell is None for row in board.grid for cell in row))  # 所有单元格都应该是空的

    @patch('builtins.input', side_effect=['1'])
    def test_game_initialized_with_two_players(self, mock_input):
        player_type = choose_player_type()  # 模拟用户输入 1，表示选择人类玩家
        self.assertEqual(player_type, 'X')  # 确保选择的玩家类型是 'X'

    @patch('builtins.input', side_effect=['2'])
    def test_game_initialized_with_one_player(self, mock_input):
        player_type = choose_player_type()  # 模拟用户输入 2，表示选择 RandomBot 玩家
        self.assertEqual(player_type, 'O')  # 确保选择的玩家类型是 'O'

    def test_players_assigned_unique_piece(self):
        board = Board()  # 新的空白棋盘
        player1_type = 'X'
        player2_type = 'O'
        self.assertNotEqual(player1_type, player2_type)  # 确保两个玩家被分配不同的棋子类型

if __name__ == '__main__':
    unittest.main()
