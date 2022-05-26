import sys
from queue import Queue

# sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    que = Queue()

    numbers = list(map(int,input().split()))

    for num in numbers:
        que.put(num)
    

    for i in range(M):
        que.put(que.get())
    
    print(f'#{test_case} {que.get()}')

    

        
