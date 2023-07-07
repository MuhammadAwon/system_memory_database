import os
import csv
import sqlite3
from csv_script import execute_cmds



# Function to process the data from csv and store in the database table
def process_data():
    try:
        # Access required file paths
        csvpath = os.path.abspath('mem_info.csv')
        cmds_jsonpath = os.path.abspath('cmds_file.json')
        
        # Execute Commands to update csv file
        execute_cmds(cmds_jsonpath)
        
        # Read csv file and store values in the list as tuple
        with open(csvpath) as f:
            csvfile = csv.reader(f, delimiter=',')
            all_values = []
            for row in csvfile:
                all_values.append(tuple(row))  # Unpack and store each value in all_values

        # Connect with memory_info.db
        conn = sqlite3.connect('memory_info.db')

        # Create cursor object
        cursor = conn.cursor()

        # Query to insert data in the 'memory' table
        insert_query = """INSERT INTO memory (total_mem, used, free, shared, buff_cache, avail, datetime) values (?, ?, ?, ?, ?, ?, ?)"""

        # Execute insert query (executemany() to process bulk query)
        cursor.executemany(insert_query, all_values)

        # Commit changes into the database
        conn.commit()

        # Close database connection
        conn.close()
        return 'Data successfully stored in the database!'
    except Exception as e:
        return f'Something went wrong: {e}'


if __name__ == '__main__':
    result = process_data()
    print(result) # Display the message whether the data is stored or not
