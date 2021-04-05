class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        mydict = {}
        #O(NKlogK)
        for i in strs:
            if "".join(sorted(i)) not in mydict:
                mydict["".join(sorted(i))] = [i]
            else:
                mydict["".join(sorted(i))].append(i)
        # O(NK)
        for anagrams in strs:
            count  = [0 for i in range(26)]
            for ch in anagrams:
                count[ord(ch)-ord("a")]+=1
            key_val = tuple(count)
            if key_val not in mydict:
                mydict[key_val] = [anagrams]
            else:
                mydict[key_val].append(anagrams)

        output = []
        for keys in mydict:
            output.append(mydict[keys])
        return output