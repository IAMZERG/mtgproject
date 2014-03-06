def statcompilation(boardstates):
    boards=sorted(winfilter, newobject(boardstates))
    print("\nGame actions in order of highest winrates for player 1:\n")
    for x in range(len(boardstates)):
        placeholder=boards[x]
        print (placeholder.actions[0]+"  P1 winrate: "+(placeholder.p1wins/placeholder.p2wins)+"\n")
    ##will need to expand a bit, but this should suffice for now.  shows actions associated with the highest winrates.
