class Solution:
    def removeDuplicates(self, nums):
        nums = list(map(lambda x: str(x), list(set(nums))))
        # nums.sort()
        b = ''.join(nums)

        return int(b)
a=[0,0,1,1,1,2,2,3,3,4]

Solution().removeDuplicates(a)

class Solution:
    def removeElement(self, nums, val):
        return len(list(filter(lambda x:x!=val,nums)))

Solution().removeElement(a,3)
len(a)

class Solution:
    def dominantIndex(self, nums):
        max_val = max(nums)
        sum_total = 0
        for index,val in enumerate(nums):
            if max_val>=2*val:
                sum_total = sum_total+1
        if sum_total == len(nums):
            return list(filter(lambda x:x[1]==max_val,enumerate(nums)))[0][0]
        else:
            return -1

Solution().dominantIndex([0,0,2,3])
max_val = max([0,0,0,1])


##finidng max counting word
class Solution:
    def mostCommonWord(self, paragraph, banned):
        # Clean String
        paragraph = paragraph.replace("!", " ").replace("?", " ").replace("\'"," ").replace(",", " ").replace(";", " ").replace(".", " ").lower()

        # removed banned words
        paragraph_list = paragraph.split(" ")

        # remove empty space ''
        paragraph_list = list(filter(lambda x:len(x)>0,paragraph_list))

        for i in banned:
            paragraph_list = list(filter(lambda x: x != i, paragraph_list))

        # Now Count?
        set_of_word = list(set(paragraph_list))
        all_counts = []
        max_val = 0
        for i in set_of_word:
            word_count = len(list(filter(lambda x: x == i, paragraph_list)))
            all_counts = all_counts + [[i, word_count]]
            if word_count > max_val:
                max_val = word_count

        # pick the max word?

        return list(filter(lambda x: x[1] == max_val, all_counts))[0][0]

paragraph = "a."
banned = ["hit"]
Solution().mostCommonWord(paragraph,banned)