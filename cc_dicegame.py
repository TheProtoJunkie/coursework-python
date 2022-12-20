import random

high_score = 0


def dice_game():
    global high_score
    high_score = high_score+roll_result
    return high_score


while True:
    print("1) Roll Dice\n"+"2) Leave Game")
    choice = input("Enter your choice")
    if choice == "1":
        print("Current High Score:", high_score)
        roll_result = random.randint(1, 6)
        print("you rolled a", roll_result)
        if high_score >= roll_result:
            dice_game()
            print("You set a new high score of", high_score, "!!")
            next_round = input(
                "Type 'yes' to play again").lower()
            if next_round == "yes":
                high_score = 0
                print("GAME RESET")
                continue
            else:
                print("Thank you for playing!!")
                break

        else:
            dice_game()
            continue

    if choice == "2":
        print("Thank you for playing!!")
        break
    else:
        print("Invalid option")
