#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that makes the user guess a number

import random


def main():
    # This Function Runs the Program

    # Input
    number_as_string = input("Enter The Number You're Guessing (0-9):")
    Hidden_Number = random.randint(0, 9)

    # Process & Output
    try:
        number_as_int = int(number_as_string)
        if number_as_int == Hidden_Number:
            print("You Were Correct! Hooray! You're Lucky!")
        else:
            print("You Were Incorrect! You Fool! You Blundered!")
    except Exception:
        print("Ok wise guy why don’t you enter a real number next time.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
