# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.

def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    # print(count)

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    # print(count)

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        # print("output",output)
        count[int(index % 10)] -= 1
        # print("count",count)
        i -= 1


    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    for i in range(0,n):
        arr[i] = output[i]
    # print(output)

# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *=10


# Driver code
arr = [1,2,3,33,102,20,88]

# Function Call
radixSort(arr)

for i in range(len(arr)):
    print(arr[i])

# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher
