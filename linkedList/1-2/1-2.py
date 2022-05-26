# 여러 개의 수열을 정해진 규칙에 따라 합치려고 한다

import sys

sys.stdin = open('sample_input.txt')

# def combine(a, b):
#     insertIndex = 0

#     for i in range(len(combi)):
#         if combi[i] < b and i == len(combi) - 1:
#             insertIndex = len(combi)
#             break

#         elif b < combi[i]:
#             insertIndex = i
#             combi = combi + newList[0]
#             break
    
#     for i in range(n_len):
#         combi.insert(insertIndex+i, newList[i])

T = int(input())

for test_case in range(1, T + 1):
    n_len, n_cnt = map(int,input().split()) #수열의 길이 N, 수열의 개수 M, 

    combi = list(map(int,input().split()))

    for i in range(n_cnt -1):
        newList = list(map(int,input().split()))
        firstNum = newList[0]

        # for i in range(len(combi)):
        for idx, v in enumerate(combi):
            if v > firstNum:
                combi[idx:idx] = newList
                # print(f'{test_case}1st combi : {combi}')
                break
        else:
            combi.extend(newList)

    # print(f'combi = {combi}')
    combi.reverse()
    if len(combi) > 9:
        combi = combi[:10]
  
    print(f"#{test_case} {' '.join(map(str, combi))} ")




