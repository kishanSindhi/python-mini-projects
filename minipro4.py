from playsound import playsound
from random import randint


def roll():
    dice = randint(1, 6)
    playsound('mini pro\dice.wav')
    if dice == 6:
        print(f"Ohh..!!! You seems to br lucky its 6.\nYou got another chance.")
    else:
        print(f"You got {dice}.")


roll()
while True:
    ans = int(input("Do you want to roll the dice again 1 for YES 2 for NO\n"))
    if ans == 1:
        roll()
    elif ans == 2:
        print("Thankyou for choocing our program for rolling the dice")
        exit()
    else:
        print("You might have entered the wrong value")
        exit()