# pig-dice-game

### Project Description

We have developed a Pig(dice game) for this project.  

**What is a Pig(dice game)?**

Pig is a simple dice game. Players take turns to roll a single die as many times as they wish, adding all roll results to a running total, but losing their gained score for the turn if they roll a 1 or a 6 in the variation we have developed. '

*Its rules are as follows:*

If the player rolls a 1 or a 6, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score more than 100 points wins.

We have a list of commands a player can choose such as 
    start
    restart
    quit
    help 
    rules 
    change_name
    start_cheat_game


### Basic of the game

We have 7 classes both for the game and tests folder. 


### Implementation

*GAME*

***dice.py***
In this class we have two functions. Some variables have been initialized such as the start and end dice position. 
Random numbers are generated in the function which is 'get_dice_value'.

***index.py***
First of all we have some print statements to choose a level. We have a documented commands list which appears if you type 'help', It shows us a list of usable commands that we can choose to proceed further.

For example: If the player types 'start'. He/she will first enter a name. A welcome message will be printed for that specific player. Then the player will select a game level after which he will choose if he wants to roll the dice first or else the computer will take the first turn.

***intelligence.py***
Here we have assigned some dice values to the variables start,end dice position and turns according to the game level chosen by the player. we have three levels for the computer to play at (easy, medium and hard). In easy mode the computer can roll numbers from 1 to 6. In medium 1 to 5 whereas in hard 2 to 5.

***player_score.py***
In this class we have handled the setting and getting of the player score, and we have found a way to retain the score even if the player changes their name.
  
***player.py***
In this class we have initialized the player name, start and end dice position. We take the input of player name. This class handles the gameplay. It allows the user to click 'h' to hold, it also checks if either of the player rolled a 1 or a 6. It handles the updating and the calculating of the score. 

***turn_score.py***
In this class we check if the player score has crossed 100 points. It also calculates the current score after every dice roll. 
The dice value and the turn score will be 0 if we get a 1 or a 6 after rolling the dice. 

***visual_repr.py***
In this class we have added some"graphics" in the game to make it seem more appealing to the player to keep his/her attention. We have then also added a table to make it more convenient for the user to know what he/she rolled, what the total score is for their turn and how much is the total after adding up Dice Value and Turn Score.
In this class we have added a tick symbol to show the score in a horizontal histogram type of way. 

*Tests*

We have 10 test cases and more than 10 assertions in each class. 


### How to Install and run the game?

A Python IDE, Command prompt, and Pretty table are required in order to run the game.

***Installing Pretty table is a must in order to properly run the game and display the visual representation.***
***The game will not work in the terminal without this.***

**How to to install Pretty table:**
 pip3 install prettytable 

**How to install coverage:**
pip3 install coverage

**How to install pdoc to generate documentation:**
pip install pdoc3

**Packages required to generate UML diagrams**
pip3 install graphviz
pip3 install pydot
pip3 install pylint

**To install the latest version of pip:**
pip install --upgrade pip

**How to install pylint as a linter:**
pip3 install pylint

**How to run the game in terminal:**
1. cd (directory path) 

2. coverage run game/index.py

**How to get coverage report:**
Coverage report -m 
The command above will show us a coverage report for all classes. 

**Unit tests for each class:**
Python -m unittest tests/(filename(class)).py 
The command above will run a unit test for one specific class mentioned in the command.. 

**How to regenerate the UML diagrams:**
1. pyreverse (location of the python repo). The output of the command will create a *.dot file.

2. dot -Tpng game.dot > game.png. This command converts the dot file to png format.
 
**Documentation regeneration:**
*For Tests:* pdoc --html /(users)/(muazk)/(Desktop)/(workspace{folder if you have any})/game/tests/

*For Game:* pdoc --html /(users)/(muazk)/(Desktop)/(workspace{folder if you have any})/game/game/

(Basically your path to the game)


### Visual Representation

Score table and Dice:

We have used a package called 'Pretty Table' to display the high score table, dice and the tick symbol ( "█").

Pretty table is a command-line tool that draws basic graphs, tables and symbols in the terminal, written in Python.

This is an example of actual game data.

Rolling the dice ....!

  +---+
  | 3 |
  +---+
+------------------------------------+
|              computer              |
+-----------+-----------+------------+
| DiceValue | TurnScore | TotalScore |
+-----------+-----------+------------+
|     5     |     5     |     45     |
|     5     |     10    |     50     |
|     5     |     15    |     55     |
|     4     |     19    |     59     |
|     3     |     22    |     62     |
+-----------+-----------+------------+


Fizza   : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 43
Computer: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 62

+--------------------+
|    FINAL SCORES    |
+------------+-------+
| PlayerName | Score |
+------------+-------+
|    Fizza   |   43  |
|  computer  |   62  |
+------------+-------+

This will be displayed when a player changes their name.

Enter a new name: muaz
{'computer': 62, 'muaz': 43}


### References

The following websites were used for installation and command help.

[Pig(dice)game] (https://en.wikipedia.org/wiki/Pig_(dice_game)

[Git] (https://git-scm.com/download/win)

[Ticksymbol] (https://raw.githubusercontent.com/mkaz/termgraph/main/README.md)
              (https://github.com/mkaz/termgraph/blob/main/README.md)

[PrettyTable] (https://github.com/jazzband/prettytable)

[Documentation] (https://docutils.sourceforge.io/README.html#quick-start)
                (https://github.com/pdoc3/pdoc)
                (https://realpython.com/generating-code-documentation-with-pycco/)
                https://pdoc.dev/docs/pdoc.html)

[UML] (https://medium.com/@ganesh.alalasundaram/uml-diagram-using-pyreverse-for-python-repository-dd68cdf9e7e1)


### License

MIT License- see file *LICENSE*


### Release
see file *Release.md*
