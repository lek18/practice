from src.algorithms1.sorting_algorithms.merge_sort_top2bottom import merge_array


def merge_sort2(x):

    output = []
    # split x into sublist of 1 element
    for i in x:
        output.append([i])

    while len(output)>1:
        #print(output)
        tracking_list = []

        for cursor in range(0,len(output)-1):
            if cursor%2==0:
                merged_arrays = merge_array(left_list=output[cursor],right_list=output[cursor+1])
                tracking_list.append(merged_arrays)
        tracking_list.extend(output[cursor+2:])
        #print(tracking_list)
        output = tracking_list
    return output[0]

x = [2,3,4,12,7,6,11,9]
merge_sort2(x)

for i in range(0,6):
    print(i)
    i = i+1
    print(i)