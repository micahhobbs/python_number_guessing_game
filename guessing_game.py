"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    print("""
    <===== Welcome to the Python Number Guessing Game! =====>
    """)

    want_to_play = input("Do you want to play? Y/N  ").lower()
    print()
    if want_to_play == "y":
        # Define random number range and counter variables
        random_low = 1
        random_high = 5
        random_number = random.randint(random_low, random_high)

        current_low_score = 0

        # Handle low score logic if it hasn't been set yet
        if current_low_score == 0:
            print("The current low score hasn't been set yet, you're the first player!\n")
        else:
            print("The current low score is {}, goodluck!".format(current_low_score))

        # Continually prompt player for number
        attempt_counter = 0
        while True:
            try:
                print("The random number is somewhere between {} and {}\n".format(
                    random_low, random_high))
                guess = int(input("What do you think the number is?  "))
            except NameError:
                print("Sorry, you entered a strange value, please try again\n")
            else:
                if guess < random_low or guess > random_high:
                    print("That's not in the correct range, try again!\n")
                elif guess > random_number:
                    print("It's lower\n")
                    attempt_counter += 1
                elif guess < random_number:
                    print("It's higher\n")
                    attempt_counter += 1
                else:
                    attempt_counter += 1
                    print("Got it!\n")
                    print("It took you {} attempts to get it right!\n".format(
                        attempt_counter))
                    if current_low_score == 0 or current_low_score > attempt_counter:
                        current_low_score = attempt_counter
                    print("The current low score is {}\n".format(
                        current_low_score))
                    print("<========================================>\n")
                    play_again = input(
                        "Do you want to play again? Y/N  ").lower()
                    if play_again == "y":
                        attempt_counter = 0
                    else:
                        break

    else:
        print("That's a shame, maybe next time!\n")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
