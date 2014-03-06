from playFunctObjects import *
from gameboard import *
from peek import *
from endturn import *
from statcompilation import *
from save import *
from load import *
from quitgame import *

import random

def game(deckp1, deckp2, board=State(), boardstates=[], new=0, ai=0):
    if new == 1 and board.gamenum == 0:
        #if board is the first board created, start with a clean slate
        board=State(deckp1, deckp2)
        board.gamenum+=1
        board.boardnum+=1

                    #basic setup for the start of the game
        commands=[]
        commands.append(random.randint(1,2))
        commandcount=0
        #dieroll
        print("Player ", commands[0], " has won the die roll.  Will player ", \
              commands[0], " go first (type \"yes\" or \"no\")?")         #commands: 1 (0)
        #player's choice
        commands.append(input())
        commandcount+=1
        if commands[1]=="yes":                                                       #commands: 2 (1)
            board.activeplayer=commands[0]
            #holds whose turn it is for the active game
        elif commands[1]=="no":
            if commands[0]==1:
                board.activeplayer=2
            if commands[0]==2:
                board.activeplayer=1
        else:
            game(deck1, deck2, boardstates, new=1)

        
            
        #game begins in earnest here
        print("And so it begins.\n")
        draw(board, 1, 7)
        draw(board, 2, 7)
        mullcountap=0  #mull count of active player
        mullcountop=0  #mull count of other player
        mull=[0,"yes","yes"]
        
        while mull[1]=="yes":
            while mull[2]=="yes":
                #this is the only way I could think of to implement the current mulligan rules for Magic: the Gathering
                #basically, it is two while loops that will exit whenever the user inputs anything other than "yes"
                if mull[board.activeplayer]=="yes":
                    if board.activeplayer==1:
                        print("\n", board.p1hand)
                    else:
                        print("\n", board.p2hand)
                    print("Would Player ", board.activeplayer, " like to mulligan(type yes or no)?\n")
                    mull[board.activeplayer]=input()
                    if mull[board.activeplayer]=="yes":
                        mullcountap+=1
                        if board.activeplayer==1:
                            board.p1library=board.p1library+newobject(board.p1hand)
                            board.p1hand=[]
                            board.p1library=shuffle(board.p1library)
                            board=draw(board, 1, (7-mullcountap))
                        else:
                            board.p2library=board.p2library+newobject(board.p2hand)
                            board.p2hand=[]
                            board.p2library=shuffle(board.p2library)
                            board=draw(board, 2, (7-mullcountap))
                if mull[otherplayer(board.activeplayer)]=="yes":
                    if otherplayer(board.activeplayer)==1:
                        print("\n", board.p1hand)
                    else:
                        print("\n", board.p2hand)
                    print("\nWwould Player ", otherplayer(board.activeplayer), " like to mulligan(type yes or no)?\n")
                    mull[otherplayer(board.activeplayer)]=input()
                    if mull[otherplayer(board.activeplayer)]=="yes":
                        mullcountop+=1
                        if otherplayer(board.activeplayer)==1:
                            board.p1library=board.p1library+newobject(board.p1hand)
                            board.p1hand=[]
                            board.p1library=shuffle(board.p1library)
                            board=draw(board, 1, (7-mullcountop))
                        else:
                            board.p2library=newobject(board.p2library+board.p2hand)
                            board.p2hand=[]
                            board.p2library=shuffle(board.p2library)
                            board=draw(board, 2, (7-mullcountop))            
        board.boardnum+=1
        boardstates.append(newobject(board))
        #the game appends the boarstate to big list of boardstates once mulligans are recorded.  This will be used for analysis of the success of opening hands
        
        #end of code for handling board, mulligans, etc. when new==1
    else:
        #otherwise, use data from the previous boardstates.
        try:
            tempboard=boardstates[-1]
        except IndexError:
            tempboard=boardstates[0]
        board=newobject(tempboard)
        board.boardnum=newobject(tempboard.boardnum+1)
        board.p1wins=newobject(tempboard.p1wins)
        board.p2wins=newobject(tempboard.p2wins)
        board.gamenum+=1

    gamewinner=0
    num=-1

    while board.p1wins==0:
        while board.p2wins==0:
            gameboard(board, boardstates)
            command=[]
            interp={"peek": peek,                      ##reveals non-active player's hand
                    "untap": untap,                    ##untaps permanents
                    "draw": draw,                      ##draw card for turn
                    "play": play,                      ##used for triggered abilities, activated abilities, "casting," and playing lands
                    "endturn": endturn,                ##ends the turn
                    "undo": undo,                      ##undoes the turn
                    "stats": statcompilation,          ##shows stats from games played in the matchup
                    "gamewinner": gamewinner,
                    "save": save,
                    "laod": load,
                    "quit": quitgame
                    }
            
            print(interp)
            print("\nEnter a command\n")
            command.append(input())
            interp[command[0]](board, boardstates)



    playagain=input("\nWould you like to play again (yes or no)?\n")
    if playagain=="yes":
        game(deckp1, deckp2, boardstates)

