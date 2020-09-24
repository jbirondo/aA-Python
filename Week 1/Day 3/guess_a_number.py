import random

num_guesses = 0
max_guesses = 5
rand = random.randint(1, 20)

user_name = input("What is your name?: ")

print("Well, {}, I am thinking of a number between 1 and 20.".format(user_name))
guess = input("Take a guess: ")

while num_guesses < max_guesses:
    if int(guess) < int(rand):
        num_guesses += 1
        print("Guess is too low.")
        guess = input("Take a guess: ")
    elif int(guess) > int(rand):
        num_guesses += 1
        print("Guess is too high.")
        guess = input("Take a guess: ")
    elif int(guess) == int(rand):
        num_guesses += 1
        print("Good job {}! You guessed the number in {} guesses!".format(user_name, num_guesses))
        break

