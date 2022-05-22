
t = [1,2,3,4,5,6,7,8,9]
f = [[]]

a = list()

for num in t: 
    size = len(f)
    print(f'num: {num}')    
    for i in range(size):
        f.append(f[i] + [num])
        print(f'f: {f}')


