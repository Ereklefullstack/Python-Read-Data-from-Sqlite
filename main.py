import sqlite3
import pandas as pd
import os

# Specify the path of your SQLite database
database_path = os.path.abspath('path_to_your_database.db')

# Connect to the SQLite database
try:
    conn = sqlite3.connect(database_path)
except sqlite3.OperationalError as e:
    print(f"Error: {e}")
    exit()

# Retrieve the list of tables
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables_df = pd.read_sql_query(query, conn)

# Display the list of tables
print("Tables in the database:")
print(tables_df)

# Save the information of all tables to CSV files
for table_name in tables_df['name']:
    data_query = f'SELECT * FROM {table_name}'
    df = pd.read_sql_query(data_query, conn)
    csv_file_path = f'{table_name}.csv'
    df.to_csv(csv_file_path, index=False)
    print(f"Data from the table '{table_name}' has been written to '{csv_file_path}'")

# Close the connection to the database
conn.close()
