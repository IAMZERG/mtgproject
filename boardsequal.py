from playFunctObjects import *

def boardsequal(board, boardstates):
    """
This function returns a list of all the boards that are equivalent to the current board.  Will be used in AI eventually.
    """
    equivalentboards=[]
    for x in range(len(boardstates)):
        if sorted(newobject(board.p1battlefield + board.p2battlefield))== sorted(newobject(boardstates[x].p1battlefield + boardstates[x].p2battlefield)):
        #if the battlefields are the same:
            equivalentboards.append(newobject(boardstates[x]))
            #append the boardstate to the list
    return equivalentboards
#syntax: sameboards=boardsequal(board,boardstates)
