import csv
import sqlite3

db = sqlite3.connect('resources/weather_crash_data.db')

cursor = db.cursor()

# Check if the crash_data table exists

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name='crash_data'
""")
if cursor.fetchone() is None:
    print('Table does not exist.')
else:
    print('Table exists.')

# Get the crash data from the crash_data table
cursor.execute("SELECT * FROM crash_data")
crash_data = cursor.fetchall()
print(f"Found {len(crash_data)} records in the crash_data table.")

# Load crash_data table into a CSV file
with open('resources/crash_data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in cursor.description])
    writer.writerows(crash_data)

cursor.close()
db.close()
