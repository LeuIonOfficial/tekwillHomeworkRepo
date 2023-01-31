import pandas as pd

# Replace with your Google Sheets API key and the spreadsheet IDs
api_key = 'YOUR_API_KEY'
source_spreadsheet_id = 'SPREADSHEET_ID_1'
target_spreadsheet_id = 'SPREADSHEET_ID_2'

# Use pandas to read the data from the source sheet
source_data = pd.read_json(f'https://sheets.googleapis.com/v4/spreadsheets/{source_spreadsheet_id}/values/Sheet1?key={api_key}')

# Use pandas to write the data to the target sheet
target_data = source_data.to_json(f'https://sheets.googleapis.com/v4/spreadsheets/{target_spreadsheet_id}/values/Sheet1?key={api_key}')