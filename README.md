ChessLearner
============
Chesslearner is a project which observes a game of chess by reading in a text file and 
generates a list of how the pieces move. 

This program includes the Sunfish chess engine, which will be modified to read in pieces.

Feel free to play around with the code.

Modifications to Sunfish
============

Sunfish is modified to  write the state of the game to a text file.

Sunfish can be run as 'sunfish.py mode <output file>'

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
produces a movelist for all the pieces. The python file should be run as 'MoveLearner.py game_list'

'game_list' is the filename for a text file where each line contains a filename for a game to be examined

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