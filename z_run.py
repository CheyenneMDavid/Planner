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
    """
    print("Enter a valid single-word as your username")
    print(
        "Usernames must only consist of letters and not more than 10"
        "characters long"
    )
    print("Spaces and special characters are not allowed.")
    print("Example:  'Dave' \n")

    username = input("Enter your username: ")
    if not username.isalpha() or " " in username:
        print(f"{username} is not a valid username")
        print("Please enter a username without spaces or special characters")
    else:
        print("Welcome, " + username.capitalize() + "!")


get_user_name()
