print("Program Started")
try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username != "admin":
        raise Exception("Invalid user name")
    if password != "1234":
        raise Exception("Invalid Password")
    print("Login Successful")
except Exception as e:
    print("Login failed:",e)
finally:
    print("Program ended")