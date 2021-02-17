def max_func(x):
    result = float("-inf")
    for i in range(len(x)):
        if x[i]>result:
            result = x[i]
    return result


a = [70, 250, 50, 80, 140, 12, 14]
max_func(x=a)