import sys

# N개의 10억 이하 자연수로 이뤄진 수열이 주어진다.
# 이 수열은 완성된 것이 아니라 M개의 숫자를 지정된 위치에 추가하면 완성된다고 한다.
# 완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split()) #수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L

    numbers = list(map(int, input().split()))

    add_list = []
    for i in range(M):
        index, value = map(int,input().split())
        numbers.insert(index, value)
    
    print(f'#{test_case} {numbers[L]}')
        



    



    

