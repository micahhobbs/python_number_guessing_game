"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

print("\n<===== Welcome to the Python Number Guessing Game! =====>")


def start_game():

    want_to_play = input("\nDo you want to play? Y/N  ").lower()

    if want_to_play == "y":
        # Define random number range and counter variables
        random_low = 1
        random_high = 5
        random_number = random.randint(random_low, random_high)
        current_low_score = 0

        # Handle low score logic if it hasn't been set yet
        if current_low_score == 0:
            print(
                "\nThe current low score hasn't been set yet, you're the first player!")
        else:
            print("The current low score is {}, goodluck!".format(current_low_score))

        # Tell the player what the number range they need to guess in
        print("\nThe random number is somewhere between {} and {}".format(
            random_low, random_high))

        # Continually prompt player for number
        attempt_counter = 0
        while True:
            try:
                guess = int(input("\nWhat do you think the number is?  "))
            except (ValueError, NameError):
                print("\nSorry, you entered a strange value, please make sure it is a whole number between {} and {}".format(
                    random_low, random_high))
            else:
                if guess < random_low or guess > random_high:
                    print("\nThat's not in the correct range, try again!")
                elif guess > random_number:
                    print("\nIt's lower")
                    attempt_counter += 1
                elif guess < random_number:
                    print("\nIt's higher")
                    attempt_counter += 1
                else:
                    attempt_counter += 1
                    print("\nGot it!\n")
                    print("It took you {} attempts to get it right!\n".format(
                        attempt_counter))
                    if current_low_score == 0 or current_low_score > attempt_counter:
                        current_low_score = attempt_counter
                    print("The current low score is {}\n".format(
                        current_low_score))
                    print(
                        "<=========================================================>\n")
                    play_again = input(
                        "Do you want to play again? Y/N  ").lower()
                    if play_again == "y":
                        attempt_counter = 0
                    elif play_again == "n":
                        print("\nNo worries, thanks for playing!\n")
                        break
                    else:
                        print("Please enter Y for Yes or N for No")
    elif want_to_play == 'n':
        print("That's a shame, maybe next time!\n")
    else:
        print("\nPlease enter Y for Yes or N for No")
        start_game()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
