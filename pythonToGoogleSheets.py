from google.oauth2.service_account import Credentials
import gspread
import pandas as pd

scope = ['https://www.googleapis.com/auth/spreadsheets']

creds = Credentials.from_service_account_file("streamlitproject-459200-ecd43e7543bb.json", scopes=scope)

gs = gspread.authorize(creds)

sheet = gs.open_by_url('https://docs.google.com/spreadsheets/d/1N9FdHxi3FH2ljvwXBWfLjiWg8FiQA065PA6y_tnFesY/edit?usp=sharing')

worksheet = sheet.get_worksheet(2)
#%%
df = pd.DataFrame(worksheet.get_all_records())