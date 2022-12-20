import banking_pkg
from banking_pkg.account import *


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


while True:
    name = input("Enter name to register: ").lower()
    if len(name) >= 10:
        print("The maximum name length is 10 characters")
        continue
    elif len(name) == 0:
        print("you must enter a name")
        continue
    else:
        break
while True:
    pin = input("Enter pin to register: ")
    if len(pin) == 4 and pin.isdigit():
        break
    else:
        print("Pin must be 4 digits")
        continue
balance = 0
print(name, "has been registered with a starting balance of $"+str(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    name_to_validate = input("Enter name: ").lower()
    pin_to_validate = input("Enter pin: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid Credentials!")
        continue

while True:
    user = name
    atm_menu(user)
    print("User: "+user)
    option = input("Choose an option: ")
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
    elif option == "3":
        balance = withdraw(balance)
        if balance <= 0:
            print("withdrawal balance more than available balance")
            balance = balance+withdraw(balance)
            continue
        else:
            continue
    elif option == "4":
        logout(name)
        break
    else:
        print("Invalid option")
