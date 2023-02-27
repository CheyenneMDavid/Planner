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
SHEET = GSPREAD_CLIENT.open("Cupcakes")

"""
Opening screen of the terminal greets user with the "We Print You Wear"
company name.
"""

print("                ===================================\n")
print("                      Welcome to Cupcakes 2 U \n")
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
    """
    df = pd.read_csv("far_east.csv", dtype={"Phone number": str})

    if num.startswith("0"):
        num = num[1:]

    result = df[df["Phone number"].str.endswith(num)]
    if not result.empty:
        print("Current customer")
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

    df = pd.read_csv("far_east.csv", dtype={"Phone number": str})

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
    df.to_csv("far_east.csv", index=False)

    print("New customer added to file.")


def calculate_cupcake_order():
    """
    Creates a dictionary called "cupcakes" of available cupcakes and their
    prices.
    Create an empty dictionary called "order" adding the type and number of
    cupcakes the customer wants, added into it as the cupcakes dictionary
    is iterated over, asking the user to input howmany of each type is wanted.
    total_cost is is calculated by types and amounts and then addthe postage.
    Finally, print order details.

    """
    cupcakes = {
        "strawberry_shortcake": 2.50,
        "lemon_cupcakes": 2.50,
        "ultimate_nutella": 3.00,
        "chocolate_peanut_butter_frosting": 4.50,
        "coconut_cupcakes": 3.00,
        "oreo_cupcakes": 3.10,
        "salted_caramel_cupcakes": 3.10,
        "red_velvet_splodge": 4.00,
    }

    order = {}
    for cupcake_type in cupcakes:
        quantity = int(input("How many of the {} cupcakes? ".format(cupcake_type)))
        order[cupcake_type] = quantity

    total_cost = sum(
        quantity * cupcakes[cupcake_type] for cupcake_type, quantity in order.items()
    )
    total_cost += 10

    print("\nOrder Details:")
    for cupcake_type, quantity in order.items():
        print(
            "- {} x {} = £{:.2f}".format(
                quantity, cupcake_type, quantity * cupcakes[cupcake_type]
            )
        )
    print("Postage = £10.00")
    print("Total Cost = £{:.2f}".format(total_cost))


# Area in which functions are called
username = user_name_terminal()
num = get_valid_number()
num = customer_check(num)
new_customer_details(num)
calculate_cupcake_order()
