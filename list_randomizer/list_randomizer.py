import random  # Import the random standard library for use in order setting function
from .is_unique import is_unique


def list_randomizer(existing_list):

    """ Returns a new list of random order from an existing ordered list by selecting random elements from the existing
    list and indexing them to the new list.

    Input parameter is type list and the function returns a list.

    The function initializes an empty new list when it is called, and then for each index in the list passed as the
    function parameter a random element from the list is extracted.

    The function then checks that the random element selected from the existing list,
    isn't already added to the new list. If it isn't a unique item, another random choice is made recursively until an
    item is selected that is unique to the new list.

    Once a unique item is selected at random, it is added to the new list created within the function at the index of
    the current iterable [i]. Upon iteration completion, the function returns the new list."""

    new_list = []

    i = 0
    while i < (len(existing_list)):
        random_element = random.choice(existing_list)

        if is_unique(random_element, new_list):
            new_list.append(random_element)
            i += 1
        else:
            i = i

    return new_list
