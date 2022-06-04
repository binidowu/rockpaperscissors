import random


print('This is a game of Rock Paper and Scissors')
print('The rules are simple')
print('You can Choose to Play Rock, Paper or Scissors\n')
print('\tRule 1: If you choose to play Rock input "R"')
print('\tRule 2: If you choose to play Paper input "P" ')
print('\tRule 3: If you choose to play Scissor input "S"\n')
print('Note:\tTo win: Rock("R") beats Scissors("S")')
print('\tTo win: Scissors("S") beats Paper("P")')
print('\tTo win: Paper("P") beats Rock("R")')
print('')

# Checks to see if the game was a tie

while True:
    choices = ('R', 'P', 'S')
    computer = random.choice(choices)
    user_choice = input('Your move? ("R","P","S"): ')

    while user_choice not in choices:
        print('Invalid choice. Please choose either rock, paper or scissors!')
        print("")
        break

    if user_choice == "R":
        if computer == "R":
            print(
                f"Player({user_choice}) : CPU({computer})")
            print("Result: It's a tie")
            print('')
            chance = bool(user_choice == computer)
            if chance is True:
                continue
            elif chance is False:
                break

    if user_choice == "S":
        if computer == "S":
            print(
                f"Player({user_choice}) : CPU({computer})")
            print("Result: It's a tie")
            print('')
            chance = bool(user_choice == computer)
            if chance is True:
                continue
            elif chance is False:
                break

    if user_choice == "P":
        if computer == "P":
            print(
                f"Player({user_choice}) : CPU({computer})")
            print("Result: It's a tie")
            print('')
            chance = bool(user_choice == computer)
            if chance is True:
                continue
            elif chance is False:
                break


# Checks to see if the game was won

    if user_choice == "R":
        if computer == "S":
            print(f"Player({user_choice}) : CPU({computer})")
            print("Result: Player won :)")
            win = bool(user_choice != computer)
            if win is True:
                break
            elif win is False:
                continue

    if user_choice == "S":
        if computer == "P":
            print(f"Player({user_choice}) : CPU({computer})")
            print("Result: Player won :)")
            win = bool(user_choice != computer)
            if win is True:
                break
            elif win is False:
                continue

    if user_choice == "P":
        if computer == "R":
            print(f"Player({user_choice}) : CPU({computer})")
            win = bool(user_choice != computer)
            print("Result: Player won :)")
            if win is True:
                break
            elif win is False:
                continue

# Checks to see if the game was lost

    if user_choice == "P":
        if computer == "S":
            print(f"Player({user_choice}) : CPU({computer})")
            print("Result: Player lost! :(")

            choice = input("To play again input 'Y'. To quit input 'Q':  ")
            print("")
            if choice == 'Y':
                continue
            elif choice == "Q":
                break

    if user_choice == "R":
        if computer == "P":
            print(f"Player({user_choice}) : CPU({computer})")
            print("Result: Player lost! :(")

            choice = input("To play again input 'Y'. To quit input 'Q':  ")
            print("")
            if choice == 'Y':
                continue
            elif choice == "Q":
                break

    if user_choice == "S":
        if computer == "R":
            print(f"Player({user_choice}) : CPU({computer})")
            print("Result: Player lost! :(")

            choice = input("To play again input 'Y'. To quit input 'Q':  ")
            print("")
            if choice == 'Y':
                continue
            elif choice == "Q":
                break
