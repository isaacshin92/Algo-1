# 이진탐색을 연습
# A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 부여

# 예를 들어 책이 총 400쪽->, 검색 구간의 왼쪽 l=1, 오른쪽 r=400이 되고, 
# 중간 페이지 c= int((l+r)/2)로 계산한다.

# 찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.

# A는 300, B는 50 쪽을 찾아야 하는 경우, 
# 다음처럼 중간 페이지를 기준으로 왼쪽 또는 오른 쪽 영역의 중간 페이지를 다시 찾아가면 된다.
# 비긴 경우는 0을출력


from re import A
import sys
from turtle import right

sys.stdin = open('sample_input.txt')


T = int(input())


def search(page_total, index):
    left = 1
    right = page_total
    cnt = 0

    while True:
        cnt += 1
        middle = int((left + right) / 2)
        if index < middle:
            right = middle 
        elif index > middle:
            left = middle 
        elif index == middle: 
            break
    return cnt 

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split()) #전체 쪽수 = P, A가 찾을 쪽수 = Pa, B가 찾을 쪽수 = Pb
    
    result ='' #결과

    a_cnt = search(P,Pa) 
    b_cnt = search(P,Pb) 


    if a_cnt > b_cnt:
        result = 'B'
    elif a_cnt < b_cnt:
        result = 'A'
    else:
        result = 0

    print(f'#{test_case} {result}')
            


  


