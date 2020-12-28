
def partition(array, low,high):
    i = low-1
    pivot = array[high]

    for j in range(low,high):
        if array[j]<pivot:
            # increase the value of i by 1
            i+=1
            array[i],array[j] = array[j], array[i]

    array[i+1],array[high] = array[high],array[i+1]

    return i+1


def quicksort(array,low,high):
    if low<high:
        #get the index of partition where item is placed in its right place
        pi = partition(array,low,high)

        #repeat
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

x= [12,3,4,51,1]
quicksort(x,0,len(x)-1)
x