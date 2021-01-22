Creating three AI agents that play the game Reversi (also known by the trademark Othello).

Written by python

# game_play.py

This file will plays two AI agents against each other. From the command line, this function is invoked with:

```
python gameplay.py [-t ] [-v] [-r] player1 player2
```

Where player1.py and player2.py are python files that contain a nextMove and nextMoveR. The flags -v stands for verbose output (display the board after every turn, already implemented), and -r stands for "reversed" (use nextMoveR rather than nextMove).

# random_play.py

AI agent that makes a random legal move

# simple_greedy.py

AI agent that uses a brain-dead evaluation function, with no search

# min_max.py

AI agent that uses a minmax search, with alpha-beta pruning

For example, you could have two random players play against each other with:

```
python3 gameplay.py random_play random_play
```

If you wanted to play simple_greedy against random_play (with simple_greedy going first), seeing all the moves, with a clock of 150 seconds:

```
python3 gameplay.py -t150 -v simple_greedy random_play 
```

# q_learn.py

...