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
