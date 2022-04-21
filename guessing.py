#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that makes the user guess a number

import random


def main():
    # This Function Runs the Program

    # Input
    counter = 0
    Hidden_Number = random.randint(0, 9)

    # Process & Output
    while True:
        try:
            number_as_string = input("Enter The Number You're Guessing (0-9):")
            number_as_int = int(number_as_string)
            counter = counter + 1
            if number_as_int > Hidden_Number:
                print(
                    "You're number looking kinda big there buddy. Guess a smaller number"
                )
            elif number_as_int < Hidden_Number:
                print("Ooooh that's TOO LOW. Guess BIGGER my friend.")
            else:
                print("DING DING DING! CORRECT! It took you {0} tries!".format(counter))
                break
        except Exception:
            print("Are You Even Trying? ENTER AN INTEGER!!!.")
        finally:
            print("")

    print("\nDone.")


if __name__ == "__main__":
    main()
