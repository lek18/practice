# import random
# def rand75():
#     outcome = random.randrange(0, 2) * random.randrange(0,2)
#     if outcome ==1 :
#         return 1
#     else:
#         return 0
#
#
# sum(map(lambda x:rand75(),range(0,10000)))/10000
#
#
# class Solution:
#     def _large(self, x, y):
#         if x + y > y + x:
#             return 1
#         else:
#             return -1
#
#     def mergesort(self, leftlist, rightlist):
#         leftind = rightind = 0
#         out = []
#         while leftind < len(leftlist) and rightind < len(rightlist):
#             if leftlist[leftind] + rightlist[rightind] > rightlist[rightind] + leftlist[leftind]:
#                 out.append(leftlist[leftind] + rightlist[rightind])
#                 leftind += 1
#             else:
#                 out.append(rightlist[rightind] + leftlist[leftind])
#                 rightind += 1
#         return out
#
#     def largestNumber(self, nums):
#         # return str(int("".join(sorted(map(str, nums), key=cmp_to_key(self._large), reverse=True))))
#
#         out = list(map(lambda x: [str(x)], nums))
#         print(out)
#         while len(out) > 1:
#             tracking_list = []
#             print(out)
#             for i in range(len(out) - 1):
#                 if i % 2 == 0:
#                     print("Here")
#                     sorted_val = self.mergesort(out[i], out[i + 1])
#                     last_valid_i = i
#                     tracking_list.append(sorted_val)
#             tracking_list.extend(out[last_valid_i + 2:])
#             out = tracking_list
#         print(out)
#         return out
#
# x=  [10,2,9,39,17]
# mysol = Solution()
# mysol.largestNumber(x)
# mysol.mergesort(['3'],['10'])
#
# [10,2,9,39,17]
# 210, 939,17
# 939210,17
#
# arr_size = len(arr)
# max_val = 1
# stack = [-1]
# for i in range(arr_size - 1):
#     if max_val > arr[arr_size - 1 - i]:
#         stack.append(max_val)
#     else:
#         stack.append(arr[arr_size - 1 - i])
#     max_val = max(max_val, arr[arr_size - 1 - i])
#
# return stack[::-1]
#  a
# max_cnt = 0
# for i in range(N):
#     nth_zero = 0
#     # nth_zero = 0
#     count = 0
#     for n in nums[i:]:
#         if n == 1:
#             count += 1
#         elif n == 0 and nth_zero + 1 < 2:
#             count += 1
#             nth_zero += 1
#         elif n == 0 and nth_zero + 1 > 1:
#             # reset the count
#             count = 0
#             nth_zero = 0
#         # print(count,i,nth_zero)
#         max_cnt = max(count, max_cnt)
#
# return max_cnt