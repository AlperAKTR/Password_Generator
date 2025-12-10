import random
import time
from Utilities import int_input, yes_no
from Utilities import Color


def character_group():

    lower_cases = "abcdefghijklmnopqrstuvwxyz"
    upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symboles = "!@#$%^&*()-_=+[]{};:,.?/"

    return lower_cases, upper_cases,numbers,symboles


def main():

    print("Welcome to our password generator !")
    generate_again = True

    while generate_again:

        password_lenght = int_input("Please enter your password lenght (must be 6-12) = ", min_lenght=6, max_lenght=12)

        lower, upper, number, symboles = character_group()

        all_characters = lower + upper + number + symboles

        password_chars = []

        for _ in range(password_lenght):

            password_chars.append(random.choice(all_characters))

        password = "".join(password_chars)

        Color.cyan(f"Here is your password ! : {password} ")
        time.sleep(2)

        generate = yes_no("Wanna generate again ? (y/n) =")

        if not generate:
            Color.green("Thank you for using our program :)")
            break

main()



