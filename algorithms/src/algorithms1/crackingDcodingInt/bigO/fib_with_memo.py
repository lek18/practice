
def fib(n,memo_array):
    memo_array[0] = 0
    memo_array[1] = 1
    if n<=0:
        return 0
    elif n==1:
        return 1
    elif memo_array[n]>0:
        return memo_array[n]
    memo_array[n] = fib(n-1,memo_array) + fib(n-2, memo_array)
    return memo_array[n]

def printallFib(n):
    memo_array=list(map(lambda x: 0, range(0,n)))
    for i in range(0,n):
        print(str(i) + ": " + str(fib(i, memo_array)))
