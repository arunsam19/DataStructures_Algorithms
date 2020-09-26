
def Bubble_sort(mylist):
    swapFlag = True
    l = len(mylist)
    while l > 1 and swapFlag:
        swapFlag = False
        for i in range(l-1):
            if mylist[i] > mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1] = temp
                swapFlag = True
        l = l - 1

# Driver code
mylist = [5,9,3,6,1,8]
sorted = []

if __name__ == '__main__':
    Bubble_sort(mylist)
    print('done')
