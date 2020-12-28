x= ["(())()"]

#function to check whether string s is a balance parenthis strings

l=1
l=2
r=1
r=2
reset
l=1
r=1
0
l!=0

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