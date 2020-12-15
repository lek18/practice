def merge_sort(x):
    if len(x)<=1:
        return x

    midpoint = len(x)//2

    left_list = merge_sort(x[0:midpoint])
    right_list = merge_sort(x[midpoint:])

    return merge_array(left_list,right_list)


def merge_array(left_list, right_list):
    left_pointer = 0
    right_pointer = 0
    output = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer]<right_list[right_pointer]:
            output.append(left_list[left_pointer])
            left_pointer += 1
        else:
            output.append(right_list[right_pointer])
            right_pointer += 1

    output.extend(left_list[left_pointer:])
    output.extend(right_list[right_pointer:])

    return output

x = [2,3,4,12,7,6,11,9]

