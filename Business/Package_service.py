from Domain.Package import get_price, get_start_date, get_end_date, get_destination, set_package_start_date, \
    set_package_end_date, set_destination, set_price
from Validation.Validation_Package import validate_package




def modify_package(package, index, choice, value):
    """
    :param package: The list of packages to be modified.
    :param index: The index of the package to be modified.
    :param choice: The attribute of the package to be modified.
        's' - start
        'e' - end
        'd' - duration
        'p' - price
    :param value: The new value to be set for the specified attribute.
    """
    if choice == 's':
        set_package_start_date(package, index, value)
    elif choice == 'e':
        set_package_end_date(package, index, value)
    elif choice == 'd':
        set_destination(package, index, value)
    elif choice == 'p':
        set_price(package, index, value)


def remove_packages(packages, choice, value):
    """
    Removes packages from the list based on specified criteria.
    :param packages: The current list of packages.
    :param choice: The removal criteria ("destination", "duration", or "price").
    :param value: The value used for comparation (destination, number of days, or price).
    :return: The list of packages after remove
    """
    if choice == 'destination':

        return list(filter(lambda package: get_destination(package) != value, packages))
    elif choice == 'duration':
        return list(
            filter(lambda package: get_end_date(package).day - get_start_date(package).day + 1 > value, packages))
    elif choice == 'price':
        return list(filter(lambda package: get_price(package) <= value, packages))


def search_packages_within_a_given_date_range(packages, start_date, end_date):
    """
      Searches for packages that fall within a specified date range.
      :param packages: The list of packages.
      :param start_date: The start date of the search range.
      :param end_date: The end date of the search range.
      :return: A list of packages that match the given date range.
      """
    return [
        package for package in packages
        if start_date <= get_start_date(package) and end_date >= get_end_date(package)
    ]


def search_packages_with_a_given_destination_and_a_price_lower_than_a_given_amount(packages, destination, price):
    """
        Searches for packages with a specified destination and price below a given amount.
        :param packages: The list of packages.
        :param destination: The desired destination.
        :param price: The maximum price.
        :return: A list of packages that match the given criteria.
        """
    return [
        package for package in packages
        if get_destination(package) == destination and get_price(package) <= price
    ]


def search_packages_with_a_specific_end_date(packages, end_date):
    """
       Searches for packages with a specified end date.
       :param packages: The list of packages.
       :param end_date: The specified end date.
       :return: A list of packages that have the given end date.
       """
    return [
        package for package in packages
        if get_end_date(package) == end_date
    ]


def number_of_offers_for_a_given_destination(packages, destination):
    """

    :param packages: The list of packages
    :param destination: The desired destination
    :return: The count of packages that have the given destination
    """
    cnt = 0

    for package in packages:
        if get_destination(package) == destination:
            cnt += 1

    return cnt


def packages_within_a_specific_period_entered_from_the_keyboard_in_ascending_order_of_price(packages, start_date,
                                                                                            end_date):
    """
    :param packages: The list of packages.
    :param start_date: The start date of the search range.
    :param end_date: The end date of the search range.
    :return: A list of packages that match the given criteria.
    """
    filtered_package = [
        package for package in packages
        if get_start_date(package) >= start_date and get_end_date(package) <= end_date
    ]

    sort_packs = sorted(filtered_package, key=lambda package: get_price(package))

    return sort_packs


def average_price_for_a_given_destination(packages, destination):
    """
    :param packages: The list of packages
    :param destination: The desired destination
    :return: The average price of the packages
    """
    sum = 0
    length = 0

    for package in packages:
        if get_destination(package) == destination:
            sum += get_price(package)
            length += 1

    if length == 0:
        return None

    average = float(sum / length)

    return average


def remove_packages_that_have_higher_price_and_different_destination(packages, price, destination):
    """
    :param packages: A list of dictionaries where each dictionary represents a package with keys including 'price' and 'destination'
    :param price: The price threshold above which packages should be removed
    :param destination: The destination that packages must match to be retained
    :return: A filtered list of packages that have a price lower than the specified price and match the specified destination
    """

    return list(
        filter(lambda package: get_price(package) < price and get_destination(package) == destination, packages))


def remove_packages_within_a_month(packages, month):
    """
    :param packages: The list of packages
    :param month: The desired month
    :return: A list of packages that match the given criteria
    """

    return list(
        filter(lambda package: not get_start_date(package).month <= month <= get_end_date(package).month, packages))


def list_for_undo(undo_list, packages):
    """
    :param undo_list: List of undo actions or states. This list will be modified by appending the current 'packages' to it.
    :param packages: The current state or package that needs to be added to the 'undo_list'.
    :return: The function does not return any value.
    """
    undo_list.append(packages)


def make_copy(packages):
    """
    :param packages: the list of packages
    :return: A copy for current list of packages.
    """
    return [el[:] for el in packages]
