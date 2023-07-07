import sqlite3


# Function to create database and table
def create_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('memory_info.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create a memory table (if it doesn't exist)
    cursor.execute("""CREATE TABLE IF NOT EXISTS memory (
                        log_id integer PRIMARY KEY AUTOINCREMENT,
                        total_mem TEXT,
                        used  TEXT,
                        free  TEXT,
                        shared INTEGER,
                        buff_cache  TEXT,
                        avail TEXT,
                        datetime TEXT
                    )""")

    # Commit the changes
    conn.commit()

    # Close the database connection
    conn.close()


if __name__=='__main__':
    create_database()
    print('Database & table created!')
