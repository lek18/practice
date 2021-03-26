input = [1,2,4,5,1,4]

#bubble sort
for i in range(len(input)):
    for j in range(i,len(input)):
        if input[j]<input[i]:
            input[j],input[i] = input[i],input[j]


#selection sort
input = [1,2,4,5,1,4]
for i in range(len(input)):
    min_index = i
    for j in range(i,len(input)):
        if input[j]<input[i]:
            min_index = j
    input[min_index], input[i] = input[i], input[min_index]
print(input)


## insertino sort
input = [1,2,4,5,1,4]
for i in range(1,len(input)):
    key = input[i]
    j=i-1
    while j>=0 and key<input[j]:
        input[j+1] = input[j]
        j-=1
    input[j+1] = key

##inserttion sort
def insertionSortRecursive(arr,n):
    if n<=1:
        return
    insertionSortRecursive(arr,n-1)
    key = arr[n-1]
    j = n-2
    while j>=0 and key<arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key

insertionSortRecursive(input,len(input))
print(input)