# author - Kishan Sindhi
# date - 30-5-2021
# discription - This is the simple number guessing game 
# in this mini project the user enters a upper limit and a lower limit
# the one who guess the number in less guess wins the game


import random


def play(ll, ul, hidden, player):
    print(f"{player} guess the number between {ll} and {ul}")
    trail = 0
    while True:
        guess = int(input("Guess the number - "))
        trail = trail+1
        if guess == hidden:
            print("Correct guess!")
            break
        elif hidden > guess:
            print("Guessed number is small than the hidden number")
        else:
            print("Guessed number is greater than the random number")
    return trail


if __name__ == '__main__':
    print('''Welcome to guess the number game!
    This is a multi-player game.
    In this game you have to guess a number from the given range of number.
    The one who guess the number first wins the game.
    --------------------------------------------------------''')
    lower_limit = int(input("Enter the lower limit\n"))
    upeer_limit = int(input("Enter the upper limit\n"))
    p1_mane = input("Enter your name player 1\n")
    p2_name = input("Enter your name player 2\n")

    hidden_num = random.randint(lower_limit, upeer_limit)
    p1 = play(lower_limit, upeer_limit, hidden_num, p1_mane)

    hidden_num2 = random.randint(lower_limit, upeer_limit)
    p2 = play(lower_limit, upeer_limit, hidden_num2, p2_name)

    print(f"\n---------------------------------------"
          f"\n\t\tSCORECARD"
          f"\n\t\t{p1_mane}-{p1}"
          f"\n\t\t{p2_name}-{p2}"
          f"\n---------------------------------------")

    if p1 > p2:
        print(f"{p1_mane} Wins the game!!\n"
              f"Congrats!!!\n"
              f"{p2_name} better luck next time\n")
    elif p2 > p1:
        print(f"{p2_name} Wins the game!!\n"
              f"Congrats!!!\n"
              f"{p1_mane} better luck next time\n")
    else:
        print(f"Its a tie!!!")
