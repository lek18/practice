def largestRectangleArea(heights):
    stack = [-1]
    maxArea = 0

    for i in range(len(heights)):
        # we are saving indexes in stack that is why we comparing last element in stack
        # with current height to check if last element in stack not bigger then
        # current element
        print(i,stack,maxArea)
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            print("Hey here",i,stack[-1])
            lastElementIndex = stack.pop()
            print("Hey",(i - stack[-1] - 1))
            maxArea = max(maxArea, heights[lastElementIndex] * (i - stack[-1] - 1))
        stack.append(i)

    # we went through all elements of heights array
    # let's check if we have something left in stack
    while stack[-1] != -1:
        lastElementIndex = stack.pop()
        maxArea = max(maxArea, heights[lastElementIndex] * (len(heights) - stack[-1] - 1))

    return maxArea



array = [2,3,4,1,5,10]
len(array)
largestRectangleArea(array)