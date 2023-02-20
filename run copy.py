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
This is the opening screen of the terminal, which greets the user, reminding
them that the "Happy Customer always returns", both English and also cantonese
reminding the user to convey an authnticity
"""
print("           ======================================")
print("                    快樂的客戶將永遠回來")
print("           Welcome to Far East Takeaway Terminal")
print("                 Happy Customer always returns!")
print("           ======================================")