#!/usr/bin/env python3
# Created by: Zack Isingoma
# Created on: 15th,december 2021.
# This program uses a try statement

import random


def main():
    # this function uses a try statement
    random_num = random.randint(1, 10)

    guess_string = input("Guess a number between 1 and 10: ")
    print("")

    # process & output
    try:
        guess_number = int(guess_string)
        if guess_number == random_num:
            print("Well done")
        else:
            print("OOh so close")
            print("The correct number was {}".format(random_num))
    except Exception:
        print("This was not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
