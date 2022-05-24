# 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램
# 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.


import sys

sys.stdin = open('sample_input.txt')


def examBrackets(strList):
    temp = []
    result = 0

    for i in strList:
        if i == '{' or i == '(':
            temp.append(i)
         #닫는 괄호가 나왔을 경우
        elif i == '}' or i == ')':
            #여는 괄호가 나오기 전에 닫는 괄호가 나왔는지 체크
            if len(temp) == 0:
                result = 0
                break
            elif i == ')' and temp[-1] != '(' or i == '}' and temp[-1] != '{':
                result = 0
                break
            else:
                temp.pop()
                if len(temp) == 0:
                    result = 1
    return result


T = int(input())

for test_case in range(1, T + 1):
    tLine = list(input())
    print(f'#{test_case} {examBrackets(tLine)}')
