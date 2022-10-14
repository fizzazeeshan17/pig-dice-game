from game.visual_repr import VisualRepresentaion
import unittest
from unittest.mock import patch
from prettytable import PrettyTable
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')


class TestVisualRepresentation(unittest.TestCase):

    def setUp(self):
        self.visual_repr_obj = VisualRepresentaion()

    @patch('builtins.print')
    def test_print_dice_1(self, mock_print):
        dice = 4
        self.visual_repr_obj.print_dice(dice)
        mock_print.assert_called_with(f'\n            +---+\n            | {dice} |\n            +---+')

    @patch('builtins.print')
    def test_print_dice_2(self, mock_print):
        dice = 1
        self.visual_repr_obj.print_dice(dice)
        mock_print.assert_called_with(f'\n            +---+\n            | {dice} |\n            +---+')

    @patch('builtins.print')
    def test_print_dice_3(self, mock_print):
        dice = 2
        self.visual_repr_obj.print_dice(dice)
        mock_print.assert_called_with(f'\n            +---+\n            | {dice} |\n            +---+')

    @patch('builtins.print')
    def test_print_dice_4(self, mock_print):
        dice = 3
        self.visual_repr_obj.print_dice(dice)
        mock_print.assert_called_with(f'\n            +---+\n            | {dice} |\n            +---+')

    @patch('builtins.print')
    def test_print_player_turn_score(self, mock_print):
        records = [
            [5, 5, 5], [3, 8, 8]
        ]
        player_name = 'Muaz'
        self.visual_repr_obj.print_player_turn_score(records, player_name)
        x = PrettyTable()
        x.field_names = ["DiceValue", "TurnScore", "TotalScore"]
        for record in records:
            x.add_row(record)
        x.align = "c"
        mock_print.assert_called_with(x.get_string(title=player_name))

    @patch('builtins.print')
    def test_display_score_after_turn1(self, mock_print):
        score = {'Muaz': 20, 'computer': 10}
        self.visual_repr_obj.display_score_after_turn(score)
        mock_print.assert_called_with('\n', '=='*50, '\n\n')

    @patch('builtins.print')
    def test_display_score_after_turn2(self, mock_print):
        score = {'Muaz': 40, 'computer': 70}
        self.visual_repr_obj.display_score_after_turn(score)
        mock_print.assert_called_with('\n', '=='*50, '\n\n')

    @patch('builtins.print')
    def test_display_score_after_game_over1(self, mock_print):

        score = {'Muaz': 20, 'computer': 10}
        self.visual_repr_obj.display_score_after_game_over(score)
        x = PrettyTable()
        x.field_names = ["PlayerName", "Score"]
        for key in score:
            x.add_row([key, score[key]])
        x.align = "c"
        mock_print.assert_called_with(x.get_string(title='FINAL SCORES'))

    @patch('builtins.print')
    def test_display_score_after_game_over2(self, mock_print):

        score = {'Muaz': 40, 'computer': 70}
        self.visual_repr_obj.display_score_after_game_over(score)
        x = PrettyTable()
        x.field_names = ["PlayerName", "Score"]
        for key in score:
            x.add_row([key, score[key]])
        x.align = "c"
        mock_print.assert_called_with(x.get_string(title='FINAL SCORES'))

    @patch('builtins.print')
    def test_game_over(self, mock_print):
        player_name = 'Muaz Khan'
        self.visual_repr_obj.game_over(player_name)
        mock_print.assert_called_with(f'GAME OVER , Hey! {player_name} won the game!')
