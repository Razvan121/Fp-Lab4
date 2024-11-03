from Domain.Package import get_price, get_destination, get_start_date, get_end_date


PACKAGE_PRICE_ERR = "Package price cannot be negative or zero."
DESTINATION_ERR = "Destination cannot be empty."
START_DATE_ERR = "Start date cannot be empty."
END_DATE_ERR = "End date cannot be empty."


def validate_package(package):
    error_messages = []

    def add_error(condition, message):
        if condition:
            error_messages.append(message)

    add_error(get_price(package) <= 0, PACKAGE_PRICE_ERR)
    add_error(get_destination(package) == "", DESTINATION_ERR)
    add_error(get_start_date(package) == "", START_DATE_ERR)
    add_error(get_end_date(package) == "", END_DATE_ERR)

    if error_messages:
        raise ValueError("There are errors in the package:\n" + "\n".join(error_messages))
