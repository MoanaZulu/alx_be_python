# Exploring Python datetime module

import datetime

def show_current_datetime():
    now = datetime.datetime.now()
    print("Current date and time:", now)

def show_future_date(days):
    future = datetime.datetime.now() + datetime.timedelta(days=days)
    print(f"Date after {days} days:", future.date())

if __name__ == "__main__":
    show_current_datetime()
    show_future_date(7)


from datetime import datetime, timedelta


def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(days: int):
    """
    Calculate the future date after adding a number of days to the current date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    """Main function to interact with the user."""
    display_current_datetime()
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        if not days_input.isdigit():
            raise ValueError("Invalid input. Please enter a numeric value.")

        days = int(days_input)
        calculate_future_date(days)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
