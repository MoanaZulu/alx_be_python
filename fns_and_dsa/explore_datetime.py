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
