class Solution:
    def binary_search(self,input_list,lower,upper,target):
        if upper>=lower:
            midpoint = (upper+lower)//2 # incase of odd number length list
            if target == input_list[midpoint]:
                return 1
            elif target<input_list[midpoint]:
                upper = midpoint-1
                return self.binary_search(input_list,lower,upper,target)
            else:
                lower = midpoint + 1
                return self.binary_search(input_list,lower,upper,target)
        else:
            return -1
x = [1,4,35,50,60]
Solution().binary_search(x,0,len(x)-1,4)


def bSearch( arr, low, high, target):
    if high >= low:
        midpoint = (low + high) // 2
        if target < arr[midpoint]:
            return bSearch(arr, low, midpoint - 1, target)
        elif target > arr[midpoint]:
            return bSearch(arr, midpoint + 1, high, target)
        elif target == arr[midpoint]:
            return True
    return False

x = [7,1,14,11]
bSearch(x,0,len(x)-1,7)
