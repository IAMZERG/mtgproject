def user1():
    pw=input("Input a password.\n")
    if pw=="user1":
        return pw
    else:
        print("Invalid input.\n")
        return None

def user2():
    pw=input("Input a password.\n")
    if pw=="user2":
        return pw
    else:
        print("Invalid input.\n")
        return None


user=input("Input a user name.\n")
try:
    interp={"user1": user1, "user2": user2}
    password=interp[user]()
    print("\n", password)
except KeyError:
    print("Invalid username.  Come back again.  Bye!\n")
input()
