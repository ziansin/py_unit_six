# Zain Pilcher
# 1/5/23
# Function for simulating classes of 23 students and their birthdays to prove the Birthday Paradox


import random
def get_birthdays():
    """
    Creates a random assortment of birthdays with random days out of 365
    :return: the list of randomly generated birthdays of type list
    """
    birthday_list = []                                  # the blank list of birthdays
    for x in range(23):                                 # the birthday list is added to by a student's birthday 23 times
        birthday_list.append(random.randint(1, 365))    # creates a random number between 1 and 365 to determine the birthday of a student
    return birthday_list

def is_duplicates(list):
    """
    :param list: the list of birthdays from the get_birthdays function
    :return: whether there were any duplicate birthdays. true if yes, false if no
    """
    x = 0
    for day in list:
        x += 1
        for days in list[x:-1]:
            if day == days:
                return True

def main():
    while True:
        try:
            tests = int(input("How many tests do you want to run?: "))                      # asks the user how many times they want to simulate the problem
        except ValueError:
            print("Not an integer")                     # if the user input is not an integer, it will prompt the user to answer again
            continue
        if tests <= 0:
            print("Needs to be more than 0")
        else:
            break
    duplicates = 0                                      # the number of times a class of 23 students had duplicate birthdays
    for x in range(int(tests)):                         # runs as many tests as the user told
        if is_duplicates(get_birthdays()) == True:
            duplicates += 1                             # if there is a duplicate in the class, the number of classes with duplicates is increased by 1
    print(duplicates, "times there were at least two of the same birthday")
    print("It's about", round(((duplicates/int(tests)) * 100), 1), "percent of the time")     # the percentage (rounded to 3 significant figures) of times that there were duplicates birthdays out of the number of simulations ran

main()