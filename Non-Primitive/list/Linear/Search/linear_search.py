# linear search function
def linear_search(mylist, value):
    index = 0
    foundValue = False
    while index < len(mylist) and not foundValue:
        if mylist[index] == value:
            print("Input {} found at index: {}".format(value, index))
            foundValue = True
        index += 1

# Driver code
mylist = [5,9,2,4,7,1]

if __name__ == "__main__":
    linear_search(mylist, 4)
