# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬

import sys

sys.stdin = open('sample_input.txt')


T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # number of decimal
    arr = list(map(int, input().split()))
    new_list = list()
    result = list()

    #sorting 
    for i in range(len(arr) -1, 0 ,-1):
        for j in range(len(arr) -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1] , arr[j]
    
    # print(f'N : {N}, arr : {arr}')
    for i in range(0, N//2):

        high = arr[len(arr) -1]
        new_list.append(str(high))
        arr.remove(arr[len(arr) -1])

        low = arr[0]
        new_list.append(str(low))
        arr.remove(arr[0])

    for i in range(10):
        result.append(new_list[i])

    print(f"#{test_case} {' '.join(result)}")
    # print(f'arr[0] : {arr[0]}')
    # print(f'arr[len(arr) -1] : {arr[len(arr) -1]}')

