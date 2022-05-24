# 가로x세로 길이가 10x20, 20x20인 직사각형
# 20xN 크기의 직사각형에 준비한 종이를 빈틈없이 붙이는 방법
# 10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램

# result  = (n-1) + (n-2)
import sys
sys.stdin = open('sample_input.txt')

def function(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        return function(n-1) + (function(n-2)*2)
T = int(input())

for test_case in range(1, T + 1):   
    N = (int(input())) //10
    print(f'#{test_case} {function(N)}')

