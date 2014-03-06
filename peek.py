def peek(board, boardstates, ai=0):
    if board.activeplayer==1:
        print("Player 2\'s hand:  ", board[12])
    if board[18]==2:
        print("Player 1\'s hand:  ", board[2])
