import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')

from game.dice import Dice
from game.turn_score import TurnScore


class Intelligence:
    def __init__(self, game_level):
        self.game_level = game_level.lower()
        self.start_dice_pos = None
        self.end_dice_pos = None
        self.turns = None

    def set_hard_level(self):
        """Returns assigned values

        Returns:
            [int]: start_dice_pos, end_dice_pos, turns
        """
        self.start_dice_pos = 2
        self.end_dice_pos = 5
        self.turns = 5
        return self.start_dice_pos, self.end_dice_pos, self.turns

    def set_medium_level(self):
        """Returns assigned values

        Returns:
            [int]: start_dice_pos, end_dice_pos, turns
        """
        self.start_dice_pos = 1
        self.end_dice_pos = 5
        self.turns = 4
        return self.start_dice_pos, self.end_dice_pos, self.turns

    def set_easy_level(self):
        """Returns assigned values

        Returns:
            [int]: start_dice_pos, end_dice_pos, turns
        """
        self.start_dice_pos = 1
        self.end_dice_pos = 6
        self.turns = 3
        return self.start_dice_pos, self.end_dice_pos, self.turns

    def computer_intelligence(self, player_score_obj):
        """Depending on the game level, start_dice_pos, end_dice_pos, turns are
            assigned turn score is calculated until turns reaches 0 and player
            score updated

        Args:
            player_score_obj ([clsobj]): player score class object to update score

        """
        score_obj = TurnScore('computer', player_score_obj)

        if self.game_level == 'e':
            self.start_dice_pos, self.end_dice_pos, self.turns = self.set_easy_level()
        elif self.game_level == 'm':
            self.start_dice_pos, self.end_dice_pos, self.turns = self.set_medium_level()
        else:
            self.start_dice_pos, self.end_dice_pos, self.turns = self.set_hard_level()

        result = None
        while self.turns:
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
            self.turns = self.turns - 1
        player_score_obj.set_player_score(score_obj.get_turn_score(), 'computer')
        if result == 'game_over':
            return result
