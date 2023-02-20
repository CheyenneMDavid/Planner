import datetime
import re
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("far_east")


"""
This is the opening screen of the terminal, which greets the user, reminding
them that the "Happy Customer always returns", both English and also cantonese
reminding the user to always convey an authnticity
"""
print("                ======================================\n")
print("                        快樂的客戶將永遠回來\n")
print("                Welcome to Far East Takeaway Terminal\n")
print("                  Happy Customer always returns!\n")
print("                ======================================\n\n")

df = pd.read_csv("far_east.csv")


def user_name_terminal():
    """
    Request input for a single-word username with no spaces or special
    characters.
    The request will loop until the input is valid.
    Change the username's first letter to capital.
    When a valid user name is entered, the user is addressed by that name.
    """
    print("Please enter a valid single-word username that only consists of" "letters.")

    print("Spaces and special characters are not allowed.\n")

    while True:
        username = input("Enter your username: ")

        if not username.isalpha() or " " in username:
            print(
                "Please input a username that only consists of letters and"
                "has no spaces."
            )
        else:
            print("Welcome, " + username.capitalize() + "!")
            return True


def check_new_customer():
    """
    Use input telephone number to see if customer is already listed
    """


# Area in which functions are called
user_name_terminal()
