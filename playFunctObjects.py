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


def actionfinished(board, boardstates, ai=0):
    board.boardnum+=1
    boardstates.append(newobject(board))
    board.actionfinished=1

def draw(board, boardstates, ai=0):
    command=["car", "duck"] #initilization to avoid error.. just random crap
    if ai==0:
        command=[]
        command.append(input("\nHow many cards are being drawn?"))
        command.append(input("\nWhich Player is drawing (1 or 2)?\n"))
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
        commands.append(input("\nIf this life total is set instead of changed, enter 1.  Otherwise enter 0.\n"))
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


def move(board, boardstates, ai=0):
    commandcount=-1
    command=[]
    # commandcount+=1 BEFORE EACH command is entered.
    if ai==0:
        print("\nWhat is the name of the object being moved?\n")
        command.append(input())
        print("\nWhich location are you moving an object from:\np1l for p1 library \np1h for p1 hand \np1g for p1 graveyard,\
              \np1e for p1 exile \np1b for p1 battlefield \np1p for p1 permanent \n\nChange 1 to to for p2)?\n")
        command.append(input())
        print("\nWhich location are you moving the object to?")
        command.append(input())
        for x in range(len(command)):
            board.actions.append(newobject(command[x]))
            #appends commands to actions for this boardstate when player is controlling game
    interpret={"p1l": board.p1library, "p1h": board.p1hand, "p1g": board.p1graveyard, "p1e": board.p1exile, "p1b": board.p1battlefield, "p1p": board.p1battlefield, "p2l": board.p2library, \
               "p2h": board.p2hand, "p2g": board.p2graveyard, "p2e": board.p2exile, "p2b":board.p2battlefield, "p2p": board.p2battlefield}
    #this will interpret the commands entered, and allow user inputs to point directly to where the objects need to go from and to
    if ai==1:
        #if ai is engaged
        interpret[board.actions[1]].append(interpret[board.actions[0]])
        for x in range(3):
            board.actions.pop(0)
    if ai==0:
        interpret[command[2]].append(command[0])
        interpret[command[1]].pop(interpret[command[1]].index(command[0]))


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
        self.activeplayer=[]
        self.gamenum=0
        self.actions=[]
        self.actionfinished=0
        self.boardnum=0
        self.boardnumlist=[]


def tap(board, boardstates, player=0, ai=0):
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
        print("\nEnter the index of a permanent that needs to be tapped.  Type \"stop\" to stop.\n")
        commands[commandcount]=input()
    commandcount=0
    while commands[commandcount]!="stop":
        if int(player)==1:
            board.p1tapped[int(commands[commandcount])].append("tapped")
        if int(player)==2:
            board.p2tapped[int(commands[commandcount])].append("tapped")      
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



