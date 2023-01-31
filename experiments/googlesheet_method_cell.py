import pandas as pd

# Replace with your Google Sheets API key and the spreadsheet ID
api_key = 'YOUR_API_KEY'
spreadsheet_id = 'SPREADSHEET_ID'

# Specify the range of the cell you want to extract
cell_range = "Декабрь'22!P7"

# Use pandas to read the data from the cell
cell_data = pd.read_json(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{cell_range}?key={api_key}')

# Print the value of the cell
print(cell_data.iat[0, 0])