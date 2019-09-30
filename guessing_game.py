#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 30 2019
# This program is a guessing game

correct_number = 5


def main():
    # input
    print("")
    user_input = int(input("Please enter a number from (0-9) : "))
    print("")

    # Process and Output
    if user_input > 9:
        print("Number Too High. Enter a Number from (0-9) only.")
    elif user_input == correct_number:
        print ("Correct Answer!")
    else:
        print("Wrong Number, Try Again")


if __name__ == "__main__":
    main()
