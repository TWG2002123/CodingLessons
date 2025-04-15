
# Below I have done 2 examples of how while loops work. While loops will run through the code indefintely whilst the condition is True

count = 0
while count < 3:
    print(count)
    count += 1

times = 0
while times < 3:
    print(times)
    times += 1

#Random Number Guessing Game

import random  #Importing a random number generator

while True: # The code here repeats whilst the 3 conditions below are True
    secret_number = random.randint(1, 100)
    guess_count = 0
    max_guesses = 10
    
    print("I'm thinking of a number between 1 and 100")
    while guess_count < max_guesses:  #This allows me to keep playing whilst the number of guesses is less than the max guesses
        try:
            guess = input(f"Guess {guess_count + 1} / {max_guesses} or 'q' to quit: ")
            if guess.lower() == 'q':
                print("The game has ended")
                break
            guess = int(guess)
            guess_count += 1

            if guess < secret_number:
                print("Too low! Try again")
            elif guess > secret_number:
                print("Too high! Try again")
            else:
                print(f"Congratulations! You guessed it in {guess_count} goes")
                break
        except ValueError:
            print("Enter a Number or 'q' to quit")

    if guess_count >= max_guesses and guess!= secret_number:
        print(f"Game Over! The correct number was {secret_number} ")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for Playing!")
        break









