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
SHEET = GSPREAD_CLIENT.open("far_east_takeaway")


"""
These global variable are the set prices for set meals.  Thee are no other
meals available, however a customer can order any number or cobimnation of
these.
"""
SET_MEAL_FOR_ONE = 8.50

SET_MEAL_FOR_TWO = 25.80

SET_MEAL_FOR_THREE = 33.20

SET_MEAL_FOR_FOUR = 42.80





printSet Meal For 1 Person
Vegetarian Spring Rolls (6)
Sweet & Sour Chicken Hong Kong Style
Egg Fried Rice


# def hr_terminal():
#     """
#     Request input: username spaces or special characters.
#     Change username, first letter to capital. With loop, until input is valid.
#     """
#     print(
#         "Please enter a valid user name which only consists of letters. "
#         "Spaces and special characters are not allowed...\n"
#     )
#     while True:
#         username = input("Enter your username: \n")

#         if username.isalpha() is False:
#             print("Please input a user name which only consists of letters.")
#             print("Spaces and special characters are not allowed...\n")
#         else:
#             print("Welcome " + username.capitalize())
#             break
#     return False


# def choose_task():
#     """
#     Request user to choose from two different tasks, by entering 1 or 2.
#     1 is to register a new employee. 2 is to book staff holiday.
#     The loop will repeatedly ask the user to select 1 or 2.
#     """
#     while True:
#         print("New staff records, select '1', then 'ENTER'")
#         print("For staff holidays, select '2', then 'ENTER' \n")

#         choice = int(input("Please make your selection: \n"))
#         if choice == 1:
#             get_valid_fullname()
#             break
#         elif choice == 2:
#             print("Place holder to run: attendance_records function")
#             return False


# def get_valid_fullname():
#     """
#     Request user input, new staff's full name. No special characters.
#     Return with Capital letter start to each word.
#     RegEx code for this function borrowed from this site:
#     https://bobbyhadz.com/blog/python-input-only-letters-allowed
#     """
#     print("Input new staff's full name, seperated by spaces.")
#     print("Names must only consist of letters and spaces.")
#     print("Special characters are not allowed...\n")

#     nam = ""
#     while True:
#         nam = input("Please input new staff's fullname: \n")
#         if not re.match(r"^[a-zA-Z\s]+$", nam):
#             print("Special charater are not allowed.")
#             continue
#         return nam.title()

#     return False


# def get_valid_number(num):
#     """
#     Validate user input as a UK phone number, using imported regex module.
#     While loop requesting input until input is valid.
#     The Regex string does have short falls of coverage, but appears to be the
#     most comprehensive when using Python as a stand alone program
#     """
#     pattern = re.compile(
#         "^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|'\
#         '((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|'\
#         '((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"
#     )

#     return pattern.match(num)


# while True:
#     num = input("Please enter a valid UK phone number:  \n")
#     if get_valid_number(num):
#         print("Phone number is valid")
#         break
#     else:
#         print("Invalid Phone number")


# def line_compiler():
#     """
#     Gathers returns from functions to information for staff list
#     """


# def main():
#     """
#     Run all program functions.
#     **Note to self**  Functions running in wrong order!
#     **Sort out and remove his reminder!
#     """
#     hr_terminal()
#     choose_task()
#     get_valid_fullname()
#     get_valid_number(num)


# main()
