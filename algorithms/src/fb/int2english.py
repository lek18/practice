class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = {0:"",1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        tens = {10:"Ten",11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

        tens2 = {20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}




        def getEnglish(x):
            """

            :param x: array of size 3 [digit1,digit2,digit3]
            :return: str - english in terms of hundred, tens and one
            """
            if x[0]!= 0:
                first_digit = ones[x[0]] + " Hundred"
            else:
                first_digit = ""

            if x[1]>1:
                second_digit = tens2[int(x[1]*10)]
                third_digit = ones[x[2]]
            elif x[1]==1:
                tens_val =  int(x[1]*10 + x[2])
                second_digit = tens[tens_val]
                third_digit = ""
            elif x[1]==0:
                second_digit = ""
                third_digit = ones[x[2]]

            return [first_digit,second_digit,third_digit]

        def addEnglishWord(input,string_val):
            ans = ""
            if len("".join(input)) > 0:
                ans += (" ".join(input) + string_val)
            else:
                ans +=("".join(input))
            return ans



        num = list(map(int,'1234567891'))
        if len(num)<=12:
            while len(num)<12:
                num.insert(0,0)
            print(num)
        #create the place holder
        i = 0
        ans = []
        while i < len(num)-2:
            val = num[i:i+3][:]
            print(i)
            print(val)

            out = getEnglish(val)
            print(out)
            if i ==0:
                ans.append(addEnglishWord(out," Billion"))
            elif i == 3:
                ans.append(addEnglishWord(out," Million"))
            elif i == 6:
                ans.append(addEnglishWord(out, " Thousand"))
            else:
                ans.append(addEnglishWord(out, ""))
            i+=3
        print(ans)
        print(num)
        print(" ".join(ans))

        return " ".join(ans)



