def gameboard(board, boardstates, ai=0):
    if board.activeplayer==1:  #if it is player 1's turn:
        print("Player 2 Life: ", board.p2life, "\nDeck: ", len(board.p2library), "\nHand: ", len(board.p2hand), "\nGraveyard:", board.p2graveyard, "\n\nP2 Battlefield: ")
        for x in range(len(board.p2battlefield)):
            print(board.p2battlefield[x]+"  "+board.p2status[x])
        print("\n")
        print("\n\n\nPlayer 1 Battlefield: ")
        for x in range(len(board.p1battlefield)):
            print(x + ".  " + board.p1battlefield[x] + "  " + board.p1status[x])
        print("\nGraveyard: ", board.p1graveyard)
        print("Player 1 Life: ", board.p1life, "\nDeck: ", len(board.p1library), "\nHand: ", board.p1hand)
    if board.activeplayer==2:  #if it is player 2's turn:
        print("Player 1 Life: ", board.p1life, "\nDeck: ", len(board.p1library), "\nHand: ", len(board.p1hand), "\nGraveyard:", board.p1graveyard, "\n\nP1 Battlefield: ")
        for x in range(len(board.p1battlefield)):
            print(board.p1battlefield[x]+"  "+board.p1status[x])
        print("\n")
        print("\n\n\nPlayer 2 Battlefield: ")
        for x in range(len(board.p2battlefield)):
            print(board.p2battlefield[x]+"  "+board.p2status[x])
        print("\nGraveyard: ", board.p2graveyard)
        print("Player 2 Life: ", board.p2life, "\nDeck: ", len(board.p2library), "\nHand: ", board.p2hand)
