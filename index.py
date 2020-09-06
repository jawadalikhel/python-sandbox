# list_1 = [1,2,3,4,5,2];
# print("Original List: ", list_1);

# list_1.append("Six");
# print("Append List: ", list_1);

# newList = [7,8];
# list_1.extend(newList);
# print("Extend List: ", list_1);

# list_1.insert(0,'ja')
# list_1.insert(4,'ja')
# list_1.insert(7,'ja')
# print("Insert List: ", list_1);

# list_1.remove(1);
# print("remove List item: ", list_1);

# X = list_1.pop();
# print("X: ", X);
# print("pop List item: ", list_1);

# indexOf = list_1.index(2)
# print("index of: ", indexOf);

# countOf = list_1.count("ja");
# print("count of: ", countOf);


# list_1.clear();
# print("clear list: ", list_1);



# ########    python dictionary methods
thisDict = {
    'brand': "ford",
    'model': 'mustang',
    'year': 1964
}

copyDict = thisDict.copy()


### to get value of a key: 2ways using 1) .get() 2) bracket notion copyDict['brand']
getVal = copyDict.get('brand')
## OR
# getVal = copyDict['brand']
print("getVal: ", getVal)

## .item()

getItem = copyDict.items();
print(getItem)

getkeys = copyDict.keys();
print("getkeys: ",getkeys)

# remove element by specifieing the key
popkey = copyDict.pop('brand');
print("popkey: ",copyDict)

# remove the last element
popIte = copyDict.popitem();
print("popItem: ",copyDict)

# return value of specified key
setdef = copyDict.setdefault('model');
print("setdef: ",setdef)

updateK = {'model': 'f350'}
doUpdate = copyDict.update(updateK);
print("doUpdate: ",copyDict)

# print("thisDict: ", thisDict['brand'])