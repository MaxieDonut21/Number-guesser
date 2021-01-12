username = 'YOUR USERNAME HERE'


def pw():
    username = 'YOUR USERNAME HERE'
    password = 'YOUR PASSWORD HERE'

    usernameinput = input("Username: ")
    passwordinput = ""

    if usernameinput == username:
        passwordinput = input("Password: ")
    elif usernameinput != username:
        while usernameinput != username:
            usernameinput = input("Username: ")
        if usernameinput == username:
            print("Correct Username!")
        elif usernameinput != username:
            print("Incorrect username, please try again")
    if passwordinput == password:
        print("Password Correct! Logging you in...")
    elif passwordinput != password:
        while passwordinput != password:
            passwordinput = input("Password: ")
        if passwordinput == password:
            print("Password Correct! Logging you in...")
        elif passwordinput != password:
            print("Incorrect password, please try again")











