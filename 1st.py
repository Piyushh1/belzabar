res = []
list1 = input("enter list of words").split()
len = input("enter the length")
for i in list1:
    if(len(i) > len):
        continue
    res.append(i)
res.sort()
print(res)