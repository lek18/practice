# Given two sorted arrays A[], B[], find 2 indices i, j for A, B respectively such that
# abs(A[i] – B[j]) is minimized. Here abs() indicates absolute value.
# Example:
# Input: A = [1, 4, 10], B = [2, 15, 20]
# Output: (i, j) = (0, 0) (A[0] = 1, B[0] = 2)
# Input: A[] = [20, 24, 100], B[] = [2, 19, 22, 79, 800]
# Output: (i, j) = (0, 1) (A[0] = 20, B[1] = 19)


# o(n^2)

def min_val(A, B):
    # init pointers
    p1 = p2 = 0
    min_value = 2 ** 31
    output = [[0, 0]]
    while p1 < len(A):
        # print(output)
        print(p1, p2)
        val = abs(A[p1] - B[p2])

        # tracking minimum
        if val < min_value:
            min_value = min(val, min_value)
            output.pop()
            output.append([p1, p2])

        if p2 + 1 < len(B):
            if B[p2 + 1] > A[p1]:
                p1 += 1
            else:
                p2 += 1
        else:
            p1 += 1

    return output[0]


min_val([20, 24, 100], [2, 19, 22, 79, 800])