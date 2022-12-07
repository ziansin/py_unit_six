def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    num = len(list_one)
    if num > 2:
        list_one = list_one[-1], list_one[1:(num - 1)], list_one[0]
    else:
        list_one = list_one[-1], list_one[0]
    list_one = str(list_one)
    list_one = list_one.replace("[", "")
    list_one = list_one.replace("]", "")
    list_one = list_one.replace("(", "[")
    list_one = list_one.replace(")", "]")
    return list_one

list1 = [1, 2, 3, 4]
print(swap(list1))

def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    num = len(list_one)
    list_one = list_one[1:(num - 1)], list_one[-1], list_one[0]
    list_one = str(list_one)
    list_one = list_one.replace("[", "")
    list_one = list_one.replace("]", "")
    list_one = list_one.replace("(", "[")
    list_one = list_one.replace(")", "]")
    return list_one

list2 = [1, 2, 3, 4]
print(rotate_left(list2))

def max_end(list_one):
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    pass # make sure to remove this line before beginning work on this function