# 0에서 9까지 숫자가 적힌 N장의 카드
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력
#  카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
import sys 


sys.stdin = open('sample_input.txt')


T = int(input())
for test_case in range(1, T + 1):
    card_num = int(input())
    cards =list(input())
    
    
    #버블 정렬을 통해 정렬. 시험에서는 sort() 사용...!
    for i in range(card_num- 1, 0, -1):
        for j in range(0, len(cards)-1):
            if cards[j] > cards[j + 1]:
                cards[j], cards[j + 1] = cards[j + 1], cards[j]
    
    #가장 많은 
    card_cnt = 0
    max_card = 0

    
        #Count 함수 사용 해결 

    for i in cards: 
        if card_cnt < cards.count(i): #비교하는 다음 카드가 이전 카드의 갯수보다 클 경우
            card_cnt = cards.count(i) # 카드 갯수에 현재 비교되는 카드의 갯수 할당
            max_card = i # 현재 비교되는 카드를 가장 많은 갯수의 카드로 할당
        elif card_cnt == cards.count(i): #이전에 비교한 카드와 비교되는 카드의 갯수가 동일할 경우 i번째 카드가 더 큰 숫자 해당 카드를 결과로 할당
            max_card = i 
    
    print(f'#{test_case} {max_card} {card_cnt}')


    
