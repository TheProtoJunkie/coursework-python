from donations_pkg.user import *
import donations_pkg
from donations_pkg.homepage import *
database = {"admin": "password123"}  # holds user names and passwords
donations = []
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: "+authorized_user)
    selection = input("Make a selection ")
    if selection == "1":
        username = input("please enter username: ")
        password = input("please enter your password: ")
        authorized_user = login(database, username, password)
        continue
    if selection == "2":
        username = input("please enter username: ")
        password = input("please enter your password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password
        continue
    if selection == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
            continue
    if selection == "4":
        show_donations(donations)
        continue
    if selection == "5":
        print("Leaving DonateMe...\nGoodbye!")
        break
    else:
        print("Invalid Selection")
