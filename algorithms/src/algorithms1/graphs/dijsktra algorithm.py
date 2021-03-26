input = [1,2,3,4,5]

def reverse(x):
    # return x[::-1]
    i = 0
    j = len(x)-1
    while i<j:
        x[i],x[j] = x[j],x[i]
        i+=1
        j-=1
    return x


reverse(input)

# sort a list
# selection sort, insertion sort, bubble sort





