from playFunctObjects import *

def upload(deckname):
    textfile=open(deckname)
    file=textfile.read()+"\n"
    file1=file
    textfile.close()
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
