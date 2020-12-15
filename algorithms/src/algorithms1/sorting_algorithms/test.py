class Solution:
    def merge2Arrays(self, left_list, right_list):
        left_cursor = right_cursor = 0
        output = []
        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                output.append(left_list[left_cursor])
                left_cursor += 1
            else:
                output.append(right_list[right_cursor])
                right_cursor += 1
        output.append(left_list[left_cursor:])
        output.append(right_list[right_cursor:])

        return output

    def merge_sort_top2bottom(self, nums):
        if len(nums) <= 1:
            return nums
        midpoint = len(nums) // 2

        left_list = self.merge_sort_top2bottom(nums[0:midpoint])
        right_list = self.merge_sort_top2bottom(nums[midpoint:])

        return self.merge2Arrays(left_list, right_list)

    def merge_sort_bottom2top(self, nums):
        pass

    def sortArray(self, nums):
        # sorting_type = "bottom2top"
        sorting_type = "top2bottom"

        if sorting_type == "bottom2top":
            return self.merge_sort_bottom2top(nums)
        else:
            return self.merge_sort_top2bottom(nums)

x = [10,9,12,3,45,1]

test1 = Solution()
test1.sortArray(x)