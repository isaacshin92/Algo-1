import sys

sys.stdin = open('sample_input.txt')


T = int(input())

for test_case in range(1, T + 1):
    #1일, 1달 3개월 1년
    day, month, threeMon, year = map(int, input().split())
    days = [1,31, 93, 365]
    total = 0
    plan = list(map(int,input().split()))
    total_day = sum(plan)
    max_price = year
    
    while total_day >= 0:
        for day in days:
            
    
        
    
    