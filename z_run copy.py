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


def get_valid_name():
    """
    Same functionvalidates both first name and last name.
    Requests user input of name (first or last) validates using RegEx string
    which allows for uppercase, lowercase, hyphens and apostrophes.
    Names are split at hyphens and apostrophes, the individual names are
    capitalized and then names are joined again.
    Result is "betty-boo" would become "Betty-Boo" and "o'brien" would
    would become "O'Brien".
    Both requests will loop until valid input is submitted.
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
            print(capitalized_first_name)
            break
        else:
            print(f"{first_name} is NOT a valid first name")
    while True:
        last_name = input("Please enter customer's last name: \n")
        if pattern.match(last_name):
            parts = last_name.split("'")
            parts = [part.capitalize() for part in parts]
            capitalized_last_name = "'".join(parts)
            print(capitalized_last_name)
            break
        else:
            print(f"{last_name} is NOT a valid last name")
    return capitalized_first_name, capitalized_last_name


def validate_address():
    """
    Request input from user, requesting entry of first line of address.
    Use Regex pattern to validate input.  The pattern allows a match using
    "flat", flat number and a letter.  For example: Flat 5b.
    Then, house number, street name, and allows for endings such as
    "drive, close, st, rd", with whitespaces where needed most.
    It's not perfect, but sufficient to avoid complexity.
    Loop until input is valid.
    """
    # RegEx pattern worked out, using: https://regexr.com/
    pattern = re.compile(
        r"^(?:flat)?\s*\d*[,_]?\s*\d+\s+[A-Za-z]+(?:\s+[A-Za-z]+)*"
    )
    while True:
        address = input("enter first line of address: \n")
        if pattern.match(address):
            print(address.title())
            break
        else:
            print(
                f"{address} is not a valid address.  Please enter a valid"
                "first line of address"
            )
    return address.title()


def validate_postcode():
    """
    Request user input for postcode.  Validation by Regex pattern
    Loop request till input is valid
    """
    pattern = re.compile(r"^[A-Za-z]{1,2}\d{1,2}[A-Za-z]?\s?\d[A-Za-z]{2}$")
    while True:
        postcode = input("Please enter a valid postcode \n")
        if pattern.match(postcode):
            print(postcode.upper())
            break
        else:
            print(f"{postcode} is an invalid format.")
    return postcode.upper()


def main():
    """
    Runs main functions
    """

    get_valid_number()
    first_name, last_name = get_valid_name()
    validate_address()
    validate_postcode()


get_user_name()
main()
