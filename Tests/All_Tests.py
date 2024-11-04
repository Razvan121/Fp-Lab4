from datetime import datetime

from Business.Package_service import modify_package, add_package, remove_packages, \
    search_packages_within_a_given_date_range, \
    search_packages_with_a_given_destination_and_a_price_lower_than_a_given_amount, \
    search_packages_with_a_specific_end_date, number_of_offers_for_a_given_destination, \
    packages_within_a_specific_period_entered_from_the_keyboard_in_ascending_order_of_price, \
    average_price_for_a_given_destination, remove_packages_that_have_higher_price_and_different_destination, \
    remove_packages_within_a_month, make_copy, list_for_undo
from Domain.Package import create_package, get_start_date, get_destination, get_end_date, get_price

from Validation.Validation_Package import validate_package


def test_create_package():
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'London'
    price = 100.15
    package = create_package(start_date, end_date, destination, price)
    assert start_date == get_start_date(package)
    assert end_date == get_end_date(package)
    assert destination == get_destination(package)
    assert price == get_price(package)


def test_validate_package():
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 9)
    destination = 'London'
    price = 100.15
    package = create_package(start_date, end_date, destination, price)

    validate_package(package)


def test_modify_package():
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'London'
    price = 100.15
    package_list = []

    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(
        package_list,
        package)
    value = 'Paris'
    modify_package(package_list, 0, 'd', value)
    value1 = 150
    modify_package(package_list, 0, 'p', value1)
    assert value == get_destination(package_list[0])
    assert value1 == get_price(package_list[0])


def test_remove_packages_destination():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'London'
    price = 100.15

    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)

    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 230

    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)

    package_list = remove_packages(package_list, 'destination', 'Paris')

    assert len(package_list) == 1
    assert get_destination(package_list[0]) == 'London'


def test_remove_packages_duration():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'London'
    price = 100.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 7, 15)
    destination = 'Paris'
    price = 230
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)
    package_list = remove_packages(package_list, 'duration', 3)
    assert len(package_list) == 1
    assert get_destination(package_list[0]) == 'Paris'


def test_remove_packages_price():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'London'
    price = 95
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)

    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 230
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)
    package_list = remove_packages(package_list, 'price', 100)
    assert len(package_list) == 1
    assert get_destination(package_list[0]) == 'London'


def test_search_packages_within_a_given_date_range():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'London'
    price = 100.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)

    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 230
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)
    package_list = search_packages_within_a_given_date_range(
        package_list,
        datetime(2020, 6, 10),
        datetime(2020, 10, 11)
    )
    assert len(package_list) == 1


def test_search_packages_with_a_given_destination_and_a_price_lower_than_a_given_amount():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'London'
    price = 100.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 230
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)

    given_destination = 'Paris'
    given_price = 500

    add_package(package_list, package_2)
    package_list = search_packages_with_a_given_destination_and_a_price_lower_than_a_given_amount(package_list,
                                                                                                  given_destination,
                                                                                                  given_price)

    assert len(package_list) == 1


def test_search_packages_with_a_specific_end_date():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2020, 10, 11)
    destination = 'London'
    price = 100.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 230
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)
    package_list = search_packages_with_a_specific_end_date(
        package_list,
        datetime(2020, 10, 11))

    assert len(package_list) == 1


def test_number_of_offers_for_a_given_destination():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'Paris'
    price = 100.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 230
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)
    contor = number_of_offers_for_a_given_destination(package_list, 'Paris')

    assert contor == 2


def test_packages_within_a_specific_period_entered_from_the_keyboard_in_ascending_order_of_price():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'Paris'
    price = 250.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 150
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)

    start_period = datetime(2019, 1, 1)
    end_period = datetime(2025, 1, 1)
    sorted_packages = packages_within_a_specific_period_entered_from_the_keyboard_in_ascending_order_of_price(
        package_list, start_period, end_period)

    assert len(sorted_packages) == 2
    assert get_price(sorted_packages[0]) == 150
    assert get_price(sorted_packages[1]) == 250.15


def test_average_price_for_a_given_destination():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'Paris'
    price = 250.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'Paris'
    price = 150
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)
    average = average_price_for_a_given_destination(package_list, 'Paris')

    assert average == 200.075


def test_remove__packages_that_have_higher_price_and_different_destination():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'Paris'
    price = 250.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 9, 11)
    destination = 'London'
    price = 150
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)

    given_price = 155
    given_destination = 'London'

    package_list = remove_packages_that_have_higher_price_and_different_destination(package_list, given_price,
                                                                                    given_destination)
    assert len(package_list) == 1
    assert get_destination(package_list[0]) == 'London'


def test_remove_packages_within_a_month():
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'Paris'
    price = 250.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    start_date = datetime(2020, 7, 10)
    end_date = datetime(2020, 7, 11)
    destination = 'London'
    price = 150
    package_2 = create_package(start_date, end_date, destination, price)
    validate_package(package_2)
    add_package(package_list, package_2)

    given_month = 7
    package_list = remove_packages_within_a_month(package_list, given_month)
    assert len(package_list) == 1
    assert get_destination(package_list[0]) == 'Paris'


def test_undo():
    undo_list_test = []
    package_list = []
    start_date = datetime(2024, 10, 10)
    end_date = datetime(2024, 10, 11)
    destination = 'Paris'
    price = 250.15
    package = create_package(start_date, end_date, destination, price)
    validate_package(package)
    add_package(package_list, package)
    list_for_undo(undo_list_test, make_copy(package_list))
    value = 'London'
    modify_package(package_list, 0, 'd', value)
    package_list = undo_list_test.pop()

    assert get_destination(package_list[0]) == 'Paris'


def run_all():
    test_create_package()
    test_validate_package()
    test_modify_package()
    test_remove_packages_destination()
    test_remove_packages_duration()
    test_remove_packages_price()
    test_search_packages_within_a_given_date_range()
    test_search_packages_with_a_given_destination_and_a_price_lower_than_a_given_amount()
    test_search_packages_with_a_specific_end_date()
    test_number_of_offers_for_a_given_destination()
    test_packages_within_a_specific_period_entered_from_the_keyboard_in_ascending_order_of_price()
    test_average_price_for_a_given_destination()
    test_remove__packages_that_have_higher_price_and_different_destination()
    test_remove_packages_within_a_month()
    test_undo()


run_all()
