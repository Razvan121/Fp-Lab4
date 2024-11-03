from datetime import datetime

from Domain.Package import create_package


def read_date():
    """
    Reads a date in the format DD-MM-YYYY.
    :return: A datetime object representing the date.
    """
    while True:
        date_str = input("Enter date in format DD-MM-YYYY: ")
        try:
            date_obj = datetime.strptime(date_str, "%d-%m-%Y")
            return date_obj
        except ValueError:
            print("Please enter a valid date in the format DD-MM-YYYY.")


def read_destination():
    """
    Reads the destination for the travel package.
    :return: A string representing the destination.
    """
    try:
        dest_str = input("Enter destination: ").strip()
        if not dest_str:
            print("Destination cannot be empty.")
            return read_destination()
        return dest_str
    except Exception as e:
        print(f"An error occurred: {e}")
        return read_destination()


def read_price():
    """
    Reads the price for the travel package.
    :return: A float representing the price.
    """
    while True:
        price_str = input("Enter price: ")
        try:
            price = float(price_str)
            if price < 0:
                print("Price cannot be negative.")
            else:
                return price
        except ValueError:
            print("Please enter a valid numeric value for price.")


def read_sum():
    """
    Reads a sum value.
    :return: A float representing the sum.
    """
    while True:
        sum_str = input("Enter sum: ")
        try:
            total_sum = float(sum_str)
            if total_sum < 0:
                print("Sum cannot be negative.")
            else:
                return total_sum
        except ValueError:
            print("Please enter a valid numeric value for the sum.")


def read_package():
    """
    Reads a travel package including start date, end date, destination, and price.
    :return: A dictionary or custom object representing the package.
    """
    start_date = read_date()
    while True:
        end_date = read_date()
        if end_date < start_date:
            print("End date must be after the start date.")
        else:
            break
    destination = read_destination()
    price = read_price()

   # return dict(start_date=start_date, end_date=end_date, destination=destination, price=price)
    return create_package(start_date, end_date, destination, price)



def read_if_modify():
    """
    Reads the user's choice for modifying the destination or price.
    :return: "1" for destination, "2" for price.
    """
    while True:
        option = input(
            "Enter 1 to modify the destination, 2 to modify the price, 3 to modify the start date or 4 the end date: ")
        if option == '1' or option == '2' or option == '3' or option == '4':
            return option
        else:
            print("Please enter 1, 2,3 or 4")


def read_day():
    """
    Reads the number of days.
    :return: An integer representing the number of days.
    """
    while True:
        days_str = input("Enter number of days: ")
        try:
            days = int(days_str)
            if 1 <= days <= 31:
                return days
            else:
                print("Please enter a number between 1 and 31.")
        except ValueError:
            print("Please enter a valid integer for the number of days.")


def read_month():
    """
    Reads the month.
    :return: An integer representing the month.
    """
    while True:
        month_str = input("Enter month: ")
        try:
            month = int(month_str)
            if 1 <= month <= 12:
                return month
        except ValueError:
            print("Please enter a valid integer for the month.")


def read_numberpack():
    """
    Reads the number of package
    :return: An integer representing the number of package.
    """
    while True:
        package_str = input("Enter the number of package: ")
        try:
            package_number = int(package_str)
            return package_number
        except ValueError:
            print("Please enter a valid integer for the number of package.")
