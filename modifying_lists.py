
def create_list(starting, ending):
    """
    Ex. create_list(4, 10) would return [4, 5, 6, 7, 8, 9, 10]
    :param starting: an integer number
    :param ending: A number greater than the starting number
    :return: list of numbers starting with the first number and going up to and including the second number
    """
    list_one = []
    for x in range(starting, (ending + 1)):
        list_one.append(x)
    return list_one

print(create_list(4, 10))


def find_odds(numbers):
    """
    Ex. find_odds([13, 2, 9, 14, 16, 18, 9, 11, 21]) would return [13, 9, 9, 11, 21]
    :param numbers: a list of numbers
    :return: a new list consisting of only the odd numbers from the original list
    """
    list_one = []
    for number in numbers:
        if number % 2 == 1:
            list_one.append(number)
    return list_one

list1 = [13, 2, 9, 14, 16, 18, 9, 11, 21]
print(find_odds(list1))


def remove_duplicates(numbers):
    """
    Ex. remove_duplicates([1, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7])  would return  [1, 2, 3, 4, 5, 6, 7]
    remove_duplicates9[‘apple’, ‘banana’, ‘banana’, ‘cherry’]) would return [‘apple’, ‘banana’, ‘cherry’]
    :param numbers:
    :return:
    """
    list_two = []
    for number in numbers:
        if number not in list_two:
            list_two.append(number)
    return list_two

list2 = [1, 2, 2, 3, 4, 4, 6, 4]
print(remove_duplicates(list2))
