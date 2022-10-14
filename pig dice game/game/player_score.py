class PlayerScore:
    def __init__(self, player_name):
        self.player_score = {
            player_name: 0,
            'computer': 0
        }

    def set_player_score(self, turn_score, player_name):
        """turnscore is added to player score

        Args:
            turn_score ([int]): score for the turn
            player_name ([str]): player name
        """
        self.player_score[player_name] += turn_score

    def get_player_score(self):
        """Returns player score

        Returns:
            [dict]: player score
        """
        return self.player_score

    def change_player_name(self,  new_player_name, player_name):
        """Update the score even if the player name got changed

        Args:
            new_player_name ([str]): new player name which got changed
            player_name ([str]): old player name
        """
        self.player_score[new_player_name] = self.player_score[player_name]
        del self.player_score[player_name]
        print(self.player_score)
