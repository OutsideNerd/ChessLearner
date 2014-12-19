# This program takes a game of chess game written in as a text file and computes
# a set of moves for the pieces. Each line of a text file consists of a 
# 64-character string, which represents the board after each turn.
# The number on the final line represents which player wins.
#
# Written by: Evan Dyke

import sys
from fractions import gcd

BOARD_WIDTH = 8
BOARD_HEIGHT = 8

def main():
     
     
    f = open(sys.argv[1], 'r')
    inputfiles = f.read().splitlines()
    # Create an empty dictionary to store the moves
    # The dictionary has a key that corresponds to each piece, and has a list
    # of possible moves for that piece. Each possible move is represented as a
    # tuple. 
    #
    # Each tuple is represented as follows: (x-position, y-position, max # spaces in direction, condition)
    # Condition refers to under what conditions the piece can move
    # 0 - any conditions, but piece cannot be blocked in direction of movement 
    # 1 - enemy piece must be in square 
    # 2 - piece has not left starting position
    
    moves = {}
    end_states = []
    game_winners = []
    
    numGamesPlayed = len(inputfiles)
    
    #  Analyze each text file that was imported as a command-line argument
    for filename in inputfiles:
        
        # Read in the information from the file
        f = open(filename, 'r')
        lines = f.readlines()
        
        boardStates = lines[:-1]
        
        # Gets the initial starting configuration of the board
        init_state = boardStates[0]
        
        # Get information on ending positions and winner
        game_winners.append(lines[-1])
        end_states.append(lines[-2])
        
        # Iterate over each move in the game
        for index in range(1, len(boardStates)):
            
            # Determine which player moves
            player = 2 - index % 2
            
            print (str(player) + " played\n" + boardStates[index - 1] + "\n" + boardStates[index])
            
            begin, end = 0,0
            
            count = 0
            
            # Check to see which piece moved
            for i, j in zip(boardStates[index - 1], boardStates[index]):
                
                
                # If player one, check to see if uppercase letter moved from position
                if(player == 1):
                    if (i != j and i.isupper() and j == '.'):
                        begin = count
                        
                    if (i != j and j.isupper()):
                        end = count
                    
                # If player two, check to see if lowercase letter moved form position
                if(player == 2):
                    if (i != j and i.islower() and j == '.'):
                        begin = count
                        
                    if (i != j and j.islower()):
                        end = count
                        
                count+=1
            
            # Translate # spaces moved into pseudo-vector coordinates with direction and length.
            # For instance, if the piece moved (a, b) with respect to its current position where
            # a, b are both integers and there exists an integer c which a, b can be divided by,
            # the direction corresponds to (a/c, b/c) and length correpsonds to c.
            # 
            a, b = end % BOARD_WIDTH - begin % BOARD_WIDTH, end / BOARD_WIDTH  - begin / BOARD_WIDTH
            move_len = abs(gcd(a,b))
            
            # If second player, invert the y-cooridnate moved since we want to see the relative direction
            # the player moved from their POV. Since the board is flipped, we invert, which will help with
            # learning pawn movement
            if(player == 2):
                b = -b
            
            
            
            # Check to see if a piece was captured
            if(((player == 1) and boardStates[index - 1][end].islower()) or 
               ((player == 2) and boardStates[index - 1][end].isupper())):
                status = 1
            
            # Check to see if piece is in starting position
            elif(boardStates[index - 1][begin] == init_state[begin]):
                status = 2
                
            else:
                status = 0
            
            # Store as a tuple (x-distpance, y_distance, length)
            move = (a / move_len, b / move_len, move_len, status)
            
            piece = boardStates[index][end].capitalize()
            
            # Adds the move to the list in the python dictionary
            if(moves.has_key(piece)):
               addToMoveList(moves[piece], move)  
            else:
                moves[piece] = [move]         
    
    print("Number of games read in: " + str(numGamesPlayed))
    print(moves)

    # Determine what configuration of pieces determine how the game is won
    
    winnerCount = {'P':[], 'R':[], 'N':[], 'B':[], 'Q':[], 'K':[]}
    loserCount = {'P':[], 'R':[], 'N':[], 'B':[], 'Q':[], 'K':[]}
    
    # Count the number of pieces for each player
    for endgame, playerWon in zip(end_states, game_winners):
        
        for piece in winnerCount:
            winnerCount[piece].append(0)
        
        for piece in loserCount:
            loserCount[piece].append(0)
        
        for pos in endgame:
            # Check to see the winner of this game so we can add to the 
            # appropriate dictionary
            if(playerWon == "1"):
                if (pos.isupper()):
                    winnerCount[pos][-1]+=1
                elif(pos.islower()):
                    loserCount[pos.upper()][-1]+=1
            
            elif(playerWon == "2"):
                if (pos.isupper()):
                    loserCount[pos][-1]+=1
                elif(pos.islower()):
                    winnerCount[pos.upper()][-1]+=1
                    
            else:
                sys.exit("Who the f*** won if not player 1 or player 2????")
    
    print(winnerCount)
    print(loserCount)

# This  is a function that adds a move in the format (x-pos, y-pos, max # spaces , condition)
# to the list of moves for each piece. It does this by takiing the move and evaluating it against
# existing hypothesis on how pieces move.
# Parameters:
#    move_list - list to add the move to
#    move - move to be added
#          
def addToMoveList(move_list, move):
     
     for known_move in move_list:
         
         # for each move that we know, check to see if the move we are examining
         # causes us to have to revise an earlier rule that we have stored
         
        
         # Check to see if the pieces move in the same direction
        if(known_move[0] == move[0] and known_move[1] == move[1]):
                
            # Exit if move already exists
            if(known_move[2] >= move[2] and known_move[3] == move[3]):    
                return
                
            # Update the known move if for the same status, the piece moves farther
            if(known_move[2] < move[2] and known_move[3] == move[3]):
                known_move = (known_move[0], known_move[1], known_move[2], move[3])
                return
             
            # If a previously known move was just for one of the following scenarios:
            #     -capturing a piece
            #     -piece has not moves form original position
            # and that is contradicted by moving to an empty square or from a non-starting
            # position, update the known move's condition
            elif(known_move[2] >= move[2] and (known_move[3] != 0 and move[3] == 0)):
                known_move = (known_move[0], known_move[1], known_move[2], 0)
                return
    
     # If the move was not found, add it to the end of the list
     move_list.append(move)       
        
        
if __name__ == '__main__':
    if(len(sys.argv) > 1):
        main()
    else:
        sys.exit("Error:  Please enter at least one filename to read moves from")