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


print("                ======================================\n")
print("                        快樂的客戶將永遠回來\n")
print("                Welcome to Far East Takeaway Terminal\n")
print("                  Happy Customer always returns!\n")
print("                ======================================\n\n")


def user_name_terminal():
    """
    Request input for a single-word username with no spaces or special
    characters.
    The request will loop until the input is valid.
    Change the username's first letter to capital.
    When a valid user name is entered, the user is addressed by that name.
    """
    print("Enter a valid single-word username that only consists of" "letters.")

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


def get_valid_number(num):

    pattern = re.compile(
        r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|"
        r"((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|"
        r"((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"
    )

    return pattern.match(num)
    print(num)


while True:
    num = input("Please enter a valid UK phone number: \n")
    if get_valid_number(num):
        print("Phone number is valid")
        break
    else:
        print("Invalid phone number")


def customer_check():

    df = pd.read_csv("far_east.csv")

    print(df[["Phone number"]])


# Area in which functions are called
user_name_terminal()
get_valid_number(num)
customer_check()
