from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date  # return instead of print

def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date  # return instead of print

def main():
    # Display current date and time
    current_dt = display_current_datetime()
    print("Current date and time:", current_dt)

    # Prompt user for number of days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    future_dt = calculate_future_date(days)
    print("Future date:", future_dt)

if __name__ == "__main__":
    main()
