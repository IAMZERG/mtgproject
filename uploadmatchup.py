def uploadmatchup():
    cmd=input("enter matchup name\n")
    try:
        matchup=open(cmd, rb)
        boardstates=pickle.load(matchup)
        matchup.close()
    except IOError:
        tryagain=input("Didn't work. Try again(y/n)?\n")
        if tryagain=="y":
            uploadmatchup()
    game(boardstates[-1].p1library, boardstates[-1].p2library)
