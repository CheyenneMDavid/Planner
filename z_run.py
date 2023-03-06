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

# print("                ===================================\n")
# print("                      Welcome to Cakes R Us \n")
# print("                Happy Cake Customer always return!!\n")
# print("                ===================================\n\n")


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


get_user_name()
