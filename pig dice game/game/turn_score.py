import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')

from game.visual_repr import VisualRepresentaion


class TurnScore:
    def __init__(self, player_name, player_score_obj):
        self.turn_score = 0
        self.list_score = []
        self.player_score_obj = player_score_obj
        self.player_name = player_name

    def check_if_crossed_100(self, player_current_score):
        """check if the score crossed 100

        Args:
            player_current_score ([int]): current score

        Returns:
            [str]: returns gameover if crossed 100
        """
        if player_current_score > 100:
            return 'game_over'

    def update_scores_list(self, dice_val, key=False):
        """Used to create records which will print using pretty table. Also helps
        in calculating current score.

        Args:
            dice_val ([int]): [description]
            key (bool, optional): If True just the playerscore is updated,
            If false player score + turnscore is updated in records third column. Defaults to False.

        """
        player_score_till_before_turn = self.player_score_obj.get_player_score()
        player_score = player_score_till_before_turn[self.player_name]
        if key == True:
            self.list_score.append([dice_val, self.turn_score, player_score])
        else:
            self.list_score.append([dice_val, self.turn_score, player_score + self.turn_score])
        result = self.check_if_crossed_100(player_score + self.turn_score)
        repr_obj = VisualRepresentaion()
        repr_obj.print_player_turn_score(self.list_score, self.player_name)
        if result == 'game_over':
            return result

    def set_score_when_one(self, dice_value):
        """Sets score when dice value is 1 or 6

        Args:
            dice_value ([int]): dice value
        """
        self.turn_score = 0
        return self.update_scores_list(dice_value, key=True)

    def set_turn_value(self, dice_value):
        """sets score when dice value is other than 1 or 6

        Args:
            dice_value ([int]): dice value
        """
        self.turn_score += dice_value
        return self.update_scores_list(dice_value)

    def get_turn_score(self):
        """returns turn score

        Returns:
            [int]: turnscore
        """
        return self.turn_score
