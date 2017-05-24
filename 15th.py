a = [1, 'a', ['d','e','f',],2,-1,(1,2,3), 'g']
a = filter(lambda x: type(x) is int, a)
print a