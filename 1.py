import gspread
from oauth2client.service_account import ServiceAccountCredentials
#from google.oauth2.service_account import Credentials
import json



gc = gspread.service_account(filename="./credentials.json")
sh = gc.open("api2025")
print(sh.sheet1.acell('A1').value)

