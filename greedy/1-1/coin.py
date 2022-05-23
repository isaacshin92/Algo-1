# 당신은 음식점의 계산을 도와주는 점원이다. 
# 카운터에는 거스름돈으로 사용할 500원,100원,50원,10원짜리 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야할 동전의 최소 개수를 구하라. 
# 단 N은 항상 10의 배수이다.


import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # greedy search 알고리즘임으로, 가장 적은 수의 잔돈을 주기 위해 가장 좋은 결과인, 
    # 가장 큰 동전으로 주는 것이 우선순위
    coins = [500,100,50,10] 
    change = int(input())
    cnt = 0

    for coin in coins:
        cnt += change // coin
        change %= coin
        print(f'cnt: {cnt}, change: {change}')