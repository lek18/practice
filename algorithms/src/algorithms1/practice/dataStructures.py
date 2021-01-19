# Stacks

stacks = [1,2,3,4,5]
stacks.append(5)

stacks

stacks.pop()
stacks

#Queues - first in first out
from collections import deque

queue = deque(stacks)
queue.append(10)

queue.popleft()
queue


## Tortoise and Hare algo!
def findDuplicates(nums):
    #First set hare and tortoise
    tortoise= nums[0]
    hare = tortoise
    while True:
        tortoise = nums[tortoise] # 1 step jump
        hare = nums[nums[hare]]   # 2 step jump
        # print("Hey tortoise",tortoise)
        # print("hey hare",hare)
        if tortoise==hare:  # stop when both meet!
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1!=ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1
findDuplicates([1,2,3,4,5,5])