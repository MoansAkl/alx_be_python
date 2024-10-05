# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and display the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now().date()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days)
    # Format and display the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
