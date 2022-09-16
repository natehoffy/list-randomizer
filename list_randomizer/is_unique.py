def is_unique(random_element, existing_list):

    """Returns a boolean value of True if a given random element is not already in an existing list,
    and False if it is."""

    if random_element not in existing_list:
        return True
    else:
        return False
