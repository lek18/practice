def csort(x):
    # if empty return None
    if len(x)==0:
        return None
    if len(x)==1:
        return x

    # first find the max value of the array
    k = x[0]
    for i in x[1:]:
        k = max(k,i)

    # create an array of size k
    aux_array = [0 for i in range(k+1)]

    # store the frequencies of each value of x in aux_array:

    for i in x:
        aux_array[i]+=1

    # save result in sorted_array val

    sorted_array = []
    for i in range(k+1):
        sorted_array.extend([i for j in range(aux_array[i])])

    return sorted_array

x = [6,5,3,1,4,5,4]
csort(x)