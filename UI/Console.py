def console():
    print("\n-----MENIU- <TRAVEL AGENCY>-----")
    print("1.Add travel package")
    print("2.Delete travel package")
    print("3.Search for travel package")
    print("4.Package Reports")
    print("5.Package Filtering")
    print("6.Undo package")
    print("7.Exit")
    print("\n")

def printTask1():
    print("1.1.Add travel package")
    print("1.2.Modify travel package")

def printTask2():
    print("2.1. Deleting all available travel packages for a given destination.")
    print("2.2. Deleting all travel packages with a duration shorter than a given number of days.")
    print("2.3. Deleting all travel packages with a price greater than a given amount.")

def printTask3():
    print(
        "3.1. Printing all travel packages that include a stay within a given date range (e.g., 10/08/2018 - 24/08/2018)")
    print("3.2. Printing all travel packages with a given destination and a price lower than a given amount.")
    print("3.3. Printing all travel packages with a specific end date.")

def printTask4():
    print("4.1. Printing the number of offers for a given destination.")
    print(
        "4.2. Printing all available packages within a specific period entered from the keyboard, in ascending order of price.")
    print("4.3. Printing the average price for a given destination.")

def printTask5():
    print(
        "5.1. Removing offers that have a price higher than the given one and a destination different from the one entered from the keyboard.")
    print("5.2  Removing offers that include days from a specific month.")

def print_curr_packages(packages):
    for i in packages:
        print(i)
