from game.player_score import PlayerScore
from game.intelligence import Intelligence
import io
import unittest
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')


class TestIntelligence(unittest.TestCase):

    def setUp(self):
        game_level = 'e'
        self.int_obj = Intelligence(game_level)

    def test_set_hard_level_equal(self):
        start_dice_pos, end_dice_pos, turns = self.int_obj.set_hard_level()
        self.assertEqual(start_dice_pos, 2)
        self.assertEqual(end_dice_pos, 5)
        self.assertEqual(turns, 5)

    def test_set_hard_level_not_equal(self):
        start_dice_pos, end_dice_pos, turns = self.int_obj.set_hard_level()
        self.assertNotEqual(start_dice_pos, 0)
        self.assertNotEqual(end_dice_pos, 7)
        self.assertNotEqual(turns, 2)

    def test_set_medium_level_equal(self):
        start_dice_pos, end_dice_pos, turns = self.int_obj.set_medium_level()
        self.assertEqual(start_dice_pos, 1)
        self.assertEqual(end_dice_pos, 5)
        self.assertEqual(turns, 4)

    def test_set_medium_level_not_equal(self):
        start_dice_pos, end_dice_pos, turns = self.int_obj.set_medium_level()
        self.assertNotEqual(start_dice_pos, 0)
        self.assertNotEqual(end_dice_pos, 7)
        self.assertNotEqual(turns, 2)

    def test_set_easy_level_equal(self):
        start_dice_pos, end_dice_pos, turns = self.int_obj.set_easy_level()
        self.assertEqual(start_dice_pos, 1)
        self.assertEqual(end_dice_pos, 6)
        self.assertEqual(turns, 3)

    def test_set_easy_level_notequal(self):
        start_dice_pos, end_dice_pos, turns = self.int_obj.set_easy_level()
        self.assertNotEqual(start_dice_pos, 0)
        self.assertNotEqual(end_dice_pos, 7)
        self.assertNotEqual(turns, 2)

    def test_computer_intelligence_player1_y(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        player_name = 'computer'
        player_score_obj = PlayerScore(player_name)

        self.int_obj.computer_intelligence(player_score_obj)
        result = player_score_obj.get_player_score()
        self.assertIn(result[player_name], [0, 1, 2, 3, 4, 5, 6])

    def test_computer_intelligence_player1_n(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        player_name = 'computer'
        player_score_obj = PlayerScore(player_name)

        self.int_obj.computer_intelligence(player_score_obj)
        result = player_score_obj.get_player_score()
        self.assertNotIn(result[player_name], [-1, -2, -3, -4])

    def test_computer_intelligence_player2_y(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        player_name = 'Muaz'
        player_score_obj = PlayerScore(player_name)

        self.int_obj.computer_intelligence(player_score_obj)
        result = player_score_obj.get_player_score()
        self.assertIn(result[player_name], [0, 1, 2, 3, 4, 5, 6])

    def test_computer_intelligence_player2_n(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        player_name = 'Muaz'
        player_score_obj = PlayerScore(player_name)

        self.int_obj.computer_intelligence(player_score_obj)
        result = player_score_obj.get_player_score()
        self.assertNotIn(result[player_name], [-1, -2, -3, -4])
