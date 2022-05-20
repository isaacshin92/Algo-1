# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력


import sys

sys.stdin = open('sample_input.txt')


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list()

    for i in range(N):
        numbers.append(input())