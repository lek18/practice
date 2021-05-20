# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
# Example
# 1:
#
# Input: nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Example
# 2:
#
# Input: nums = [0, 1]
# Output: [[0, 1], [1, 0]]
# Example
# 3:
#
# Input: nums = [1]
# Output: [[1]]
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        def backtrack(first,n):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                # print(nums)
                nums[first], nums[i] = nums[i], nums[first]
                # print(nums)
                # use next integers to complete the permutations
                backtrack(first + 1,n)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
                # print(nums)

        n = len(nums)
        first = 0
        output = []
        backtrack(first,n)
        return output

test1 = Solution()
test1.permute(nums=["1","2","3","4"])
# test1.validCombination([1,2,2])


def toInt(x):

    i = -len(x)
    pwr = len(x)-1
    total = 0
    while i<0:
        # print(i,pwr)
        total += 10**pwr * (ord(x[i])-ord("0"))
        pwr-=1
        i+=1

    return total


toInt("100")

toInt("50563400")

ch = ":"

lwr1,upr1 = ord("0"), ord("9")
lwr2,upr2 = ord("a"), ord("z")
lwr3,upr3 = ord("A"), ord("Z")
val = ord(ch)


not ( (val >=lwr1 and val<=upr1) or (val >=lwr2 and val<=upr2) or (val >=lwr3 and val<=upr3) )