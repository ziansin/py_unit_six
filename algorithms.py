
def add_numbers(numbers):
    """
    Ex. add_numbers([9, 5, 11, 6, 1, 15]) returns 47
    :param numbers: a list of numbers
    :return: the sum of all the numbers in the list
    """
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum

list1 = [1, 2, 3, 4, 5, 6]
print(add_numbers(list1))

def get_max(numbers):
    """
    Ex. get_max([45, 23, 99, 34, 67, 98, 0]) returns 99
    :param numbers: a list of numbers
    :return: The largest number in the list
    """
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

list1 = [1, 2, 3, 4, 5, 6]
print(get_max(list1))

def get_min(numbers):
    """
    Ex. get_min([45, 23, 99, 34, 67, 98, 0]) returns 0
    :param numbers: a list of numbers
    :return: The smallest number in the list
    """
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

list1 = [1, 2, 3, 4, 5, 6]
print(get_min(list1))


def merge(list1, list2):
    """
    Ex. merge([3, 4, 7, 9], [1, 5, 8, 11]) return [1, 3, 4, 5, 7, 8, 9, 11]
    :param list1: a list in sorted order
    :param list2: a second list in sorted order
    :return: a single list consisting of both smaller lists combined in sorted order.
    """
    list = []
    min1 = 0
    min2 = 0
    while min1 < len(list1) and min2 < len(list2):
        if list1[min1] < list2[min2]:
            list.append(list1[min1])
            min1 = min1 + 1
        else:
            list.append(list2[min2])
            min2 = min2 + 1
    list += list1[min1:] + list2[min2:]
    return list

list_one = [1, 2, 4, 5]
list_two = [3, 6, 7, 8]
print(merge(list_one, list_two))
