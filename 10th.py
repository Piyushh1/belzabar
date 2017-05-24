list = ['team1','teamX','team4','team5']
a = {'team1' : 'Alpha', 'team2' : 'Beta', 'team3': 'Gamma', 'team4': 'Delta' };
res = {}
for i in list:
    if(a.has_key(i)):
        res[i] = a[i];  
    //val = a.get(i,'none')
    //	if val!='none':
    // res[i]=val


print(res)