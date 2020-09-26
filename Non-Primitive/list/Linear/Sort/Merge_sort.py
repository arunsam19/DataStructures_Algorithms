def merge_sort(mylist):
    if len(mylist) > 1:
        middle = len(mylist)//2
        left = mylist[:middle]
        right = mylist[middle:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mylist[k] = left[i]
                i += 1
            else:
                mylist[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1

# Driver code
mylist = [5,9,3,6,1,8]
sorted = []

if __name__ == "__main__":
    merge_sort(mylist)