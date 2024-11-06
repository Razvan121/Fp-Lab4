
from Business.Package_service import modify_package, remove_packages, \
    search_packages_within_a_given_date_range, \
    search_packages_with_a_given_destination_and_a_price_lower_than_a_given_amount, \
    search_packages_with_a_specific_end_date, number_of_offers_for_a_given_destination, \
    packages_within_a_specific_period_entered_from_the_keyboard_in_ascending_order_of_price, \
    average_price_for_a_given_destination, remove_packages_within_a_month, \
    remove_packages_that_have_higher_price_and_different_destination, list_for_undo, make_copy
from Infrastructure.repo_package import add_package
from Tests.All_Tests import run_all
from UI.Console import *
from UI.Read import read_package, read_numberpack, read_date, read_destination, read_price, read_day, read_month

packages = []
undo_list = []


def meniu():
    global packages
    global undo_list
    console()

    while True:
        print("Current available packages: ")
        print_curr_packages(packages)
        print("\n")

        command = input("Enter your choice: ")
        if command == '1':
            printTask1()

            choice = input("Enter your choice for Task1: ")

            if choice == '1':
                list_for_undo(undo_list, make_copy(packages))
                new_package = read_package()
                add_package(packages, new_package)

            elif choice == '2':

                list_for_undo(undo_list, make_copy(packages))
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




        elif command == '2':
            printTask2()

            choice = input("Enter your choice for Task2: ")
            if choice == '1':

                list_for_undo(undo_list, make_copy(packages))
                destination_delete = read_destination()
                new_packages = remove_packages(packages, 'destination', destination_delete)
                packages = new_packages

            if choice == '2':

                list_for_undo(undo_list, make_copy(packages))
                days_value = read_day()
                new_packages = remove_packages(packages, 'duration', days_value)
                packages = new_packages

            if choice == '3':

                list_for_undo(undo_list, make_copy(packages))
                price_value = read_price()
                new_packages = remove_packages(packages, 'price', price_value)
                packages = new_packages

        elif command == '3':
            printTask3()

            choice = input("Enter your choice for Task3: ")
            if choice == '1':

                list_for_undo(undo_list, make_copy(packages))
                given_start_date = read_date()
                given_end_date = read_date()
                new_packages = search_packages_within_a_given_date_range(packages, given_start_date, given_end_date)

                if new_packages is not None:
                    print_curr_packages(new_packages)
                    print("\n")
                else:
                    print("No packages found")
            elif choice == '2':

                list_for_undo(undo_list, make_copy(packages))
                given_destiantion = read_destination()
                given_price = read_price()
                new_packages = search_packages_with_a_given_destination_and_a_price_lower_than_a_given_amount(packages,
                                                                                                              given_destiantion,
                                                                                                          given_price)
                if new_packages is not None:
                    print_curr_packages(new_packages)
                    print("\n")
                else:
                    print("No packages found")
            elif choice == '3':

                list_for_undo(undo_list, make_copy(packages))
                given_end_date = read_date()
                new_packages = search_packages_with_a_specific_end_date(packages, given_end_date)

                if new_packages is not None:
                    print_curr_packages(new_packages)
                    print("\n")
                else:
                    print("No packages found")

        elif command == '4':

            printTask4()
            choice = input("Enter your choice for Task4: ")

            if choice == '1':

                list_for_undo(undo_list, make_copy(packages))
                given_destiantion = read_destination()
                contor = number_of_offers_for_a_given_destination(packages, given_destiantion)
                print(f"There are {contor} offers for {given_destiantion}")

            elif choice == '2':

                list_for_undo(undo_list, make_copy(packages))
                given_start_date = read_date()
                given_end_date = read_date()
                new_packages = packages_within_a_specific_period_entered_from_the_keyboard_in_ascending_order_of_price(
                    packages, given_start_date, given_end_date)
                print_curr_packages(new_packages)
            elif choice == '3':

                list_for_undo(undo_list, make_copy(packages))
                given_destiantion = read_destination()
                average = average_price_for_a_given_destination(packages, given_destiantion)
                print(f"The average price for {given_destiantion} is {average}")

        elif command == '5':

            printTask5()
            choice = input("Enter your choice for Task5: ")

            if choice == '1':

                list_for_undo(undo_list, make_copy(packages))
                given_price = read_price()
                given_destiantion = read_destination()
                new_packages = remove_packages_that_have_higher_price_and_different_destination(packages, given_price,
                                                                                                given_destiantion)
                packages = new_packages
            elif choice == '2':

                list_for_undo(undo_list, make_copy(packages))
                given_month = read_month()
                new_packages = remove_packages_within_a_month(packages, given_month)
                packages = new_packages

        elif command == '6':

            packages = undo_list.pop()

        elif command == '7':

            print("BYE!")
            break

        else:
            print("Choose a valid option")


# run_all()
# meniu()
