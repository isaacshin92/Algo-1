import sys

sys.stdin = open('sample_input.txt')

T = int(input())

# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
for tc in range(1, T + 1):
    N, S = input().split()
    ten=int('0x' + S, 16) # 16 -> 10
    # print(f'ten: {ten}')
    b = format(ten,'b') # 10 -> 2
    if len(b) < int(N) * 4: # 첫자리가 0인경우 
        # print(type(b))
        
        # print(f'b : {b}')
        # print(f'len(b) : {len(b)}')
        b = '0' + b
 
    print(f'#{tc} {b}')
    
    
