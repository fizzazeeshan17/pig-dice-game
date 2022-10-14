from prettytable import PrettyTable
import time


class VisualRepresentaion:

    def print_dice(self, d):
        """Prints dice

        Args:
            d ([int]): dice value
        """
        print('\nRolling the dice ....! ')
        time.sleep(1)
        print(f'''
            +---+
            | {d} |
            +---+'''), '\n'

    def print_player_turn_score(self, records, player_name):
        """prints the table of turnscore

        Args:
            records ([list]): all the records that are printed
            player_name ([str]): player name
        """
        x = PrettyTable()
        x.field_names = ["DiceValue", "TurnScore", "TotalScore"]
        for record in records:
            x.add_row(record)
        x.align = "c"
        time.sleep(1)
        print(x.get_string(title=player_name))

    def display_score_after_turn(self, score):
        """termpgraph with the scores

        Args:
            score ([int]): player score
        """
        display_tick = "█"
        colon = ":"
        for key in score:
            print('\n', f"{key:<8}{colon:>5} ", display_tick*score[key], score[key])
        print('\n', '=='*50, '\n\n')

    def display_score_after_game_over(self, score):
        """Display table after game is over

        Args:
            score (dict): player score
        """
        x = PrettyTable()
        x.field_names = ["PlayerName", "Score"]
        for key in score:
            x.add_row([key, score[key]])
        x.align = "c"
        time.sleep(1)
        print(x.get_string(title='FINAL SCORES'))

    def game_over(self, player_name):
        """print game is over

        Args:
            player_name ([str]): playername
        """
        time.sleep(1)
        print(f'GAME OVER , Hey! {player_name} won the game!')
