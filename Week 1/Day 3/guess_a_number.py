from random import randint

num_guesses = 0
max_guesses = 5
rand = randint(1, 20)

user_name = input("What is your name?: ")

print("Well, {}, I am thinking of a number between 1 and 20.".format(user_name))

while num_guesses <= max_guesses:
    guess = input("Take a guess: ")
    if num_guesses == max_guesses:
        print("Sorry, {}. You could not guess my number {}.".format(user_name, rand))
        break
    elif int(guess) < int(rand):
        num_guesses += 1
        print("Guess is too low.")
    elif int(guess) > int(rand):
        num_guesses += 1
        print("Guess is too high.")
    elif int(guess) == int(rand):
        num_guesses += 1
        print("Good job {}! You guessed the number in {} guesses!".format(user_name, num_guesses))
        break




