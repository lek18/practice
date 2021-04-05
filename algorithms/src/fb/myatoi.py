
s = "     "
len(s)
if s[0] == " ":
    i = 0
    while s[i] == " ":
        print("hello",i)
        i += 1
        if i >=len(s):
            break
    s = s[i:]

print(s)
len(s)