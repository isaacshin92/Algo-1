#N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.




import sys

sys.stdin = open('sample_input.txt')      


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    
    # bubble sort
    for i in range(n-1, 0,-1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1] , arr[j]

    result = arr[len(arr) -1] - arr[0]
    print(f'#{test_case} {result}')    