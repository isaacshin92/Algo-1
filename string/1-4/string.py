# 1. 두 개의 문자열 str1과 str2가 주어진다
# 2. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
# 3. 그중 가장 많은 글자의 개수를 출력
# 

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    rlt = 0
    dict = {}
    cnt = 0


    for i in range(0, len(str1)): # dictionary 사용으로 중복 문자열 제거
         dict[str1[i]] = 0
    # print(f'dict: {dict}')
    
    for key in dict.keys():
        temp = 0
        for i in str2:
            if key == i : # str2 에서 하나씩 꺼내, key와 비교 후 value 값 증가시킨다.
                # dict[key] += 1
                temp += 1
        if cnt < temp:
            cnt = temp
    
    print(f'#{test_case} {cnt}')
        


    

