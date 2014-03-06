def user1():
    pw=input("Input a password.\n")
    if pw=="user1":
        return pw
    else:
        print("Incorrect.\n")
        return None

def user2():
    pw=input("Input a password.\n")
    if pw=="user2":
        return pw
    else:
        print("Incorrect.\n")
        return None


user=input("Input a user name.\n")
try:
    #note: functions are NOT called in the interp dictionary
    interp={"user1": user1,
            "user2": user2}
    password=interp[user]()  #function called and value is named password
    print("\n", password)    #password is printed
except KeyError:
    print("Invalid username.  Come back again.  Bye!\n")
input()
