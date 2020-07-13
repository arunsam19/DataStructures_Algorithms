Hash_table = [[] for i in range(10)]

def hash(key):
    return key % len(Hash_table)

def insert(Hash_table, key, value):
    hash_key = hash(key)
    Hash_table[hash_key].append(value)

def display():
    for i in range(10):
        print(i, end = " --> ")
        print(*Hash_table[i], sep = " --> ")

def printLocation(key, value):
    if Hash_table[key][0] == value:
        print("The location of the value: Index key - {}, closed  key - 0".format(key))
    else:
        for j in range(len(Hash_table[key])):
            if Hash_table[key][j] == value:
                print("The location of the value: Index key - {}, closed  key - {}".format(key, j))

#Driver code
insert(Hash_table, 5, "Chennai")
insert(Hash_table, 5, "Kanchi")
insert(Hash_table, 10, "Bangalore")
printLocation(5, "Kanchi")
display()




