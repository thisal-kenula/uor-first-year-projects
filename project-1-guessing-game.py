# Semester 1 – Project 1 – Guessing game

import random;

x = random.randint(1, 100)
marks = 100

while True:
    guess = int(input("Guess a number: "))
    if guess > x:
        print("Too large")
    elif guess < x:
        print("Too small")
    elif x == guess:
        print("You've guessed it correctly..🎉")
        print(f"Marks: {marks}")
        break
    marks-=5
