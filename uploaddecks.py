from upload import *
from game import *
from playFunctObjects import *

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
