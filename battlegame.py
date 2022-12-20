# Task 1/2
# characters
wizard = 'Wizard'
elf = 'Elf'
human = 'Human'
dragon = 'Dragon'
orc = 'Orc'  # bonus task 3

# Health
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
orc_hp = 60

# Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50
orc_damage = 250
my_hp = ''
my_damage = ''

# Task 3
i = 1
while i < 2:
    i = i+1
    while i == 2:
        print('1)', wizard, '\n2)', elf, '\n3)', human, '\n4)',
              orc, "\nTo exit the game, type 5 or 'exit'.")
        character = input('Choose your character: ').lower()  # bonus 1/2
        if character == '1' or character == 'wizard':
            print('You selected: ', wizard,)
            my_character = wizard
            my_hp = wizard_hp
            print('Health: ', wizard_hp)
            my_damage = wizard_damage
            print('Damage: ', wizard_damage)
            break

        if character == '2' or character == 'elf':
            print('You selected: ', elf,)
            my_character = elf
            my_hp = elf_hp
            print('Health: ', elf_hp)
            my_damage = elf_damage
            print('Damage: ', elf_damage)
            break

        if character == '3' or character == 'human':
            print('You selected: ', human,)
            my_character = human
            my_hp = human_hp
            print('Health: ', human_hp)
            my_damage = human_damage
            print('Damage: ', human_damage)
            break

        if character == '4' or character == 'orc':
            print('You selected: ', orc,)
            my_character = orc
            my_hp = orc_hp
            print('Health: ', orc_hp)
            my_damage = orc_damage
            print('Damage: ', orc_damage)
            break
        if character == '5' or character == 'exit':  # bonus task 4
            print('Thanks for playing!')
            break
        else:
            print('Unknown Character')

# task 4
    while True:
        if character == '5' or character == 'exit':  # bonus task 4
            break
        print('ATTACK!!!')
        dragon_hp = dragon_hp-my_damage
        print('The ', my_character, ' damaged the Dragon!')
        print("The Dragon's health is now", dragon_hp)
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            play_again = input(
                'If you would like to play again, type yes: ').lower()
            if play_again == 'yes':
                i = 1
                break
            else:
                print('Thanks for playing!')
                break

        if dragon_hp != 0:
            print("It's the Dragon's turn to attack")
            my_hp = my_hp-dragon_damage
            print(my_character, ' has been damaged by the Dragon')
            print(my_character, ' hp is now ', my_hp)

        if my_hp <= 0:
            print(my_character, ' has lost the battle!')
            play_again = input(
                'If you would like to play again, type yes: ').lower()
            if play_again == 'yes':
                i = 1
                break
            else:
                print('Thanks for playing!')
                break
