
def binary_search(myli, value):
    if len(myli) == 2:
        if myli[0] == value:
            return 1
        elif myli[1] == value:
            return 2
        else:
            print('The value is not found in the list')
    while len(myli) > 2:
        middleIndex = len(myli)//2
        if myli[middleIndex] == value:
            return middleIndex
        elif value < myli[middleIndex]:
            return binary_search(myli[:middleIndex], value)
        elif value > myli[middleIndex]:
            return middleIndex + binary_search(myli[middleIndex:], value) + 1


def binary_search_new(mylist, left, right, value):
    while left <= right:
        middleIndex = int((left + right)/2)
        if mylist[middleIndex] == value:
            return middleIndex
        if value < mylist[middleIndex]:
            right = middleIndex - 1
        elif value > mylist[middleIndex]:
            left = middleIndex + 1
    if left > right:
        print('The value is not found at in the list')

#driver code
mylist = [1,4,5,8,10,11,19,20]
mylist = [1,4,5,8,10,11]
value = 11

if __name__ == "__main__":
    #foundIndex = binary_search(mylist, value)
    #print('The value is found at index: {}'.format(foundIndex))

    foundIndex = None
    foundIndex = binary_search_new(mylist, 0, len(mylist)-1, value)
    if foundIndex != None:
        print('The value {} is found at index: {}'.format(value, foundIndex))