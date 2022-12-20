def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("Hi", username+"!\n", "You have logged in successfully!")
            return username
        else:
            print("Incorrect password")
            return ""
    else:
        print("Username does not exist")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered")
        return ""
    else:
        print(username, "has been registered!")
        return username
