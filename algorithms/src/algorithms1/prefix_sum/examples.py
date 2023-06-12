# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
# return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
#
# For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13,
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].12
from typing import List


def prefix_sum(x: List[int])->List[int]:

    sum = 0
    output = []
    for a in x:
        sum+=a
        output.append(sum)

    return output

prefix_sum(x= [1, 6, 3, 2, 7, 2])

def solution(nums: List[int], queries:List[List[int]], limit:int) ->List[bool]:

    # construct the prefix sum
    prefix_sum_holder = prefix_sum(nums)
    output=[]
    for i,j in queries:

        if i == 0:
            output.append(prefix_sum_holder[j] <= limit)

        else:
            output.append(prefix_sum_holder[j]-prefix_sum_holder[i-1]<=limit)

    return output

solution(nums=[1, 6, 3, 2, 7, 2], queries=[[0, 3], [2, 5], [2, 4]] , limit = 13)
