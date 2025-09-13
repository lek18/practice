# Given an integer array arr, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
# Input: arr = [1, 0, 20, 4, 3, 0, 0, 5]
# Output: [1, 20, 4, 3, 5, 0, 0, 0]

# Input: arr = [1, 0, 2, 0, 3, 0]
# Output: [1, 2, 3, 0, 0, 0]

sample = [1, 0, 20, 4, 3, 0, 0, 5]

position = 0
for i, j in enumerate(sample):
    if j != 0:
        sample[position], sample[i] = sample[i], sample[position]
        position += 1
print(sample)

# Follow up
# Can you move the zeros to beginning of the array and keep the order.

def move_zeros_to_start(nums):
    zero_index = len(nums) - 1  # pointer for where the next zero should go
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index -= 1
    return nums


nums = [1, 0, 20, 4, 3, 0, 0, 5]
result = move_zeros_to_start(nums)
print(result)

##  Question 2

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

""" 
Example 1: 
Input: height = [1,8,6,2,5,4,8,3,7] 

Output: 49 
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. 

Example 2: 
Input: height = [1,1] 
Output: 1 
Constraints: 
n == height.length 
2 <= n <= 105 
0 <= height[i] <= 104 
"""

height = [1, 1]
left = 0
right = len(height) - 1
size = 0
while left < right:
    l = right - left
    h = min(height[left], height[right])
    size = max(size, h * l)
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(size)


## Question 3

