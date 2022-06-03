import sys
import math
sys.stdin = open('sample-input.txt')

T = int(input())

for tc in  range(1, T + 1):
    N = int(input()) + 1
    
    start = None
    home = []
    ville = []
    
    for i in range(N):
        row = list(map(int,input().split()))
        ville.append(row)
        
        for j in range(N):
            if row[j] == 1:
                home.append([i,j])
            elif row[j] == 2:
                start = [i,j]
        
        max_distance = 0
        
    for h in home:
        distance = (start[0] - h[0]) ** 2 + (start[1] - h[1]) ** 2
        max_distance = max(distance, max_distance)
    print(f'#{tc} {math.ceil(max_distance ** (1/2))}')        