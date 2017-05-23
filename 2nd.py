a = [int(x) for x in input().split()]
res = []
for i in a:
    if(i%5==0 and i!=0):
        res.append(i)
res.sort();
print(res);
