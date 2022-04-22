''' Sort tuples using their first value. The resulting tuples should be sorted in reverse
 alphabetical order (solution using only python keywords are preferred):'''

tuple1 = (('k', 5), ('n', 1), ('a', 7), ('t', 6), ('j', 11))

# using reverse=True for reverse alphabetical order

result = sorted(tuple1, reverse=True)

# typecasting into tuple

result = tuple(result)
print('Sorted Tuple:', result)
