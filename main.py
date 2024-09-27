import datetime
import calendar

# 1. Write a Python function to display the current date and time.
# 2. calculate the number of days into the year and the number of days left in the year.
def calculateDays():
    today = datetime.datetime.now().date()
    last_day_of_year = datetime.datetime(today.year, 12, 31).date()
    days_in_year = 365 if not calendar.isleap(today.year) else 366
    days_left = (last_day_of_year - today).days
    days_into_year = (today - datetime.datetime(today.year, 1, 1).date()).days
    days_to_christmas = (datetime.datetime(today.year, 12, 25).date() - today).days 
    print(f"today is: {today}")
    print(f"the last day of the year is: {last_day_of_year}")
    print(f"days in this year: {days_in_year}")
    print(f"days into year: {days_into_year}")
    print(f"days left: {days_left}")
    print(f"days to christmas: {days_to_christmas}")    
    





calculateDays()