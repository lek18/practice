class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        idea is to find the index i and index i+1 where and nums[i]<nums[i+1]
        then from index i+1 to len(nums) find the lowest upper bound index and swap it with i
        any element from index i+1 to len(nums) get reversed.

        """

        # search for first item right to left that is < its right element
        found = False
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                found = True
                break
            i -= 1  # decrease our i from right to left
        # print(i,found)
        if not found:  # nothing happend return sorted num
            nums.sort()
        else:
            lower_bound_index = self.getLowerBound(i + 1, nums, nums[i])
            # swap the elements
            nums[i], nums[lower_bound_index] = nums[lower_bound_index], nums[i]
            # reverse elements from i+1
            nums[i + 1:] = nums[i + 1:][::-1]

    def getLowerBound(self, st_index, nums, target):
        # lower_bound_index = st_index

        for i in range(st_index, len(nums)):
            if nums[i] > target and nums[i] <= nums[st_index]:
                lower_bound_index = i
        return lower_bound_index
