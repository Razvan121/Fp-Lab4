from Validation.Validation_Package import validate_package


def add_package(package, new_package):
    """
    :param package: The list to which a new package will be added.
    :param new_package: The package to be added to the list.
    """
    validate_package(new_package)
    return package.append(new_package)
