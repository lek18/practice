class Solution(object):
    def combine(self, nums, k):
        """
        :type n: list
        :type k: int
        :rtype: List[List[int]]
        """

        def backtrack(first=0, curr=[]):
            # if the combination is done
            if k == len(curr):
                if curr[:] not in ans:
                    ans.append(curr[:])

            for i in range(first, N):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use the next integers to complete the combination
                backtrack(i + 1, curr)
                # back track
                curr.pop()


        N = len(nums)
        ans = []
        backtrack()
        return ans

test1 = Solution()
test1.combine([1,1,1,2],2)