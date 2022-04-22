'''Write a generator function that takes in input a string and returns its reverse then test it printing the reverse of
 the string: “C4E Python LAB!” '''
def rev_string(my_str):
    length=len(my_str)
    for i in range (length -1, -1 , -1):
        #when we uese yield keyword it becomes generator.
        yield my_str[i]
# for loop to reverse the string

for char in rev_string("C4E PYTHON LAB!"):
    print(char,end='')