import time
import schedule
from main import process_data


# Function to schedule data storage
def schedule_data():
    # Call process_data function from main.py
    result = process_data()
    print(result)

# Schedule the job to run every minute
schedule.every(1).minutes.do(schedule_data)
print("Scheduler is running...")

# Keep the script running to execute scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
