x=[1,2,3,45,78]

def sortByEven(x):

    def func1(x,y):
        if x-y>0:
            return 1
        elif x-y<0:
            return -1

    x_copy = x
    x.sort(key=lambda y:y%2)
    #
    return x,sorted(x_copy,key= lambda x:x%2)

sortByEven(x)

from functools import cmp_to_key
def largestNumber(x):

    def func1(x,y):
        if str(x)+str(y)>str(y)+str(x):
            return 1
        else:
            return -1

    x_copy = x
    x.sort( key=cmp_to_key(lambda x,y:func1(x,y)),reverse = True)
    #
    return x,sorted(x_copy,key= cmp_to_key(lambda x,y:func1(x,y)),reverse = True )

largestNumber(x)