import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pyodbc

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\isbakhullail\\Documents\\INTERVIEW_MINING\\End To End Pipeline Multi Source To Data WareHouse\\gsheetsourceinterviewmining-5d3b76bed363.json', scopes=scopes)
file = gspread.authorize(creds)
workbook = file.open('DATA_SOURCE_TRAINING_HISTORY')
sheet = workbook.sheet1
data = sheet.get_all_values()
data_without_header = data[1:]

#Membuat Koneksi di SQL Server 

# Replace the values in the connection string with your SQL Server credentials
server = 'LAPTOP-RR6QESQB\MSSQLSERVERBACUL'
database = 'AdventureWorksDW2012'
username = 'ETLPROJECT'
password = 'ETLBACUL'
driver = '{ODBC Driver 17 for SQL Server}'  # Make sure the appropriate driver is installed

# Create the connection string
connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Connect to the SQL Server
conn = pyodbc.connect(connection_string)
print('connection succes')

#insert table
# Assuming your list and table have the same number of columns
table_name = 'DATA_SOURCE_TRAINING_HISTORY'

# Prepare the SQL query
num_columns = len(data_without_header[0])  # Assuming all rows in the list have the same number of elements
sql_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * num_columns)})"

#EKESEKUSI
# Create a cursor to execute the query
cursor = conn.cursor()

# Execute the insertion query with executemany to insert all rows at once
cursor.executemany(sql_query, data_without_header)

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
print('DATA BERHASIL DI INSERT')
