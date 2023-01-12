# Problem 1
# Example 1: Given an array of positive integers nums
# and an integer k, find the length of the
# longest subarray whose sum is less than or equal to k.
from typing import List


# Example: nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8.


class Solution1:
    def longestSubArray(self, nums: List[int], k: int) -> int:

        # This is a sliding array solution
        left = curr = ans = 0
        N = len(nums)
        for right in range(N):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans

newSolution1 = Solution1()
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
print(newSolution1.longestSubArray(nums, k))








