class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        print("Your username has been changed to:", self.name)

    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to: ", self.pin)

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to: ", self.password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print("Hi", self.name+", your balance is: ", self.balance)

    def withdraw(self):
        withdraw_amount = input(
            "Hi "+self.name+", how much would you like to withdraw:")
        self.balance = float(self.balance)-float(withdraw_amount)
        return (self.balance)

    def deposit(self):
        deposit_amount = input(
            "Hi "+self.name+", how much would you like to deposit:")
        self.balance = float(self.balance)+float(deposit_amount)
        return (self.balance)

    def transfer_money(self):
        check_pin = input("Hi "+self.name+", please verify your pin")
        if int(check_pin) == self.pin:
            transfer_amount = input(
                "How much money would you like to transfer:")
            bankuser1.balance = float(bankuser1.balance)+float(transfer_amount)
            self.balance = float(self.balance)-float(transfer_amount)
            return (True, bankuser1.balance, self.balance)
        else:
            print("Incorrect pin.")
            return (False)

    def request_money(self):
        check_pin = input("Hi "+bankuser1.name +
                          ", you've received a request for money from"+self.name+", please verify your pin: ")
        if int(check_pin) == bankuser1.pin:
            check_password = input("Hi "+self.name +
                                   ", please verify your password:")
            if check_password == self.password:
                request_amount = input(
                    "How much money would you like to request: ")
                bankuser1.balance = float(
                    bankuser1.balance)-float(request_amount)
                self.balance = float(self.balance)+float(request_amount)
                return (True, bankuser1.balance, self.balance)
        else:
            print("Incorrect pin.")
            return (False)


""" Driver Code for Task 1 """
'''
user1 = User("Bob", 1234, "best*password*ever")
print(user1.name, user1.pin, user1.password)
'''

""" Driver Code for Task 2 """
'''user1 = User("Bob", 1234, "best*password*ever")
print(user1.name, user1.pin, user1.password, "\n")
print("...changing stuff...\n")
user1.change_name("Better Bob")
user1.change_pin(4321)
user1.change_password("best*password*ever_TIMES_INFINITY!\n")
print("...new stuff...\n")
print("Username:", user1.name, "\nUser PIN:",
      user1.pin, "\nUser password:", user1.password)
'''

""" Driver Code for Task 3 """
'''bankuser1 = BankUser("Bob", 1234, "best*password*ever")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
'''
""" Driver Code for Task 4 """
'''bankuser1 = BankUser("Bob", 1234, "best*password*ever")
bankuser1.show_balance()
bankuser1.withdraw()
bankuser1.show_balance()
bankuser1.deposit()
bankuser1.show_balance()
'''
""" Driver Code for Task 5 """
bankuser1 = BankUser("Tarzan", 1111, "password1")
bankuser2 = BankUser("Jane", 2222, "password2")
bankuser2.deposit()
print("...Initial Balance...")
bankuser2.show_balance()
print()
bankuser1.show_balance()
bankuser2.transfer_money()
print("...New balance after transfer...")
bankuser2.show_balance()
print()
bankuser1.show_balance()
bankuser2.request_money()
print("...New balance after request...")
bankuser2.show_balance()
print()
bankuser1.show_balance()
