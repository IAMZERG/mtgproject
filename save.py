def save(boardstates):
    filename=input("\nEnter a name to save the matchup as.\n")
    file=open(filename, "wb")
    ##writing and reading from binary is key for this to work ("wb")
    pickle.dump(boardstates, file)
    #    note:   variable,  file
    file.close()
