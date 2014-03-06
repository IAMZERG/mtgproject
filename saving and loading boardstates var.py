##Storing the boardstates list in JSON file
##and retrieving it from file

import pickle

boardstates=["cards", "cards","card"]
filename=input("\nEnter a name to save the matchup as.\n")
file=open(filename, "wb")
##writing and reading from binary is key for this to work ("wb")
pickle.dump(boardstates, file)
#    note:   variable,  file
file.close()


## for importing from file:

filename=input("\nEnter the name of a file to load a matchup from.\n")
file=open(filename, "rb")
##writing and reading from binary is key for this to work ("wb")
boardstates=pickle.load(file)


