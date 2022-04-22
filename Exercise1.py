# Flatten the following homogeneous list of lists using list comprehension:

list1 = [[1, 2, 3, 4], ['a', 'b', 'c'], [5, 'd']]

# Using list comprehension
flatten_list = [item for sublist1 in list1 for item in sublist1]
print(flatten_list)
