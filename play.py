def play(board, boardstates, ai=0):
    gameboard(board)
    actionfinished=0
    command=[]
    if ai==1:
        command=board.actions
    num=0
    if ai==0:
        command.append(input("\nDescribe the action being performed.  "))
    while board.actionfinished == 0:
        print ("\nPerforming action: " + command[0])
        if ai==0:

            interp= {
                "draw": draw,
                "move": move,
                "life": life,
                "peek": peek,
                "maketoken": maketoken,
                "search library": search_library,
                "shuffle": shuffle_board,
                "actionfinished": actionfinished,   #Means spell resolves and the actions between this and the "play" command were used to cast the spell.
                "tap": tap,
                "untap": untap,
                "undo": undo
                }
            print(interp)
            print("\nEnter a command.")
            command.append(input())
            #standard input for when player is inputting commands
            interp[command[num]](board, boardstates, ai)
            num+=1
            #this will only be needed when the ai isn't running
        


    else:
        for x in range(num):
            board.actions.append(command[x])
