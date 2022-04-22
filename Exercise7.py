#Given the following two dicts, print their union

d1={'a':1, 'b':2, 'c':3}
d2={'a':4, 'd':'e'}

d3=d1.copy()
#
for key,value in d2.items():
    d3[key]=value
print(d3)