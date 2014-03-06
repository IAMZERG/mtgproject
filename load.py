def load(boardstates=[]):
    filename=input("\nEnter the name of a file to load from.\n")
    file=open(filename, "rb")
    ##writing and reading from binary is key for this to work ("wb")
    boardstates=pickle.load(file)
