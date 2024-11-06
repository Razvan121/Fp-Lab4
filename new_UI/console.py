from os import remove

from Business.Package_service import modify_package, remove_packages, search_packages_within_a_given_date_range, \
    number_of_offers_for_a_given_destination
from Domain.Package import create_package
from Infrastructure.repo_package import add_package
from UI.Console import print_curr_packages
from UI.Read import read_package, read_numberpack, read_date, read_destination, read_price
from Validation.Validation_Package import validate_package


def new_console():
    print("Add travel package")
    print("Modify travel package")
    print("Print packages")
    print("Deleting all available travel packages for a given destination.")
    print(
        " Printing all travel packages that include a stay within a given date range (e.g., 10/08/2018 - 24/08/2018)")
    print("Printing the number of offers for a given destination.")

def ui_print_packages(packages):
    print_curr_packages(packages)

def ui_add_package(packages,new_package):
    validate_package(new_package)
    add_package(packages, new_package)

def ui_modify_package(packages):
    index = read_numberpack()
    modify_choice = input("Enter your choice for modify: (possible choices : 's','e','d','p') ")

    if modify_choice == 's' or modify_choice == 'e':
        value = read_date()
        modify_package(packages, index, modify_choice, value)

    if modify_choice == 'd':
        value = read_destination()
        modify_package(packages, index, modify_choice, value)

    if modify_choice == 'p':
        value = read_price()
        modify_package(packages, index, modify_choice, value)



def ui_delete_for_given_destination(packages):
    destination_delete = read_destination()
    new_packages = remove_packages(packages, 'destination', destination_delete)
    packages = new_packages

def ui_search_within_a_given_range(packages):
    given_start_date = read_date()
    given_end_date = read_date()
    new_packages = search_packages_within_a_given_date_range(packages, given_start_date, given_end_date)

    if new_packages is not None:
        print_curr_packages(new_packages)
        print("\n")
    else:
        print("No packages found")

def ui_number_offers_for_a_given_destination(packages):
    given_destiantion = read_destination()
    contor = number_of_offers_for_a_given_destination(packages, given_destiantion)
    print(f"There are {contor} offers for {given_destiantion}")


