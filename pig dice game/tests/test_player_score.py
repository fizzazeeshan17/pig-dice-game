from game.player_score import PlayerScore
import unittest
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')


class TestPlayerScore(unittest.TestCase):

    def setUp(self):
        player_name = 'Muaz Khan'
        self.player_score_obj = PlayerScore(player_name)

    def test_set_player_score_1_equal(self):

        turn_score = 30
        player_name = 'Muaz Khan'
        self.player_score_obj.set_player_score(turn_score, player_name)
        self.assertEqual(self.player_score_obj.get_player_score()[player_name], turn_score)

    def test_set_player_score_1_notequal(self):

        turn_score = 30
        player_name = 'Muaz Khan'
        self.player_score_obj.set_player_score(turn_score, player_name)
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], 0)
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], -10)

    def test_set_player_score_2_equal(self):

        turn_score = 60
        player_name = 'computer'
        self.player_score_obj.set_player_score(turn_score, player_name)
        self.assertEqual(self.player_score_obj.get_player_score()[player_name], turn_score)

    def test_set_player_score_2_notequal(self):

        turn_score = 60
        player_name = 'computer'
        self.player_score_obj.set_player_score(turn_score, player_name)
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], 0)
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], -10)

    def test_get_player_score_player1_equal(self):

        player_name = 'Muaz Khan'
        self.assertEqual(self.player_score_obj.get_player_score()[player_name], 0)

    def test_get_player_score_player1_notequal(self):

        player_name = 'Muaz Khan'
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], 10)
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], 20)

    def test_get_player_score_player2_error1(self):

        player_name = 'Muaz'
        res = self.player_score_obj.get_player_score()
        self.assertRaises(KeyError, lambda: res[player_name])

    def test_get_player_score_player3_error2(self):

        player_name = 'Michael'
        res = self.player_score_obj.get_player_score()
        self.assertRaises(KeyError, lambda: res[player_name])

    def test_get_player_score_computer_equal(self):

        player_name = 'computer'
        self.assertEqual(self.player_score_obj.get_player_score()[player_name], 0)

    def test_get_player_score_computer_notequal(self):

        player_name = 'computer'
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], 10)
        self.assertNotEqual(self.player_score_obj.get_player_score()[player_name], 20)
