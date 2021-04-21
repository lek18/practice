x= ["(())()"]

#function to check whether string s is a balance parenthis strings

def checkString(s):
    l=r=0
    #count =0
    for ch in s:
        # print(ch)
        # print(l)
        # print(r)
        if ch =="(":
            l+=1
        else:
            r+=1
        if r==l:
            l=r=0
    # print(l)
    # print(r)
    if l!=r:
        return False
    else:
        return True

checkString("((()(()))")