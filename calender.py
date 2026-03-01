# calendar

import calendar
from datetime import date

# Ask user for date in DD-MM-YYYY format
user_input = input("Enter date (DD-MM-YYYY): ")
try:
    # Split and convert to integers
    day, month, year = map(int, user_input.split('-'))

    # Find the day of the week first to validate the date
    day_name = calendar.day_name[date(year, month, day).weekday()]

    # Display the calendar for that month
    print(f"\nHere is the calendar for {calendar.month_name[month]} {year}:\n")
    print(calendar.month(year, month))

    print(f"The date {day:02d}-{month:02d}-{year} falls on a {day_name}.")

except ValueError:
    print("\nError: Invalid date or format. Please use DD-MM-YYYY format and enter a valid date.")
