def twosum(X,target):

    mydict = {}
    output = []
    for i in range(len(X)):
        # record the difference
        diff = target - X[i]
        if diff in mydict:
            result = sorted([X[i],diff])
            if result not in output:
                output.append(result)
        mydict[X[i]] = i
    return output


twosum([1,2,4,7,5,1,5,15],6)

twosum([0, 1, 2, -1, -4], 1)

twosum([-1, 0, 1, 2, -1], 4)