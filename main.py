import random

print("Computer picks a number between 1 and 100. Try and guess it.")

computer_choice = random.randint(1, 100)

diff = input("Choose a difficulty. Type 'easy' or 'hard'. : ")

attempts = []

number = 0

if diff == "easy":
    print("You have 10 attempts remaining.")
    number += 10
    for i in range(1, 13):
        attempts.append("*")

elif diff == "hard":
    print("You have 5 attempts remaining.")
    number += 5
    for i in range(1, 8):
        attempts.append("*")

guess = int(input("Make a guess: "))

for attempt in  attempts:

    if guess == computer_choice:
        print("You are correct.")
        break

    elif guess > computer_choice:
        print("Answer is lower.")
        attempts.remove("*")
        number -= 1
        print(f"You have {number} attempts remaining.")
        guess = int(input("Make another guess: "))
        

    elif guess < computer_choice:
        print("Answer is higher.")
        attempts.remove("*")
        number -= 1
        print(f"You have {number} attempts remaining.")
        guess = int(input("Make another guess: "))

    
   



