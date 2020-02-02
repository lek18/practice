# Assume unique solution
# Given a list - determine all pair values and their index such that they sum to target
class Solution():
    def twoSum(self, input_list, target):
        difference_dict = {}  # possible difference [ values in input list] : index of possible difference
        list_size = len(input_list)
        output = []
        for i in range(list_size):
            #take the difference
            difference = target - input_list[i]
            #check if the difference is available
            if difference in difference_dict.keys():
                output = output + [[[difference,input_list[i]],[difference_dict[difference],i]]]
            difference_dict[input_list[i]]=i
        return output
