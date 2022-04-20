#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that makes the user guess a number

import constants


def main():
    # This Function Runs the Program

    # Input
    Number = int(input("Enter The Number You're Guessing (0-9):"))

    # Process & Output
    if Number != constants.HIDDEN_NUMBER:
        print("You Were Incorrect! You Fool! You Blundered! :(")
    if Number == constants.HIDDEN_NUMBER:
        print("You Were Correct! Hooray! You're Lucky! :)")
    print("\nDone")


if __name__ == "__main__":
    main()
