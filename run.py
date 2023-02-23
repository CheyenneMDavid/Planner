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
reminding the user to always convey an authenticity
"""
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


def validate_number(num):
    """
    Validate user input as a UK phone number, using imported regex module.
    While loop requesting input until input is valid.
    The Regex string does have short falls of coverage, but appears to be the
    most comprehensive when using Python as a stand alone program
    """
    pattern = re.compile(
        r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|"
        r"((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|"
        r"((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"
    )

    return pattern.match(num)

    print(num)


while True:
    num = input("Please enter a valid UK phone number: \n")
    if validate_number(num):
        print("Phone number is valid")
        break
    else:
        print("Invalid phone number")

print(f"The number you input was{num}")


def number_search():
    """
    Look for match in CSV file, Phone number column, using validated phone
    phone number from validate_number function.
    """
    df = pd.read_csv("far_east.csv")

    #
    print(df[["Phone number"]])


# Area in which functions are called:
user_name_terminal()
validate_number(num)
number_search()
