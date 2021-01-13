class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        tens = {11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

        tens2 = {10:"Ten",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}

        hundreds = {}
        for key in ones:
            value = int(key*1e2)
            hundreds[value] = ones[key] + " Hundred"

        thousands = {}
        for key in ones:
            value =int(key*1e3)
            thousands[value] = ones[key] + " Thousand"

        ten_thousands = {}
        for key in tens:
            value = int(key*1e3)
            ten_thousands[value] = tens[key] + " Thousand"

        ten_thousands2 = {}
        for key in tens2:
            value = int(key*1e3)
            ten_thousands2[value] = tens2[key] + " Thousand"

        hundred_thousands = {}
        for key in ones:
            value = int(key*1e5)
            hundred_thousands[value] = ones[key] + " Hundred Thousand"

        millions = {}
        for key in ones:
            value = int(key*1e6)
            millions[value] = ones[key] + " Million"

        ten_millions = {}
        for key in tens:
            value = int(key*10e6)
            ten_millions[value] = tens[key] + " Million"

        ten_millions2 = {}
        for key in tens2:
            value = int(key*10e6)
            ten_millions2[value] = tens2[key] + " Million"

        billions = {}
        for key in ones:
            value = int(key*1e9)
            billions[value] = ones[key] + " Billion"

        place_holder_dict = {
            1 : ones,
            2 : [tens,tens2],
            3 : hundreds,
            4 : thousands,
            5 : [ten_thousands,ten_thousands2],
            6 : hundred_thousands,
            7 : millions,
            8 : [ten_millions,ten_millions2],
            9 : billions
        }

        num = '12345'
        nums = list(num)
        N = len(nums)-1
        place_holders = list(map(int,[1,10,1e2,1e3,1e4,1e5,1e6,1e9][:N+1]))[::-1]
        ans  = []
        ans_english = []
        #create the place holder
        for i in range(len(nums)):
            print(i,nums[i],place_holders[i])
            value = int(nums[i])*int(place_holders[i])
            str_value = str(value)
            ans.append(value)
            if len(str_value) not in [2,5,8]:
                dict2use = place_holder_dict[len(str_value)]
                ans_english.append(dict2use[value])
            else:
                if str_value[0]!="1" and str_value[1]!="0":
                    dict2use = place_holder_dict[len(str_value)][0] # use the tens (11,12,13,...
                    ans_english.append(dict2use[value])
                else:
                    dict2use = place_holder_dict[len(str_value)][1] # use the tens (10,20,30,...
                    ans_english.append(dict2use[value])



