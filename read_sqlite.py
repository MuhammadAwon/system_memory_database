import sqlite3


# Conenct with the database
conn = sqlite3.connect('memory_info.db')

# Create cursor object
cursor = conn.cursor()

# Write and execute query to read data from 'memory' table
query = """SELECT * FROM memory"""
cursor.execute(query)

# Fetch the result
result = cursor.fetchall()
# Display result
for row in result:
    print(row)

# Close connection
conn.close()
