

def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        key = mylist[i]
        j = i-1
        while j >= 0 and key < mylist[j]:
            mylist[j+1] = mylist[j]
            j = j-1
        mylist[j+1] = key
    print("sorted list: ", *mylist)

if __name__ == "__main__":
    li = [4,1,3,8,5,2,9]
    print("input list: ", *li)
    insertion_sort(li)
