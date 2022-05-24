from itertools import combinations, permutations

list = [(1,2)]


for i in list :
    print(f'permutations: {list(permutations(i,2))}')