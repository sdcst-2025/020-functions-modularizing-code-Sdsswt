"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
def title():
    print("game rules: chose a number between 1 and 10,\n if the number is the same random number that you picked it will tell you chose the right number,\n if you dont chose the same number\n it will tell you that you chose the wrong number")

def game():
   y = int(input("enter a number between 1 and 10: "))
   x = (random.randint(0,11))
   while x!=y:
    if x != y:
       print("you chose the wrong number")
       y = int(input("enter a number between 1 and 10: "))
    if x == y:
        print("you chose the right number")
        break


title()
game()