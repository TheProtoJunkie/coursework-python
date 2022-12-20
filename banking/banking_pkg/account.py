def show_balance(balance):
    print("The current balance is:", float(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return (balance+float(amount))


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return (balance-float(amount))


def logout(name):
    print("Goodbye", name, "!")
