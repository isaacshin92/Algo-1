import sys
from itertools import combinations, permutations

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    ingredients = int(input())
    synergy = []

    for i in range(ingredients):
        synergy.append(list(map(int,input().split(' '))))
    # combinations 함수를 통해, subset을 구함 -> 두번째 인자로 ingredients//2를 넘겼음으로, 주어진 재료의 반
    aa = list(combinations(range(ingredients-1), ingredients//2))
    bb = []
    cc =[]
    for i in aa:
        bb.append(tuple(set(range(ingredients)) - set(i)))
        # set(range(ingredients))의 결과값 ex (0,1,2,3)... 에서 - set(i)_ (0,1)과 같이 aa에 있는 값을 뺌으로, 중복 X
        cc.append(list(permutations(i,2))) #각 조합마다, 순열을 구한다. (순열은 같은 요소여도 순서가 다르면 다른 배열로 친다.)
    dd = []
    for i in bb:
        dd.append(list(permutations(i,2)))
 
    rlt = 987654321
    a_synergy, b_synergy = 0, 0

    for i in range(len(cc)):
        for j in range(len(cc[i])):
            a_synergy += synergy[cc[i][j][0]][cc[i][j][1]]
            b_synergy += synergy[dd[i][j][0]][dd[i][j][1]]

        if abs(a_synergy - b_synergy) <= rlt:
            rlt = abs(a_synergy - b_synergy)
            a_synergy, b_synergy = 0, 0 
        else:
            a_synergy, b_synergy = 0, 0 
    print(f'#{test_case} {rlt}')






