from game.turn_score import TurnScore
from game.player_score import PlayerScore
import io
import unittest
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')


class TestTurnScore(unittest.TestCase):

    def setUp(self):
        player_name = 'Muaz Khan'
        player_score_obj = PlayerScore(player_name)
        self.turn_score_obj = TurnScore(player_name, player_score_obj)

    def test_check_if_crossed_100_equal(self):
        score = 50
        self.assertEqual(self.turn_score_obj.check_if_crossed_100(score), None)

        score = 102
        self.assertEqual(self.turn_score_obj.check_if_crossed_100(score), 'game_over')

    def test_check_if_crossed_100_notequal(self):
        score = 50
        self.assertNotEqual(self.turn_score_obj.check_if_crossed_100(score), 'game_over')
        self.assertNotEqual(self.turn_score_obj.check_if_crossed_100(score), 'gameover')

        score = 102
        self.assertNotEqual(self.turn_score_obj.check_if_crossed_100(score), None)
        self.assertNotEqual(self.turn_score_obj.check_if_crossed_100(score), 'gameover')

    def test_set_score_when_one_equal(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        dice_value = 6
        self.turn_score_obj.set_score_when_one(dice_value)
        self.assertEqual(self.turn_score_obj.get_turn_score(), 0)

    def test_set_score_when_one_notequal(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        dice_value = 6
        self.turn_score_obj.set_score_when_one(dice_value)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), -10)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), -20)

    def test_set_turn_value_equal(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        dice_value = 5
        self.turn_score_obj.set_turn_value(dice_value)
        self.assertEqual(self.turn_score_obj.get_turn_score(), dice_value)

    def test_set_turn_value_notequal_plus(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        dice_value = 5
        self.turn_score_obj.set_turn_value(dice_value)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), dice_value+5)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), dice_value+15)

    def test_set_turn_value_notequal_minus(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        dice_value = 5
        self.turn_score_obj.set_turn_value(dice_value)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), dice_value-5)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), dice_value-15)

    def test_get_turn_score_equal(self):
        self.assertEqual(self.turn_score_obj.get_turn_score(), 0)

    def test_get_turn_score_notequal_negative(self):
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), -10)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), -20)

    def test_get_turn_score_notequal_postive(self):
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), 10)
        self.assertNotEqual(self.turn_score_obj.get_turn_score(), 20)
