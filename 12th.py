list = [1,2,3,4,5,4,2,1,5,6,7,8,2,4,6]
res = {}
for i in list:
    if res.get(i)==None:
        res[i] = 1
    else:
        res[i] = res[i]+1


print res