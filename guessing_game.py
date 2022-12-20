import random

prev_guesses = []


def guess_random_number(tries, start, stop):
    secret_num = random.randint(start, stop)
    while tries >= 0:
        print('You have', tries, 'tries left')
        my_guess = input("Guess a number between " +
                         str(start)+" and "+str(stop)+': ')
        prev_guesses.append(my_guess)
        if my_guess in prev_guesses:
            print('You already guessed that number')
        elif int(my_guess) == secret_num:
            print('You guessed the right number!')
            break
        elif int(my_guess) > secret_num:
            print('You guessed too high')
            tries -= 1
            continue
        elif int(my_guess) < secret_num:
            print('You guessed too low')
            tries -= 1
            continue
        elif int(my_guess) < start or my_guess > stop:
            print('You guessed out of range')
            continue
        elif tries == 0:
            print('You ran out of guesses!')
            break
    return


def guess_random_number_linear(tries, start, stop):
    secret_num = random.randint(start, stop)
    for i in range(stop):
        print('There are', tries, 'tries left')
        if i == secret_num:
            print('The secret number has been found! it is', i)
            return
        if tries == 0:
            print('The secret number was not found')
            return
        else:
            tries -= 1
            print('The program guessed incorrectly')


def guess_random_number_binary(tries, start, stop):
    secret_num = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
        print('There are', tries, "tries left")
        pivot = (lower_bound+upper_bound)//2
        if pivot == secret_num:
            print('The secret number has been found! it is', pivot)
            return pivot
            break
        if pivot > secret_num:
            print('The secret number guess was incorrect')
            upper_bound = pivot-1
            tries -= 1
        if tries == 0:
            print('The secret number was not found')
            break
        else:
            print('The secret number guess was incorrect')
            lower_bound = pivot+1
            tries -= 1
    return -1

# ===== test driver code - task 1 =====#
#guess_random_number(5, 0, 10)

# ===== test driver code - task 2 =====#
#guess_random_number_linear(5, 0, 10)


# ===== test driver code - task 3 =====#
guess_random_number_binary(5, 0, 10)
