# Flattern the following heterogeneous list:

def flattenlist(object):
    gather=[]
    for item in object:
        if isinstance(item,(list,tuple,set)):
            gather.extend(flattenlist(item))
        else:
            gather.append(item)
    return gather
nestedlist=l = [35,53,(525,6743),64,63,[743,754,757]]
flattenedlist= flattenlist(nestedlist)
print(flattenedlist)
