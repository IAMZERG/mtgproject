from playFunctObjects import State

def endturn(board, boardstates, ai=0):
    """This function takes care of creating a new board for the new turn,
    increasing the turn counter, and changing the active player."""
    if board.activeplayer==1:
        boardstates.append(newobject(board))
        board.p1turncount+=1
        board.activeplayer=2
        board.boardnum+=1
    if board.activeplayer==2:
        boardstates.append(newobject(board))
        board.p2turncount+=1
        board.activeplayer=1
        board.boardnum+=1
