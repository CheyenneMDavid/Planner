from datetime import date
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
SHEET = GSPREAD_CLIENT.open("CakesRUs")

"""
Opening screen of the terminal greets user with the "We Print You Wear"
company name.
"""

print("                ===================================\n")
print("                      Welcome to Cakes R Us \n")
print("                Happy Cake Customer always returns!\n")
print("                ===================================\n\n")


def user_name_terminal():
    """
    Request input for a single-word username with no spaces or special
    characters. The request will loop until the input is valid.
    When a valid user name is entered, the username's first letter
    is changed to a capital and returned to greet the user.
    This function is outside the main function which loops and runs everything
    else.
    """
    print("Enter a valid single-word username")
    print("Username must only consists of letters.")
    print("Spaces and special characters are not allowed.\n")
    while True:
        username = input("Enter your username: ")

        if not username.isalpha() or " " in username:
            print(
                "Please input a username that only consists of letters and "
                "has no spaces."
            )
        else:
            print("Welcome, " + username.capitalize() + "!")
            break


def get_valid_number():
    """
    Validate user input as a UK phone number, using imported regex module.
    While loop requesting input until input is valid.
    The Regex string does have short falls of coverage, but appears to be the
    most comprehensive.
    """

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


def customer_check(num):
    """
    Specify that data-type is a string.
    Remove the preceeding "0", in order for it to be matched against the Phone
    numbers column in the CSV, which doesn't store preceeding Zeros, without
    extra jiggery-pokery in the settings of google sheets.
    If a match is found, the customer first name, last name and phone number
    are displayed.  After the order function is then called.
    If no match is found, the new_customer_details function is called.
    """
    df = pd.read_csv("cakes.csv", dtype={"Phone number": str})

    if num.startswith("0"):
        num = num[1:]

    result = df[df["Phone number"].str.endswith(num)]
    if not result.empty:
        print("Current customer deails:")
        print(
            result[["First name", "Last name", "Phone number"]].to_string(index=False)
        )
        cake_order(num)
    else:
        print("This is a new customer. \n")
        print("New Customer file being started. \n")
    return num


def new_customer_details(num):
    """
    Request user input, new customer details of first name, last name,
    first line of address and postcode.
    Validate postcode using RegEx.  Loop request for valid postcode till
    valid postcode is entered and then break out of loop.
    Capitalize first and last names and change postcode to uppercase.
    Create new dictionary called "new_customer", use it to make a new
    dataframe and then use the new dataframe to update the old df.
    Save updated df to csv file.
    """

    df = pd.read_csv("cakes.csv", dtype={"Phone number": str})

    first_name = input("Enter customer first name: ")
    last_name = input("Enter customer last name: ")
    address = input("Enter first line of customer address: ")

    while True:
        postcode = input("Enter customer postcode: ")
        postcode_pattern = re.compile(
            r"^[A-Za-z]{1,2}\d{1,2}[A-Za-z]?\s?\d[A-Za-z]{2}$"
        )
        if not postcode_pattern.match(postcode):
            print("Invalid postcode format")
        else:
            break

    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    postcode = postcode.upper()
    new_customer = {
        "Phone number": num,
        "First name": [first_name],
        "Last name": [last_name],
        "First line of address": [address],
        "Postcode": [postcode],
    }

    new_df = pd.DataFrame(new_customer)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("cakes.csv", index=False)

    print("New customer details recorded. \n \n")


def cake_order(num):
    """
    Requests input from user, for cake customer wishes to order
    """
    print("Cakes available to order: \n")
    print("New Baby Girl, cost £35.00")
    print("New Baby Boy, cost £35.00")
    print("18th Birthday, cost £35.00")
    print("Wedding, £70 \n")

    cakes = {"girl": 35, "boy": 35, "18": 35, "wedding": 70}

    while True:
        cake_choice = input("What type of cake does the customer want? \n")
        if cake_choice in cakes:
            cost = cakes[cake_choice]
            cake_type = cake_choice.capitalize()
            order_date = date.today().strftime("%d-%m-%Y")
            break
        else:
            print("Invalid input, please choose a valid cake.")

    df = pd.read_csv("cakes.csv", dtype={"Phone number": str})
    df.loc[df["Phone number"] == num, "Cake type"] = cake_type
    df.loc[df["Phone number"] == num, "Order date"] = order_date
    df.loc[df["Phone number"] == num, "Cost"] = cost
    df.to_csv("cakes.csv", index=False)

    print("Order details recorded. \n \n")


def update_file(num, cost, cake_type, order_date):

    d_f = pd.read_csv("cakes.csv", dtype={"Phone number": str})
    d_f.loc[d_f["Phone number"] == num, "Cake type"] = cake_type.capitalize()
    d_f.loc[d_f["Phone number"] == num, "Order date"] = order_date
    d_f.loc[d_f["Phone number"] == num, "Cost"] = cost
    d_f.to_csv("cakes.csv", index=False)

    print("Order details recorded. \n \n")


def main():
    """
    Run all functions
    """
    num = get_valid_number()
    num = customer_check(num)
    new_customer_details(num)
    cake_order(num)


username = user_name_terminal()
"""
Function called outside main function, so that it only runs once, upon
starting the program.
"""
main()
