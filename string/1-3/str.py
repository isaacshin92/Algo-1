# str1 , str2 문자열 2개가 주어짐,
# str2 안에 str1과 일치하는 부분이 있는지 찾아라.

import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    temp = ''
    result = 0
    # print(f'str1: {str1}, str2: {str2}')
    # print(f'len: {len(str1)}, len: {len(str2)}')

    #slicing 
    for i in range(0, len(str2) - (len(str1)-1)):
        temp = str2[i:len(str1)+ i]
        if temp == str1:
            result = 1
    print(f'#{test_case} {result}')