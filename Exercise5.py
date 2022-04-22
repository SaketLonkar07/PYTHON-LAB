''' Build a dictionary with the same records of the following one but without
the None valued entries using conditional dictionary comprehension.'''

dict1 = {'a': 1, 'b': 2, 'c': None, 'd': 'z', 'e': None}

# By using dictionary comprehension

new_dict = {k: v for k, v in dict1.items() if v is not None}
print(new_dict)
