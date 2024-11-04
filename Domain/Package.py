def create_package(start_date, end_date, destination, price):
    """
    :param start_date: The start date of the travel package.
    :param end_date: The end date of the travel package.
    :param destination: The destination of the travel package.
    :param price: The price of the travel package.
    :return: A dictionary containing the details of the travel package.
    """
    return [
        start_date,
        end_date,
        destination,
        price
    ]


def get_start_date(package):
    """
    :param package: A list or iterable where the first element is the start date
    :return: The start date of package, which is the first element of the input list.
    """
    return package[0]


def get_end_date(package):
    """
    :param package: A tuple where the second element represents the end date of a package.
    :return: The end date of the package, which is the second element of the input list.
    """
    return package[1]


def get_destination(package):
    """
    :param package: A list or tuple where the third element represents the destination.
    :return: The third element of the package, which is the destination.
    """
    return package[2]


def get_price(package):
    """
    :param package: A list where the fourth element (index 3) represents the price of the package.
    :return: The price of the package extracted from the provided list.
    """
    return package[3]


def set_package_start_date(packages, index, start_date):
    """
    :param packages: The list of current packages
    :param index: The index of the current package that will be set
    :param start_date: The start date of the travel package that will be set

    """
    packages[index][0] = start_date


def set_package_end_date(packages, index, end_date):
    """
    :param packages: The list of current packages
    :param index: The index of the current package that will be set
    :param end_date: The end date of the travel package that will be set

    """
    packages[index][1] = end_date


def set_destination(packages, index, destination):
    """
    :param packages: The list of current package
    :param index: The index of the current package that will be set
    :param destination: The destination of the travel package that will be set

    """
    packages[index][2] = destination


def set_price(packages, index, price):
    """
    :param packages: The list of current packages
    :param index: The index of the current package that will be set
    :param price: The price of the travel package that will be set

    """
    packages[index][3] = price
