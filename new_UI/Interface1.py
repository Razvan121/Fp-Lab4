def ui_add_package(packages, new_package):
    """
    Adaugă un pachet în lista `packages` după validare.
    Dacă pachetul nu este valid, returnează 3 ca și cod de eroare.
    """

    # Extragem datele pachetului
    start_date = new_package.get('start_date')
    end_date = new_package.get('end_date')
    destination = new_package.get('destination')
    price = new_package.get('price')

    # Verificăm dacă datele au formatul corect (ca exemplu, lungime 10 pentru 'YYYY-MM-DD')
    if not (len(start_date) == 10 and len(end_date) == 10):
        print("Error: Date format should be YYYY-MM-DD.")
        return 3  # Cod de eroare pentru date invalide

    # Verificăm prețul
    if not isinstance(price, (int, float)) or price <= 0:
        print("Error: Price must be a positive number.")
        return 3  # Cod de eroare pentru preț invalid

    # Dacă toate câmpurile sunt valide, adăugăm pachetul
    packages.append(new_package)
    return packages


def ui_delete_for_given_destination(packages, destination):
    """
    Șterge toate pachetele care au `destination` specificat.
    Returnează lista actualizată.
    """
    updated_packages = [pkg for pkg in packages if pkg.get('destination') != destination]

    if len(updated_packages) < len(packages):
        print(f"Deleted packages for destination: {destination}")
    else:
        print(f"No packages found for destination: {destination}")

    return updated_packages


def ui_count_packages_for_destination(packages, destination):
    """
    Afișează numărul de pachete pentru o anumită destinație.
    """
    count = sum(1 for pkg in packages if pkg.get('destination') == destination)
    print(f"Number of packages for destination '{destination}': {count}")
    return count


def ui_print_packages_with_end_date(packages, end_date):
    """
    Afișează toate pachetele care au o anumită dată de sfârșit.
    """
    matching_packages = [pkg for pkg in packages if pkg.get('end_date') == end_date]

    if matching_packages:
        print(f"Packages with end date '{end_date}':")
        for pkg in matching_packages:
            print(pkg)
    else:
        print(f"No packages found with end date '{end_date}'")


def execute_batch_commands(commands, packages):
    for command in commands.split(';'):
        parts = command.strip().split()
        if not parts:
            continue

        cmd, args = parts[0].lower(), parts[1:]

        # Comanda `add`
        if cmd == 'add':
            if len(args) != 4:
                print("Error: Add command requires 4 arguments: start_date, end_date, destination, and price")
                continue

            try:
                start_date, end_date, destination, price = args
                new_package = {
                    'start_date': start_date.strip(),
                    'end_date': end_date.strip(),
                    'destination': destination.strip(),
                    'price': float(price.strip()),
                }

                print(f"Attempting to add package: {new_package}")
                result = ui_add_package(packages, new_package)

                if result == 3:
                    print("Error: Invalid package data. Package not added.")
                else:
                    print(f"Package added successfully: {new_package}")

            except ValueError:
                print("Error: Price must be a valid number.")
            except Exception as e:
                print(f"Error in add command: {str(e)}")

        # Comanda `delete`
        elif cmd == 'delete':
            if len(args) < 1:
                print("Error: Delete command requires 1 argument: destination")
                continue

            try:
                destination = args[0].strip()
                packages = ui_delete_for_given_destination(packages, destination)
            except Exception as e:
                print(f"Error in delete command: {str(e)}")

        # Comanda `count`
        elif cmd == 'count':
            if len(args) != 1:
                print("Error: Count command requires 1 argument: destination")
                continue

            try:
                destination = args[0].strip()
                ui_count_packages_for_destination(packages, destination)
            except Exception as e:
                print(f"Error in count command: {str(e)}")

        # Comanda `print_end_date`
        elif cmd == 'print_end_date':
            if len(args) != 1:
                print("Error: Print_end_date command requires 1 argument: end_date")
                continue

            try:
                end_date = args[0].strip()
                ui_print_packages_with_end_date(packages, end_date)
            except Exception as e:
                print(f"Error in print_end_date command: {str(e)}")

        else:
            print(f"Unknown command: {cmd}")

    return packages


def run_batch_mode():
    packages = []
    commands = input("Enter batch commands (use ';' to separate commands): ").strip()
    packages = execute_batch_commands(commands, packages)
    print("Final Packages List:", packages)

# Pentru a porni modul batch, decomentați linia de mai jos
# run_batch_mode()
