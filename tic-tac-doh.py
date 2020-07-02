"""
REQUIREMENTS:
Create a game for two players; X and O.
Each play places their token somewhere on a line,
It can be at either end or anywhere in the middle.
The game starts with a line 9 units long.
To win you must have three consecutive tokens of your kind.
To avoid losing you may block your opponent using your tokens,
to prevent them from getting three in a row.
The game is over as soon as someone wins,
or all the spaces are filled in.

NAIVE PLAYERS:
1  X . . . . . . . .
2  X . . . Y . . . .
3  X X . Y Y . . . .
3  X X X Y Y . . . .
X WINS!

EXPERT PLAYERS:
1  . . . . . . . . .
2  . . . . X . . . .
3  . . . . X Y . . .
4  . . . X X Y X . .
5  . . Y X X Y X . .
6  . . Y X X Y X X .
7  . . Y X X Y X X Y
8  Y . Y X X Y X X Y
9  Y X Y X X Y X X Y
ITS A TIE!

"""

