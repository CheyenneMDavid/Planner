import re
import pandas as pd
import gspread
from google.oauth2.service_account import (
    Credentials,
)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("CakesRUs")


orders = SHEET.worksheet("orders")

data = orders.get_all_values()

# print(data)

df = pd.read_csv("cakes.csv")

# print(df)

"""
Opening screen of the terminal greets user with the "Cakes RUs"
company name.
"""

print("                ===================================\n")
print("                      Welcome to Cakes R Us \n")
print("                Happy Cake Customer always return!!\n")
print("                ===================================\n\n")


def get_user_name():
    """
    Request input for a single-word username with no spaces or special
    characters.
    Request input for a single-word username with no spaces or special
    characters. The request will loop until input is valid.
    When a valid user name is entered, the username's first letter
    is changed to a capital and returned to greet the user.
    """
    print("Enter a valid single-word username")
    print("Username must only consists of letters.")
    print("Spaces and special characters are not allowed.\n")
    while True:
        username = input("Enter your username: \n")

        if not username.isalpha() or " " in username:
            print(f"{username} is not a valid username.")
            print(
                "Usernames must be a single word, consisting only of letters."
                "Example: 'Trudie' or 'Dave': \n"
            )
        else:
            print("Welcome, " + username.capitalize() + "!")
            break


def get_valid_number():
    """
    Request for user input of a valid UK phone number. Validate with RegEx
    pattern which will contine to loop until a valid input it entered.
    """
    # The Regex pattern for this code is from the StackOverflow site, here:
    # https://stackoverflow.com/questions/11518035/regular-expression-for-
    # gb-based-and-only-numeric-phone-number
    pattern = re.compile(
        r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|"
        r"((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|"
        r"((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"
    )

    while True:
        num = input("Please enter a valid UK phone number: \n")
        if pattern.match(num):
            print(f"Thank you, {num} is a valid phone number")
            return num
        else:
            print(f"{num} is an invalid phone number")


def get_valid_first_name():
    """
    Requests user input and uses RegEx to validate.  Pattern allows for upper
    and lowercase letters, hyphens and apostrophies.
    PProcess is looped with an "invalid entry" statement until input is valid.
    If present, names are split at the hyphen into two seperate names,
    capitalized and then joined again.
    """
    pattern = re.compile(
        r"^[A-Za-z][A-Za-z'-]+[a-z](,? [A-Z][A-Za-z'-]+[a-z])*$"
    )
    # The Regex pattern for this code is from the StackOverflow site, here:
    # https://stackoverflow.com/questions/39895282/improving-the-below-regex-
    # for-us-and-uk-names
    # I changed it and tested the change her: https://regexr.com/

    print(
        "When entering customer's name, hyphens and apostrophes are allowed,"
        "but spaces are not. \n"
    )
    while True:
        first_name = input("Please enter customer's first name: \n")
        if pattern.match(first_name):
            parts = first_name.split("-")
            parts = [part.capitalize() for part in parts]
            capitalized_first_name = "-".join(parts)
            print(f"{first_name} is a valid name")
            print(capitalized_first_name)
            return
        else:
            print(f"{first_name} is not a valid first name")


def get_valid_last_name():
    """
    Requests user input and uses RegEx to validate.  Pattern allows for upper
    and lowercase letters, hyphens and apostrophies.
    Process is looped with an "invalid entry" statement until input is valid.
    If present, names are split at the apostraphe into two seperate names,
    capitalized and then joined again.
    """
    pattern = re.compile(
        r"^[A-Za-z][A-Za-z'-]+[a-z](,? [A-Z][A-Za-z'-]+[a-z])*$"
    )
    # The Regex pattern for this code is from the StackOverflow site, here:
    # https://stackoverflow.com/questions/39895282/improving-the-below-regex-
    # for-us-and-uk-names
    # I changed it and tested the change her: https://regexr.com/

    while True:

        last_name = input("Please enter customer's last name: \n")
        if pattern.match(last_name):
            parts = last_name.split("'")
            parts = [part.capitalize() for part in parts]
            capitalized_last_name = "'".join(parts)
            print(f"{last_name} is a valid name")
            print(capitalized_last_name)
            return
        else:
            print(f"{last_name} is not a valid first name")


get_user_name()

get_valid_number()
get_valid_first_name()
get_valid_last_name()
