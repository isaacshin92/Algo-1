# 1부터 12까지의 숫자를 원소로 가진 집합 A
# 집합 A의 부분 집합 중 N개의 원소를 갖고
# 원소의 합이 K인 부분집합의 개수를 출력

import sys

sys.stdin = open('sample_input.txt')


T =int(input())

for test_case in range(1, T + 1):

    # 12까지 숫자 집합     
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    # for i in range(1,13):
    #     A.append(i)

    #Main logic
    N, K = map(int,input().split()) # 부분 집합 원소의 수 N, 부분집합의 합 K
    sum_cnt = 0
    subset = [[]]


    # 부분집합 구하기
    for i in A:
        size = len(subset)
        for j in range(size):
            subset.append(subset[j] + [i])

    for sub in subset:
        temp = 0
        if len(sub) == N:
            for j in range(N):
                temp += sub[j]
            if temp == K:
                sum_cnt += 1


    print(f'#{test_case} {sum_cnt}')
    

    #  아래 코드는 문제 해석을 잘못 함, 부분집합이 아닌, 1 ~ 12까지의 수를 N개 씩 끊어 계산함.....
    # for i in range(0, len(A) -N + 1):
    #     temp = 0 

    #     for j in range(N):
    #         temp += A[i+j]
    #     print(f'temp : {temp}')
    #     if temp == K:
    #         sum_cnt += 1