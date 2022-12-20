def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login    | 2.    Register     |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate   | 4.    Show Donations      |")
    print("------------------------------------------")
    print("              5.    Exit              ")
    print("------------------------------------------")


def donate(username):
    donation_amount = input("How much would you like to donate: $")
    donation_string = (username, "Donated $"+donation_amount)
    print("Thank you for your donation!")
    return donation_string


def show_donations(donations):
    print("\n--- All Donations ---")
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        for gifts in donations:
            gifts = donations
            print(gifts)
