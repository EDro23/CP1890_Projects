from datetime import datetime
today = datetime(2024, 2, 15)
birthday = datetime(2024, 2, 23)
wait_time = birthday - today
days = wait_time.days
print("There are", days, "days until your birthday!")