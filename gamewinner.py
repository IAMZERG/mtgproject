from playFunctObjects import *
from game import *

#doesn't take the ai argument since it does the same thing either way.
def gamewinner(board, boardstates):
    #this function will find all boardstates from the current game and show the proper winner.
    #board.actions will handle ending the game properly.
    #It will also need to call the game() function properly.
    boardstates.append(newobject(board))
    winner=input("Who won? Enter \"1\" or \"2\" or something else to avoid choosing winner")
    for x in range(len(boardstates)):
        if boardstates[x].gamenum==board.gamenum:
            if winner=="1":
                boardstates[x].p1wins=1
            if winner=="2":
                boardstates[x].p2wins=1
    cmd=input("Play another? \"y\" or \"n\"?")
    if cmd=="y":
        game(deckp1,deckp1,boardstates,board,new=1)
    else:
        quit

