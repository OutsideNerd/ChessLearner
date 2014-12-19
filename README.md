ChessLearner
============
Chesslearner is a project which observes a game of chess by reading in a text file and 
generates a list of how the pieces move. 

This program includes the Sunfish chess engine, which will be modified to read in pieces.

Feel free to play around with the code.

Modifications to Sunfish
============

Sunfish is modified to  write the state of the game to a text file.

Sunfish can be run as 'python sunfish.py mode <output file>'

mode argument can be either 'c' or 'r', and specifies whether to play against the computer
or have Sunfish generate random chess moves until the game is one by one of the sides (the king
can be placed in check). Playing randomly will generate a number games as specified by
the GAMES_PLAYED variable in 'sunfish.py'. The moves generated will be written out in files named
'game<number>.txt'.

output file is an optional argument for specifying the name of the file to output the game state to
when playing against the compute.

Running the program
====================

'MoveLearner.py' contains the code which inputs a series of chess games represented by board states, and
produces a movelist for all the pieces. The python file should be run as 'python MoveLearner.py game_list output_file'

'game_list' is the filename for a text file where each line contains a filename for a game to be examined

'output_file' is the filename for a text file to output the moves to

Sample Input For a Game of Chess
=====================

rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR
rnbqkbnrpppppppp.................P..............P.PPPPPPRNBQKBNR
rnbqkbnrpppp.ppp............p....P..............P.PPPPPPRNBQKBNR
rnbqkbnrpppp.ppp............p....P............P.P.PPPP.PRNBQKBNR
rnb.kbnrpppp.ppp............p....P.....q......P.P.PPPP.PRNBQKBNR
rnb.kbnrpppp.ppp............p....P....Pq........P.PPPP.PRNBQKBNR
rnb.kb.rppppnppp............p....P....Pq........P.PPPP.PRNBQKBNR
rnb.kb.rppppnppp............p....P....Pq....P...P.PP.P.PRNBQKBNR
rnb.kb.rppppnpp.............p..p.P....Pq....P...P.PP.P.PRNBQKBNR
rnb.kb.rppppnpp.............p..p.P...PPq....P...P.PP...PRNBQKBNR
rnb.kb..ppppnpp........r....p..p.P...PPq....P...P.PP...PRNBQKBNR
rnb.kb..ppppnpp........r....p..P.P...P.q....P...P.PP...PRNBQKBNR
rnb.kb..ppppnpp........r.......P.P..pP.q....P...P.PP...PRNBQKBNR
rnb.kb..ppppnpp........r.......P.P..pP.q...BP...P.PP...PRNBQK.NR
rnb.kb..ppppnp........pr.......P.P..pP.q...BP...P.PP...PRNBQK.NR
rnb.kb..ppppnp........pr.......P.P..pP.q...BP...PBPP...PRN.QK.NR
rnb.kb..ppppnp........pr.......P.P..pP.....BP...PBPP...PRN.Qq.NR
2

Each row of the text file corresponds to the board configuraton at each turn. The number at the end specifies
which player won the game, with 1 being the player on the right, and 2 being the player on the left.

Sampe Output For a Game of Chess
=======================

The output for an analyzed chess game looks s follows:

B
(1, -1, 2, 2, 0)
(-1, -1, 4, 0, 0)
(1, 1, 4, 2, 2)
(1, -1, 3, 2, 0)
(-1, 1, 4, 2, 2)
(1, -1, 4, 0, 1)
(1, 1, 2, 1, 2)
(-1, -1, 5, 2, 0)
(-1, 1, 6, 1, 2)

K
(1, 0, 1, 2, 0)
(1, -1, 1, 2, 0)
(0, -1, 1, 2, 0)
(-1, 0, 1, 2, 0)
(-1, 1, 1, 0, 2)
(1, 1, 1, 0, 2)
(-1, -1, 1, 0, 2)
(0, 1, 1, 0, 2)

N
(1, -2, 1, 2, 0)
(-1, -2, 1, 0, 0)
(2, 1, 1, 0, 2)
(1, 2, 1, 0, 2)
(-2, -1, 1, 0, 0)
(-1, 2, 1, 0, 2)
(-2, 1, 1, 0, 2)
(2, -1, 1, 0, 2)

Q
(-1, -1, 2, 2, 0)
(-1, 1, 3, 2, 2)
(1, -1, 5, 2, 2)
(0, 1, 5, 2, 2)
(-1, -1, 4, 1, 2)
(0, -1, 1, 2, 0)
(1, 1, 5, 2, 2)
(1, 0, 1, 0, 0)
(0, 1, 4, 1, 2)
(0, -1, 5, 2, 2)
(-1, 0, 6, 0, 2)
(1, -1, 2, 0, 0)
(-1, 0, 1, 0, 0)
(1, 0, 3, 0, 2)
(1, 1, 2, 1, 2)
(-1, 1, 1, 1, 2)
(-1, -1, 3, 2, 0)
(1, 0, 5, 2, 2)
(-1, 0, 2, 2, 1)
(0, -1, 2, 0, 0)
(0, -1, 4, 1, 2)
(1, -1, 4, 2, 1)

P
(0, -1, 2, 2, 1)
(0, -1, 1, 2, 2)
(-1, -1, 1, 1, 0)
(1, -1, 1, 1, 0)

R
(0, -1, 1, 0, 0)
(0, 1, 7, 2, 2)
(-1, 0, 2, 2, 0)
(0, -1, 6, 2, 2)
(-1, 0, 6, 2, 2)
(1, 0, 2, 2, 0)
(1, 0, 4, 2, 0)
(1, 0, 6, 0, 0)
(0, -1, 4, 0, 0)
(0, -1, 4, 1, 2)
(0, 1, 2, 1, 2)
(-1, 0, 7, 2, 1)
(-1, 0, 3, 1, 2)
(1, 0, 7, 2, 2)
(0, -1, 3, 1, 1)

Each letter corresponds to a piece in the chess game. Also, each tuple represents a possible move for 
that letter, which is explained as follows:

(x-direction, y-direction, length, capture piece condition, initial move condition)

x-direction: horizontal direction in which piece can move
y-direction: vertical direction in which piece can move
length: length of the "vector" in that direction, or max length pieces can move
capture piece condtion: digit representing the rule whether piece can move if an enemy
			piece is captured or not
			0 - can move regardless of empty square or capture
			1 - can only move if enemy piece would be captures
			2- can only move if the square is free
initial move condtion: digit representing whether piece can move to a square if the
			piece is there or not
			0 - can move regardless of whether first move or not
			1 - can only move if the piece is starting out
			2- can only move if the pice has already been moved
