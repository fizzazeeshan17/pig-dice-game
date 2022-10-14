import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')

from game.dice import Dice
from game.turn_score import TurnScore


class Player:
    def __init__(self, start, end):
        self.player_name = None
        self.start_dice_pos = start
        self.end_dice_pos = end

    def get_player_name(self):
        """Take input player name as input from user

        Returns:
            [str]: playername
        """
        self.player_name = input('Enter your name : ')
        return self.player_name

    def game_play(self, key, player_name, player_score_obj):
        """ Until player clicks h  or until dice value is 1 or 6 turn score is calculated
             and player score updated

        Args:
            key ([str]): [description]
            player_name ([str]): [description]
            player_score_obj ([clsobj]): [description]

        """
        score_obj = TurnScore(player_name, player_score_obj)
        result = None
        while key:
            dice_obj = Dice(self.start_dice_pos, self.end_dice_pos)
            dice_value = dice_obj.get_dice_value()
            if dice_value == 1 or dice_value == 6:
                result = score_obj.set_score_when_one(dice_value)
                if result == 'game_over':
                    break
                break
            result = score_obj.set_turn_value(dice_value)
            if result == 'game_over':
                break
            user_input = input("Enter 'h' to hold the turn otherwise click any other key to continue : ")
            if user_input == 'h' or user_input == 'H':
                key = False
        player_score_obj.set_player_score(score_obj.get_turn_score(), player_name)
        if result == 'game_over':
            return result
