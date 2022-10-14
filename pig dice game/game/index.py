import cmd
import time
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')

from game.player import Player
from game.intelligence import Intelligence
from game.player_score import PlayerScore
from game.visual_repr import VisualRepresentaion

LEVEL_MSG = """Please select the game level
                e - easy
                m - medium
                h - hard : """
WELCOME_MSG = f"Click Y|y to start first or N|n to give chance to your opponent : "
USER_MSG = '''\nClick q to quit the game |
click r to restart the game |
click c to change the name |
\nClick any key to roll the dice : '''


class PigShell(cmd.Cmd):
    intro = "Welcome to the Pig-dice game. Type 'help' or '?'' to list commands.\n"
    prompt = '(Pig) '
    flag = None

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.repr_obj = VisualRepresentaion()

        self.game = False
        self.player_name = None
        self.player_turn = 1
        self.game_level = 'E'

    def default(self, arg):
        'Default function which is called when does not understand the command'
        print('I do not understand that command. Type "help" for a list of commands.')

    def quitGame(self, score):
        """Quits from the game

        Returns:
            [boolean]: To quit
        """
        self.repr_obj.display_score_after_turn(score)
        self.repr_obj.display_score_after_game_over(score)
        return True

    def changeName(self, player_score_obj):
        """
            Changes the existing player name
        Args:
            player_score_obj (clsobj): player score object used to change the name
        """
        changed_player_name = input('Enter a new name: ')
        player_score_obj.change_player_name(changed_player_name, self.player_name)
        self.player_name = changed_player_name

    def check_the_key(self, key, player_score_obj):
        """[summary]

        Args:
            key ([str]): To act on specific function
            player_score_obj ([clsobj]): Used to get the score and change the name of player

        Returns:
            [func]: Returns to specific function
        """
        if key.lower() == 'q' or key.lower() == 'r':
            score = player_score_obj.get_player_score()
            self.quitGame(score)
            return 'break'
        elif key.lower() == 'c':
            self.changeName(player_score_obj)
            return key
        else:
            return key

    def start_the_game(self, player_score_obj):
        """Calls computer intelligence or gameplay of player depending on the turn
        returns when
        - game is over
        - user quits the game

        Args:
            player_score_obj ([clsobj]): Object of player score

        Returns:
            [type]: Return only if game is over
        """
        int_obj = Intelligence(self.game_level)

        while self.game:
            if self.player_turn % 2 == 1:
                print('\nComputers turn')
                result = int_obj.computer_intelligence(player_score_obj)
                if result == 'game_over':
                    return {'game_over': 'computer'}
                self.player_turn = self.player_turn + 1
            elif self.player_turn % 2 == 0:

                key = input(USER_MSG)
                key_ = self.check_the_key(key, player_score_obj)
                if key_ == 'break':
                    return
                result = self.player_obj.game_play(key_, self.player_name, player_score_obj)
                if result == 'game_over':
                    return {'game_over': self.player_name}
                self.player_turn = self.player_turn + 1
            self.repr_obj.display_score_after_turn(player_score_obj.get_player_score())

    def set_player_turn(self, game_start_key):
        """If game start key is n player turn would be 1 else 0

        Args:
            game_start_key ([str]): Y|N y - players wants to start first; n - computer starts first

        Returns:
            [int]: returns player turn 1 or 0
        """
        if game_start_key in ['n', 'N']:
            self.player_turn = 1
            print('First turns goes to Computer')
        else:
            self.player_turn = 2
            print(f"{self.player_name}, you're starting the game now get ready! Good luck :) ")
        return self.player_turn

    def get_game_level(self):
        """To get to know which level users wants to play
        e - easy
        m - medium
        h - hard

        Returns:
            [str]: The level of the game
        """
        level_flag = False
        while not level_flag:
            game_level = input(LEVEL_MSG)
            if game_level in ['e', 'E', 'm', 'M', 'h', 'H']:
                level_flag = True
        return game_level

    def get_game_start_key(self):
        """To get to know who is starting the game first whether the player or computer
        player = y
        computer = n

        Returns:
            [func]: To set the player turn
        """
        while not self.game:
            game_start_key = input(WELCOME_MSG)
            if game_start_key in ['n', 'N', 'y', 'Y']:
                self.game = True
        return self.set_player_turn(game_start_key)

    def display(self, score, result):
        """Function that displays accordingly once game is over

        Args:
            score ([dict]): Player score
            result ([dict]): Container the playername with gameover as key

        Returns:
            [boolean]: To end the game
        """
        self.repr_obj.display_score_after_turn(score)
        self.repr_obj.game_over(result['game_over'])
        self.repr_obj.display_score_after_game_over(score)
        return True

    def do_start(self, args):
        'To start the game,  Click command start'
        if args == 'cheat':
            start_dice = 2
            end_dice = 5
        else:
            start_dice = 1
            end_dice = 6
        self.player_obj = Player(start_dice, end_dice)
        self.repr_obj = VisualRepresentaion()

        self.game = False
        self.player_name = None
        self.player_turn = 0
        self.game_level = None

        self.player_name = self.player_obj.get_player_name()
        player_score_obj = PlayerScore(self.player_name)

        print(f"Hey! {self.player_name}, Let's play pig.")
        time.sleep(0.2)
        self.game_level = self.get_game_level()
        self.player_turn = self.get_game_start_key()
        result = self.start_the_game(player_score_obj)
        if type(result) == dict:
            score = player_score_obj.get_player_score()
            self.display(score, result)

    def do_rules(self, args):
        'Rules of the game are here'
        print('The Basic Rules of the game are as follows: ')
        print()
        print('A player shall roll a die until the player decides to hold')
        print('Be careful because if you(the player) roll a 1 or a 6')
        print('You will lose your score of that turn- meaning you will get a 0 for that turn')
        print('If you roll any other number besides a 1 or a 6')
        print("It will be added to your 'TurnScore' and your turn will continue")   
        print()
        print("Now, To roll the dice type 'start' or 'start_cheat_game' to start with cheats ")

    def do_quit(self, args):
        'Quit the game'
        return True

    def do_start_cheat_game(self, arg):
        'To play this game faster,  Type start_cheat_game'
        print('Welcome to cheat game')
        print()
        print('''Cheat game will end quicker than the usual game because
you will only get numbers between 2 and 5 ''')
        self.do_start('cheat')


if __name__ == '__main__':
    PigShell().cmdloop()
