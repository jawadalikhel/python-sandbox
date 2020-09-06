list_1 = [1,2,3,4,5,2];
print("Original List: ", list_1);

list_1.append("Six");
print("Append List: ", list_1);

newList = [7,8];
list_1.extend(newList);
print("Extend List: ", list_1);

list_1.insert(0,'ja')
list_1.insert(4,'ja')
list_1.insert(7,'ja')
print("Insert List: ", list_1);

list_1.remove(1);
print("remove List item: ", list_1);

X = list_1.pop();
print("X: ", X);
print("pop List item: ", list_1);

indexOf = list_1.index(2)
print("index of: ", indexOf);

countOf = list_1.count("ja");
print("count of: ", countOf);


list_1.clear();
print("clear list: ", list_1);



# tuple_1 = 