import sys 

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T + 1):
    N = int(input())
    cnt = 0          # Queen을 배치할 수 있는 가짓수 체크
    row = [0] * N    # N 크기만큼의 row -> 여기에 놓은 것을 기준으로 판단할 것
    