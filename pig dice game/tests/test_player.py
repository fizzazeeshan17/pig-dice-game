from game.player import Player
from game.player_score import PlayerScore
import io
import unittest
from unittest.mock import patch
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_obj = Player(1, 6)

    def test_get_player_name1(self):
        with patch('builtins.input', return_value="Muaz Khan"):
            self.assertEqual(self.player_obj.get_player_name(), "Muaz Khan")
            self.assertNotEqual(self.player_obj.get_player_name(), "Muaz")

    def test_get_player_name2(self):
        with patch('builtins.input', return_value="computer"):
            self.assertEqual(self.player_obj.get_player_name(), "computer")
            self.assertNotEqual(self.player_obj.get_player_name(), "Muaz")

    def test_get_player_name3(self):
        with patch('builtins.input', return_value="Fizza"):
            self.assertEqual(self.player_obj.get_player_name(), "Fizza")
            self.assertNotEqual(self.player_obj.get_player_name(), "Muaz")

    def test_get_player_name4(self):
        with patch('builtins.input', return_value="Fizza Zeeshan"):
            self.assertEqual(self.player_obj.get_player_name(), "Fizza Zeeshan")
            self.assertNotEqual(self.player_obj.get_player_name(), "Muaz Khan")

    def test_get_player_name5(self):
        with patch('builtins.input', return_value="Muaz"):
            self.assertEqual(self.player_obj.get_player_name(), "Muaz")
            self.assertNotEqual(self.player_obj.get_player_name(), "Muaz Khan")

    def test_game_play_player1_In(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        key = 1
        player_name = 'Fizza'
        player_score_obj = PlayerScore(player_name)
        with patch('builtins.input', return_value="h"):
            self.player_obj.game_play(key, player_name, player_score_obj)
            result = player_score_obj.get_player_score()
            self.assertIn(result[player_name], [0, 1, 2, 3, 4, 5, 6])

    def test_game_play_player2_In(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        key = 1
        player_name = 'computer'
        player_score_obj = PlayerScore(player_name)
        with patch('builtins.input', return_value="h"):
            self.player_obj.game_play(key, player_name, player_score_obj)
            result = player_score_obj.get_player_score()
            self.assertIn(result[player_name], [0, 1, 2, 3, 4, 5, 6])

    def test_game_play_player1_NotIn(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        key = 1
        player_name = 'Muaz'
        player_score_obj = PlayerScore(player_name)
        with patch('builtins.input', return_value="h"):
            self.player_obj.game_play(key, player_name, player_score_obj)
            result = player_score_obj.get_player_score()
            self.assertNotIn(result[player_name], [-1, -2, -3])

    def test_game_play_player2_NotIn(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        key = 1
        player_name = 'Fizza'
        player_score_obj = PlayerScore(player_name)
        with patch('builtins.input', return_value="h"):
            self.player_obj.game_play(key, player_name, player_score_obj)
            result = player_score_obj.get_player_score()
            self.assertNotIn(result[player_name], [-1, -2, -3])

    def test_game_play_player3_NotIn(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        key = 1
        player_name = 'Fizza'
        player_score_obj = PlayerScore(player_name)
        with patch('builtins.input', return_value="h"):
            self.player_obj.game_play(key, player_name, player_score_obj)
            result = player_score_obj.get_player_score()
            self.assertNotIn(result[player_name], [-1, -2, -3])
