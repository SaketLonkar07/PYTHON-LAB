'''Write a function that given two list of elements:
a. Prints “True” if all the elements in the first list are in the second one, “False” otherwise
b. Prints the list of elements the two lists have in common. Then write a txt file containing
the list of elements just find. Write each element to a newline in the same file. Name
the file “common_elements.txt”
c. Prints the list of elements that are in the first list or in the second but not in both. Then
write a txt file containing the list of elements just find. Write each element to a newline
in the same file. Name the file “disjoint_elements.txt”
Then explain, commenting your code, the solution you proposed.'''

# first condition

List1= [1,2,3,4,5,6,7]
List2= [1,2,3,4,5,6,7,8,9,10]
check=all(item in List2 for item in List1)

if check:
    print("True,List 2 contains all the elements of the list 1")
else:
    print("False,List 2 doesn't have all the elements of the list 1")

# Second Condition

def common(a,b):
    c=[value for value in a if value in b]
    return c
d=common(List1,List2)
print(d)
with open('C:\\Users\\253289\\Desktop\\pi\\Common_element.txt', 'w') as filehandle:
    for listitem in d:
        filehandle.write('%s\n' % listitem)
# Third condition
def list_diff(list1,list2):
    out=[]
    for elements in list2:
        if not elements in list1:
            out.append(elements)
    return out
#Test input
list1= [1,2,3,4,5,6,7]
list2= [1,2,3,4,5,6,7,8,9,10]
#Run input
e=list_diff(list1,list2)
print(e)

with open('C:\\Users\\253289\\Desktop\\pi\\Disjoint_elements.txt', 'w') as filehandle:
    for listitem in e:
        filehandle.write('%s\n' % listitem)
