# 버스는 0번에서 출발
# 종점인 N번 정류장까지 이동
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K

# result = 충전기가 설치된 M개의 정류장 번호를 줌, 최소한 몇 번의 충전을 해야 종점에 도착하는지 출력
# 도착할 수 없는 경우는 0을 출력


# K, N, M이 주어지고, 다음줄에 M개의 정류장 번호

import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):

    bus_stops = []
    max_charge, end_point, num_charger = map(int, input().split())

    charging_cnt = 0 # result 
    fuel = 0 # 현재 잔여 연료 
    current = 0 #버스의 현재 위치 

    for i in range(0, end_point + 1):
        bus_stops.append(0)

    #정류장에 충전기 유무 표시 . 
    for c in list(map(int, input().split())):
        bus_stops[c] = 1

    #버스 이동. 
    last_charge = 0 #최종 충전 위치. (현재 위치가 마지막 충전 장소로 돌아왔다면, 버스는 종점까지 갈 수 없음을 의미)
    current = max_charge # 일단 최대 이동 거리 이동하고 시작. 

    while current < end_point:

        if current == last_charge:
            charging_cnt = 0 # 종점까지 갈수 없음을 의미
            break

        if bus_stops[current] == 1: #버스가 도달한 곳이 충전기가 있는 곳이면. 
            last_charge = current
            charging_cnt += 1 #충전 횟수 증가. 
            current += max_charge # 또 한번 최대 거리 이동
        else: 
            current -= 1 #다시 앞으로 한칸씩 돌아가서 충전기가 있는지 확인한다. 

    result = charging_cnt
    
    
    print(f'#{test_case} {result}')


                    



