py_class = ["Allen", "Francis", "Jacob", "Julian", "Nonso", "Peter","Raina", "Scott", "Yvette"]
blank_list = []
# Loop through a list
# for name in py_class:
#     print(name + " is the best!")


# add to a list
py_class.append("Gregory")
print(py_class)
py_class[1] = "Harold"

# remove a item from a list by index
# del py_class[1]
print(py_class)

# remove a item from a list by value
if "Harold" in py_class:
    py_class.remove("Harold")
print(py_class)