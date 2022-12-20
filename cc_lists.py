import random
diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []
while diamonds:
    pick_a_card = input("press 1 to pick a random card, press Q to quit: ")
    if pick_a_card.upper() == "Q":
        print("Thanks for playing!")
        break
    if pick_a_card == "1":
        card_picked = random.choice(diamonds)
        print(card_picked)
        diamonds.remove(card_picked)
        your_hand = hand.append(card_picked)
        print("This is your hand now: ", hand, "Pick another card")
        print("Diamonds left to pick:", diamonds)
    if not diamonds:
        print("There are no more cards to pick!")
        break
    else:
        print("Invalid input, please press 1 or Q")
