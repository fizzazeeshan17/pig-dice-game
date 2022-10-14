
from game.index import PigShell
from game.player import Player
from game.visual_repr import VisualRepresentaion
import io
import unittest
from unittest.mock import patch
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game_obj = PigShell()
        self.player_obj = Player(1, 6)
        self.repr_obj = VisualRepresentaion()

        self.game = False
        self.player_name = None
        self.player_turn = 0
        self.game_level = None

    @patch('builtins.print')
    def test_default(self, mock_print):
        self.game_obj.default('arg')
        mock_print.assert_called_with('I do not understand that command. Type "help" for a list of commands.')

    def test_set_player_turn_n(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        game_start_key = 'n'
        player_turn = self.game_obj.set_player_turn(game_start_key)
        self.assertEqual(player_turn, 1)
        self.assertNotEqual(player_turn, 2)

        game_start_key = 'N'
        player_turn = self.game_obj.set_player_turn(game_start_key)
        self.assertEqual(player_turn, 1)
        self.assertNotEqual(player_turn, 2)

    def test_set_player_turn_y(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        game_start_key = 'Y'
        player_turn = self.game_obj.set_player_turn(game_start_key)
        self.assertEqual(player_turn, 2)
        self.assertNotEqual(player_turn, 1)

        game_start_key = 'y'
        player_turn = self.game_obj.set_player_turn(game_start_key)
        self.assertEqual(player_turn, 2)
        self.assertNotEqual(player_turn, 1)

    def test_get_game_level_e(self):
        with patch('builtins.input', return_value="e"):
            game_level = self.game_obj.get_game_level()
            self.assertEqual(game_level, 'e')

        with patch('builtins.input', return_value="E"):
            game_level = self.game_obj.get_game_level()
            self.assertEqual(game_level, 'E')

    def test_get_game_level_m(self):

        with patch('builtins.input', return_value="M"):
            game_level = self.game_obj.get_game_level()
            self.assertEqual(game_level, 'M')

        with patch('builtins.input', return_value="m"):
            game_level = self.game_obj.get_game_level()
            self.assertEqual(game_level, 'm')

    def test_get_game_level_h(self):

        with patch('builtins.input', return_value="h"):
            game_level = self.game_obj.get_game_level()
            self.assertEqual(game_level, 'h')

        with patch('builtins.input', return_value="H"):
            game_level = self.game_obj.get_game_level()
            self.assertEqual(game_level, 'H')

    def test_get_game_start_key(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        with patch('builtins.input', return_value="n"):
            result = self.game_obj.get_game_start_key()
            self.assertEqual(result, 1)

    def test_display(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        score = {'computer': 30, 'Muaz': 40}
        result = {'game_over': 'Muaz'}
        res = self.game_obj.display(score, result)
        self.assertEqual(res, True)
        self.assertNotEqual(res, False)

    @patch('builtins.print')
    def test_do_rules(self, mock_print):
        self.game_obj.do_rules('args')
        mock_print.assert_called_with("Now, To roll the dice type 'start' or 'start_cheat_game' to start with cheats ")

    def test_do_quit(self):
        result = self.game_obj.do_quit('args')
        self.assertEqual(result, True)
        self.assertNotEqual(result, False)
