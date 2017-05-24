a1 = {'team1' : 'Alpha', 'team2' : 'Beta'}
a2 = {'team3': 'Gamma', 'team4': 'Delta' };
res = {}
res = dict(a1.items() + a2.items())
print(res)
