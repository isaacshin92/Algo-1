import sys
sys.stdin = open('input.txt')
T = 10 
highest = 0
lowest = 0

for tc in range(1, T+ 1):
    
    dump_cnt = int(input())
    boxes = list(map(int,input().split()))
    
    for i in range(dump_cnt + 1):
        
        highest = max(boxes)
        lowest = min(boxes)
        boxes[boxes.index(highest)] = highest - 1 
        boxes[boxes.index(lowest)] = lowest + 1 
          
    print(f'highest: {highest}, lowest: {lowest}')
    print(f'#{tc} {highest - lowest}')

