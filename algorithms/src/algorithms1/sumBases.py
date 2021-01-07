def sum_2Base3(num1,num2):
  num1_len = len(num1)
  num2_len = len(num2)

  num1 = list(map(lambda x:int(x),list(num1)))
  num2 = list(map(lambda x:int(x),list(num2)))
  # vectors
  if num1_len>num2_len:
    #add preceding zerors to num2_len
    diff= num1_len-num2_len
    vector_zeros=[0]*diff
    # modify my num2
    num2 = vector_zeros + num2
  else:
    diff= num2_len-num1_len
    vector_zeros=[0]*diff
    # modify my num1
    num1 = vector_zeros + num1

  number_ints_2_add = len(num1) # = 4
  carry_over = 0
  output = []
  for i in range(0,number_ints_2_add):
      #i=1
      i = number_ints_2_add - i -1
      sum_ints = num1[i]+num2[i]+carry_over
      stay = sum_ints%3
      carry_over = sum_ints//3
      output =  [stay] + output
  if carry_over>0:
      output = [carry_over] + output

  return "".join(map(lambda x:str(x),output))




num1="221"
num2="112"
sum_2Base3(num1,num2)

num1="2222"
num2="1122"
sum_2Base3(num1,num2)

a = [1,2,3,4]
a.extend()

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

factorial(4)

def convert2BaseN(num,base):
    quotient = num//base
    ans = [num%base]
    while quotient>0:
        remainder = quotient%base
        ans.insert(0,remainder)
        quotient = quotient//base
    #ans.insert(0,remainder)
    return ans