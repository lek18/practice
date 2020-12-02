class Solution:
    def binary_search(self,input_list,lower,upper,target):
        if upper>=lower:
            midpoint = (upper+lower)//2 # incase of odd number length list
            if target == input_list[midpoint]:
                return midpoint
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
