##to do:
##    1.     DIVIDE FILE INTO MODULES TO MAKE IT MORE MANAGABLE
##    1a.    COMBINE A LOT OF THE SMALLER FUNCTIONS SO i HAVE A NICE, CLEAN LAYOUT FOR THE CODE

##    2.     FOR GAMEWINNER(), CREATE FUNCTIONALITY THAT WAS PRESENT INSIDE GAME() BEFOREHAND:

##        <if command[num]=="6":>
##            win=input("Who won (1 or 2, or 0 if this was not where you wanted to be)?")
##            if win=="1":
##                gamewinner(1, board, boardstates)
##                boardstates.append(newobject(board))
##                game(deck1, deck2)
##            if win=="2":
##                boardstates.append(newobject(board))
##                gamewinner(2, board, boardstates)
##                game(deck1, deck2)
##                #this will put an end to the game, and will prompt to start another


##    3.    FOR ALL FUNCTION DEFINITIONS USED BY GAME FUNCTION (if possible), STICK TO THE FORMAT FUNC_NAME(BOARD, BOARDSTATES, AI=0)

##    5.    FIX DRAW() FUNCTION(TOP PRIORITY)


import random
import pickle

def play(board, boardstates, ai=0):
    gameboard(board, boardstates)
    actionfinished=0
    command=[]

    #since AI is not being implemented, I suppose I can remove this....
    if ai==1:
        command=board.actions
    num=0

    #this may always be necessary, so I might be able to remove the if statement.
    if ai==0:
        command.append(input("\nEnter the player followed by the name of the card being played.  "))
        player,card_name=command[0].split(" ", 1)
        move(board, boardstates, preset=[player+"h to "+player+"b", card_name])
        #print(command)    #this is for testing purposes.
    while board.actionfinished == 0:
        gameboard(board,boardstates)
        print ("\nPerforming action: " + command[0])

        #again, if AI is ever implemented, this will make it easier.  I can re-use the play command, though it might be easier to write a separate command [def ai_play()]
        #to acommodate this functionality using the code in the else statement and a separate ai_game() function that is called when the AI is activated, and reverts back to
        #the game() function when an unknown boardstate is reached.
        if ai==0:

            #this menu is ugly and hard to use.  The other functions are equally ugly and hard to use.  Need to implement Urwid to make this run more smoothly, provide
            #a bit of a GUI feel, and make the whole experience less frustrating and more idiot-proof.

            play_actions= {
                "draw": draw,
                "move": move,
                "bury": bury,
                "life": life,
                "peek": peek,
                "play": play,
                "use": use,
                "maketoken": maketoken,
                "search library": search_library,
                "shuffle": shuffle_board,
                "done": actionfinished,   #Means spell resolves and the actions between this and the "play" command were used to cast the spell.
                "tap": tap,
                "untap": untap,
                "undo": undo
                }
            for x in play_actions.keys():
                print (x)
            print("\nEnter a command.")
            command.append(input())
            num+=1
            print(command[num])
            user_in=command[num]
            print (user_in)
            print(play_actions[command[num]])
            print(play_actions[user_in])
            
            #standard input for when player is inputting commands
            play_actions[user_in](board, boardstates)
        else:
            for x in range(num):
                board.actions.append(command[x])

def use(board, boardstates, ai=0):
    gameboard(board)
    actionfinished=0
    command=[]
    if ai==1:
        command=board.actions
    num=0
    if ai==0:
        command.append(input("\nEnter the player followed by the name of the card being cast.  "))
        player,card_name=command.split(" ", 1)
        #move(board, boardstates, preset=[player+"h to "+player+"b", card_name])
        print(command)
    while board.actionfinished == 0:
        gameboard(board,boardstates)
        print ("\nPerforming action: " + command[0])
        if ai==0:

            play_actions= {
                "draw": draw,
                "move": move,
                "bury": bury,
                "life": life,
                "peek": peek,
                "maketoken": maketoken,
                "search library": search_library,
                "shuffle": shuffle_board,
                "done": action_finished,   #Means spell resolves and the actions between this and the "play" command were used to cast the spell.
                "tap": tap,
                "untap": untap,
                "undo": undo
                }
            for x in play_actions.keys():
                print (x)
            print(play_actions)
            print("\nEnter a command.")
            command.append(input())
            num+=1
            #standard input for when player is inputting commands
            play_actions[command[num]](board, boardstates)
        else:
            for x in range(num):
                board.actions.append(command[x])


def action_finished(board, boardstates, ai=0):
    board.boardnum+=1
    boardstates.append(newobject(board))
    board.actionfinished=1

def bury(board, boardstates, ai=0):
    gameboard(board, boardstates)
    print("Enter a player and cardname to bury it: ")
    command=[]
    command.append(input())
    player, card=command[0].split(" ", 1)
    move(board, boardstates, preset=[player+"b to "+player+"g ", card])
    

def draw(board, boardstates, player=0, cards=1, ai=0):
    command=["car", "duck"] #initilization to avoid error.. just random crap
    print(command)
    if ai==0:
        command=[]
        print(command)
        command.append(input("\nHow many cards are being drawn?"))
        command.append(input("\nWhich Player is drawing (1 or 2)?\n"))
        print(command)
    else:
        command=[]
        if board.actions:
            command.append(board.actions.pop(0))
            command.append(board.actions.pop(0))
    print(command)
    if command[1]=="1":
        cards=[board.p1library.pop(0) for x in range(int(command[0]))]
        board.p1hand=board.p1hand+cards
    else:
        cards=[board.p2library.pop(0) for x in range(int(command[0]))]
        board.p2hand=board.p2hand+cards
    return board


def life(board, boardstates, ai=0):
    commands=[]
    if ai==0:
        commands.append(input("Which player's life total changed(1 or 2)?\n"))
        commands.append(input("How much?\n"))
        commands.append(input("\nIf this life total is set to the number entered previously instead of changed, enter 1.  Otherwise enter 0.\n"))
    else:
        for x in range (3):
            commands.append(board.actions.pop(0))
    if commands[2]=="0":
        if commands[0]=="1":
            board[0]+=int(commands[1])
        if commands[0]=="2":
            board[10]+=int(commands[1])
    if commands[2]=="1":
        if commands[0]=="1":
            board[0]=int(commands[1])
        if commands[0]=="2":
            board[10]=int(commands[1])
    return board

def maketoken(board, boardstates, ai=0):
    command=[]
    if ai==0:
        command.append(input("Enter the type of token, counter or emblem (e.g. poison, +1/+1, loyalty).\n")) #this is command[0]
        command.append(input("\nIs it being attached to something, or is it standalone? (enter 1 or 2)\n")) #this is command[1]
        command.append(input("Which player is this token/emblem/counter for (1 or 2)?\n")) #this is command[2]
    else:
        command=board.actions
    if command[1] == "2":
        #if token/counter is standalone
        if command[2] == "1":
            board.p1battlefield.append(command[0])
        if command[2] == "2":
            board.p2battlefield.append(command[0])
    if command[1] == "1":
        #if token/counter is being attached to something
        if  ai==0:
            command.append(input("What is the counter/other object being attached to?\n")) #this is command[3]
            gameboard(board)
            command.append(input("What is the index of the object that you are attaching things to?\n")) #this is command[4]
        if command[2]=="1":
            #if player==1
            board.p1status[command[4]].append(command[3])
            #adds token to object on battlefield
        if command[2]=="2":
            board.p2status[command[4]].append(command[3])
    if ai==1:
        for x in range(5):
            board.actions.pop(0)
    return (board)

def newobject(obj):
    obj=[obj]
    obj2=obj[:]
    return obj2[0]

def otherplayer(num):
    if int(num)==1:
        return 2
    else:
        return 1


def move(board, boardstates, preset=[""], ai=0):
    
    """
    This is a function meant primarily for the game itself to use.  It's used in "play," "cast,"
    and in doing other things as well.  It can also be called by the user if needed... The other
    functions "should" take care of all the functionality needed by the user, however.
    """
    command=[]

    location_dict={"p1l": board.p1library, "p1h": board.p1hand, "p1g": board.p1graveyard, "p1e": board.p1exile, "p1b": board.p1battlefield, "p1p": board.p1battlefield, "p2l": board.p2library, \
               "p2h": board.p2hand, "p2g": board.p2graveyard, "p2e": board.p2exile, "p2b":board.p2battlefield, "p2p": board.p2battlefield}

    if ai==1:
        command=board.actions

    if preset==[""]:
        for key in location_dict.keys():
            print (key)
        command.append(input("\nEnter two locations to move a card to and from, with \" to \" between them:  "))
        command.append(input("\nEnter the name of the card you would like to move:  "))
    else:
        command.append(preset[0])
        command.append(preset[1])
             

    locations=command[0].split(" to ")
    try:
        card = location_dict[ locations[0] ].pop( location_dict[ locations[0] ].index( command[1] ))
        location_dict[ locations[1] ].append(card)
    except ValueError as err:
        print("Error: "+str(err)+"\nReturning to previous menu.  Press enter to continue.")
        input()
    
    


    
def search_library(board, boardstates, ai=0):
    command=[]
    if ai==0: #{
        command.append(input("\nWhich player's library is being searched(1 or 2)?\n"))
        if command[0]=="1": #{
            for x in range(len(board.p1library)):
                print(str(x)+". "+board.p1library[x])
                #print out a list of all the cards in the deck.
            command.append(input("\nEnter the number of the card.\n"))
        #}
        else:  #{
            for x in range(len(board.p2library)):
                print(str(x)+". "+board.p2library[x]+"\n")
                #print out a list of all the cards in the deck.
            command.append(input("\nEnter the number of the card to be added to your hand.\n"))
        #}
    #}
    else:
        #set command var based on actions, while removing items as necessary
        command.append(board.actions.pop(0))
        command.append(board.actions.pop(0))
    if command[0]=="1":
        board.p1hand.append(board.p1library.pop(int(command[1])))
    else:
        board.p2hand.append(board.p2library.pop(int(command[1])))

def shuffle (bigdeck):
    print ("Shuffling deck.\n")
    i=0
    while i<100000:
        randomnum=random.randint(0,(len(bigdeck)-1))
        card=bigdeck.pop(randomnum)
        bigdeck.append(card)
        i+=1
    print("Shuffling complete.\n")
    return bigdeck

def shuffle_board (board, boardstates, ai=0):
    command=[]
    command.append(input("Which Player is shuffling (1 or 2)?\n"))
    print ("Shuffling deck.\n")
    i=0
    if command[0]=="1":
        while i<100000:
            randomnum=random.randint(0,(len(board.p1library)-1))
            card=board.p1library.pop(randomnum)
            board.p1library.append(card)
            i+=1
    if command[0]=="2":
        while i<100000:
            randomnum=random.randint(0,(len(board.p1library)-1))
            card=board.p2library.pop(randomnum)
            board.p2library.append(card)
            i+=1
    print("Shuffling complete.\n")
    return (board)

class State:
    def __init__(self, p1deck=[], p2deck=[]):
        self.p1life=20
        self.p1hand=[]
        self.p1library=newobject(p1deck)
        self.p1graveyard=[]
        self.p1exile=[]
        self.p1wins=0
        self.p1battlefield=[]
        self.p1tapped=[]
        self.p1status=[]
        self.p1turncount=0
        self.p2life=20
        self.p2hand=[]
        self.p2library=newobject(p2deck)
        self.p2graveyard=[]
        self.p2exile=[]
        self.p2wins=0
        self.p2battlefield=[]
        self.p2tapped=[]
        self.p2status=[]
        self.p2turncount=0
        self.activeplayer=1
        self.gamenum=0
        self.actions=[]
        self.actionfinished=0
        self.boardnum=0
        self.boardnumlist=[]


def tap(board, boardstates, player=0, ai=0):
    if player==0:
        player=board.activeplayer
    gameboard(board, boardstates)
    if ai==0:
        commands=[]
        
    else:
        commands=board.actions
        
    for x in range(1000):
        commandcount+=1
        print("\nPlayer whose permanents are being tapped: "+str(player)+"Enter the index of a permanent that needs to be tapped.  "
              "\nType \"stop\" to stop.\n Player incorrect?  Type \"change\".")
        commands.append(input())
        if commands[x]=="stop":
            break
        if commands[x]=="change":
            print("Enter number of the player (1 or 2)")
            commands.append(input())
            x+=1
            if commands[x] != "1" and commands[x] != "2":
                print("Invalid input.")
                x=x-1
    for x in range(1000):
        if int(player)==1:
            board.p1tapped[int(commands[x])].append("tapped")
        if int(player)==2:
            board.p2tapped[int(commands[x])].append("tapped")      
    if ai==0:
        for x in range(len(commands)):
            board.actions.append(commands[x])
            #should store the commands in the actions list for recall later

def undo(board, boardstates):
    board=newobject(boardstates[board.boardnum-1])
    boardstates.pop(-1)
    return board

def untap(board, boardstates, player=0, ai=0):
    if player==0:
        player=board.activeplayer
    gameboard(board)
    if ai==0:
        commands=[""]
    else:
        commands=board.actions
    commandcount=-1
    while commands[commandcount]!="stop":
        commandcount+=1
        print("\nEnter the index of a permanent that needs to be untapped.  Type \"stop\" to stop.\n")
        commands[commandcount]=input()
    commandcount=0
    while commands[commandcount]!="stop":
        if player==1:
            board.p1tapped.pop(int(commands[commandcount]))
        if player==2:
            board.p2tapped.pop(int(commands[commandcount]))       
    if ai==0:
        for x in range(len(commands)):
            board.actions.append(commands[x])
            #should store the commands in the actions list for recall later



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

def game(deckp1, deckp2, board=State(), boardstates=[], new=0, ai=0):
    if new == 1:
        #if board is the first board created, start with a clean slate
        board=State(deckp1, deckp2)
        board.gamenum+=1
        board.boardnum+=1

                    #basic setup for the start of the game
        commands=[]
        commands.append(random.randint(1,2))
        print(commands)
        commandcount=0
        #dieroll
        print("Player ", commands[0], " has won the die roll.  Will player ", \
              commands[0], " go first (type \"yes\" or \"no\")?")         #commands: 1 (0)
        #player's choice
        commands.append(input())
        print(commands)
        if commands[1]=="yes":                                                       #commands: 2 (1)
            board.activeplayer=commands[0]
            #holds whose turn it is for the active game
        if commands[1]=="no":
            if commands[0]==1:
                board.activeplayer=2
            if commands[0]==2:
                board.activeplayer=1
        else:
            game(deckp1, deckp2, boardstates, new=1)

        
            
        #game begins in earnest here
        print("And so it begins.\n")
        print(board.activeplayer)
        board.p1library=shuffle(board.p1library)
        board.p2library=shuffle(board.p2library)
        draw_board(board, 1, 7)
        draw_board(board, 2, 7)
        mullcountap=0  #mull count of active player
        mullcountop=0  #mull count of other player
        mull=[0,"yes","yes"]
        print(board.activeplayer*100)
        
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
                            board=draw_board(board, 1, (7-mullcountap))
                        else:
                            board.p2library=board.p2library+newobject(board.p2hand)
                            board.p2hand=[]
                            board.p2library=shuffle(board.p2library)
                            board=draw_board(board, 2, (7-mullcountap))
                player=otherplayer(board.activeplayer)
                if mull[player]=="yes":
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
                            board=draw_board(board, 1, (7-mullcountop))
                        else:
                            board.p2library=board.p2library+newobject(board.p2hand)
                            board.p2hand=[]
                            board.p2library=shuffle(board.p2library)
                            board=draw_board(board, 2, (7-mullcountop))            
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
                    "play": play,                      ##used for playing lands, casting spells, etc.
                    "use": use,                        ##takes care of triggered abilities, attacking
                    "endturn": endturn,                ##ends the turn
                    "undo": undo,                      ##undoes the turn
                    "stats": statcompilation,          ##shows stats from games played in the matchup
                    "gamewinner": gamewinner,
                    "save": save,
                    "laod": load,
                    "quit": quitgame
                    }
            
            print("\n", "Commands:\n")
            for x in interp.keys():
                print(x)
            print("\nEnter a command\n")
            command.append(input())
            interp[command[0]](board, boardstates)



    playagain=input("\nWould you like to play again (yes or no)?\n")
    if playagain=="yes":
        game(deckp1, deckp2, boardstates)




def gameboard(board, boardstates, ai=0):
    if board.activeplayer==1:  #if it is player 1's turn:
        print("Player 2 Life: ", board.p2life, "\nDeck: ", len(board.p2library), "\nHand: ", len(board.p2hand), "\nGraveyard:", board.p2graveyard, "\n\nP2 Battlefield: ")
        num=0
        for x in board.p2battlefield:
            num+=1
            print("    "+str(num)+".  "+x+"  ", end="")
            try:
                print(board.p2status[num])
            except IndexError:
                print("")
                pass
        print("\n")
        print("\n\n\nPlayer 1 Battlefield: ")
        num=0
        for x in board.p1battlefield:
            num+=1
            print("    "+str(num)+".  "+x+"  ", end="")
            try:
                print(board.p1status[num])
            except IndexError:
                print("")
                pass
        print("\nGraveyard: ", board.p1graveyard)
        print("Player 1 Life: ", board.p1life, "\nDeck: ", len(board.p1library), "\nHand: ", board.p1hand)
    if board.activeplayer==2:  #if it is player 2's turn:
        print("Player 1 Life: ", board.p1life, "\nDeck: ", len(board.p1library), "\nHand: ", len(board.p1hand), "\nGraveyard:", board.p1graveyard, "\n\nP1 Battlefield: ")
        num=0
        for x in board.p1battlefield:
            num+=1
            print("    "+str(num)+".  "+x+"  ", end="")
            try:
                print(board.p1status[num])
            except IndexError:
                print("")
                pass
        print("\n")
        print("\n\n\nPlayer 2 Battlefield: ")
        num=0
        for x in board.p2battlefield:
            num+=1
            print("    "+str(num)+".  "+x+"  ", end="")
            try:
                print(board.p2status[num])
            except IndexError:
                print("")
                pass
        print("\nGraveyard: ", board.p2graveyard)
        print("Player 2 Life: ", board.p2life, "\nDeck: ", len(board.p2library), "\nHand: ", board.p2hand)

def draw_board(board, player, cards):
    if player==1:
        for x in range(cards):
            board.p1hand.append(board.p1library.pop(0))
    if player==2:
        for x in range(cards):
            board.p2hand.append(board.p2library.pop(0))
    #moves cards from a player's library to hand


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

def load(board, boardstates=[]):
    filename=input("\nEnter the name of a file to load from.\n")
    with open(filename, "rb") as file:
        ##writing and reading from binary is key for this to work ("wb")
        boardstates=pickle.load(file)

def peek(board, boardstates, ai=0):
    if board.activeplayer==1:
        print("Player 2\'s hand:  ", board[12])
    if board[18]==2:
        print("Player 1\'s hand:  ", board[2])


def quitgame(board, boardstates):
    save(boardstates)
    #saves the boardstates as file for the matchup before exiting
    quit()

def save(board, boardstates):
    filename=input("\nEnter a name to save the matchup as.\n")
    with open(filename, "wb") as file:
        ##writing and reading from binary is key for this to work ("wb")
        pickle.dump(boardstates, file)
        #    note:   variable,  file

def statcompilation(boardstates):
    boards=sorted(winfilter, newobject(boardstates))
    print("\nGame actions in order of highest winrates for player 1:\n")
    for x in range(len(boardstates)):
        placeholder=boards[x]
        print (placeholder.actions[0]+"  P1 winrate: "+(placeholder.p1wins/placeholder.p2wins)+"\n")
    ##will need to expand a bit, but this should suffice for now.  shows actions associated with the highest winrates.
    ##really needs a good way to visualize all the data... maybe SQLite for that?

def upload(deckname):
    with open(deckname) as textfile:
        file=textfile.read()+"\n"
        file1=file
        deck=[]
        cards=0
    
        for x in range(1000):
            if "\n" in file1:
                cards=file1[:file1.index("\n")]
                file1=file1[file1.index("\n")+1:]
                if len(cards)>0:
                    for y in range(int(cards[0])):
                        deck.append(cards[2:])
            else:
                break
    return newobject(deck)

def uploaddecks(board=[], boardstates=[]):
    deck1=[]      #shells to hold decklists
    deck2=[]
    from_file1="0"
    from_file2="0"
    from_file1=input("To load deck 1 from a file, enter the file name now (minus the .txt extension).\n")
    from_file2=input("To load deck 2 from a file, enter the file name now (minus the .txt extension).\n")
    try:
        deck1=upload(from_file1+".txt")
        deck2=upload(from_file2+".txt")
    except IOError:
        print("Upload failed.  Try again.")
        uploaddecks()
    boardstates=[]
    
    print("\n"*100)
    game(deck1,deck2, new=1)


def uploadmatchup():
    cmd=input("enter matchup name\n")
    try:
        with open(cmd, rb) as matchup:
            boardstates=pickle.load(matchup)
    except IOError:
        tryagain=input("Didn't work. Try again(y/n)?\n")
        if tryagain=="y":
            uploadmatchup()
    game(boardstates[-1].p1library, boardstates[-1].p2library, boardstates[-1], boardstates)


def main():
    cmd=input("What would you like to do? (1. upload decks or 2. load matchup)\n")
    if cmd=="1":
        uploaddecks()
    if cmd=="2":
        uploadmatchup(boardstates=[])
    input("press enter to exit.")

if __name__=="__main__":
    main()
    


