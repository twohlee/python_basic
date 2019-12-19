GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = True

if not IS_DEV_MODE: # release 버전의 코드가 작동
    # step1
    print( "Enjoy Custom Game world" )
    # step2 
    while True:
        
        tmp = input("게임 제목을 입력하시오, 단 {}자 이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    print( 'gameTitle', gameTitle )
    # step 3
    while True:
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            break
    # step4
    while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')
            continue
        if not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue    
        game_level = tmp
        break
else: # test or dev(개발) 버전으로 코드가 작동 
    # 매번 입력받아서 테스트하기엔 시간이 많이 소요되므로, 값을 고정하여 개발
    gameTitle   = 'testgame'
    player_name ='guest'
    game_level  = 1

# step 5
print( '-'*20 )
print( '현재 까지 입력 상황' )
print( 'gameTitle',   gameTitle )
print( 'player_name', player_name )
print( 'game_level',  game_level )
print( '-'*20 )


# step 6
# 인트로 
'''
=========================================
+           게임제목(중앙정렬)            +
+                lv레벨값                +
+         "플레이어 이름"의 연대기        +
=========================================
             press any key!!
'''
'''
print('='*40)
print('+{0:^38}+'.format(gameTitle))
print('+{0:^38}+'.format('lv : %s' % game_level))
print('+{0:^34}+'.format('%s의 연대기' % player_name))
print('='*40)
print('{0:^40}'.format('press any key!!'))
'''
#step 7
# 카드 게임
# 트럼프 카드의 종류는 4타입, 타입별로 13장의 카드가 존재한다.
# A는 합산값의 * 2을 한다 >> 예를 들어 A, 3 => (1,3) *2 = 8점
# J = 11, Q = 12, K = -5
 
'''
Tip : 13*4 중 8장만 뽑고 나머진 다 버려도 무방

♤ : A, 2~10, J, Q, k 
♡ : A, 2~10, J, Q, k 
♧ : A, 2~10, J, Q, k 
◇ : A, 2~10, J, Q, k 

'''



# 전체 룰
# 1. 게임이 시작하면 카드를 섞는다. >> 셔플 >> random 모듈을 활용(외장함수, 구현을 위해서 사용)
# 2. 카드를 순서대로 나 한장(0), 컴퓨터 한장(1), 나 한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
# >> 
# 3. 플레이어는 최대 2장까지 더 받을 수 있다
# 3-1.   다시 나 한장(4,6), 컴퓨터 한장(5,7) >> 최대 2번까지 가능
# 4. 승패 >> 내가 가진 카드 중 최대값 2개를 합산해서, 특별 기능이 있다면 추가 계산하여 높은 쪽이 승리한다.
# 5. 한번에 이기면 ((내 카드의 합 - 컴퓨터 카드의 합)*100), 카드를 한 번 받으면 20점씩 깐다.
# 6. 카드를 받으면 카드를 더 받겠습니까? 아니면 승부를 내겠습니까? 
# 7. 다시 하시겠습니까? yes => 다시 1번 부터 시작
# 7-1. no => game over!! 출력하고 게임 종료
# A는 합산값의 * 2을 한다 >> 예를 들어 A, 3 => (1,3) *2 = 8점
# J = 11, Q = 12, K = -5

'''

import random


card = random.choice(['A', 2,3,4,5,6,7,8,9,10, 'J', 'Q', 'k'])

'''

# '1'.is

'''
#랜덤 및 셔플 테스트
import random
ori_data [1,2,3,4,5]
target_data = ori_data[:]
# 난 항상 일정하게 섞이는 값을 원한다 >> 난수가 항상 일정하게 나온다. >> seed 고정하면 됨
random.seed(1) # seed를 고정하면 난수가 나오는 순서가 동일 >> 항상 일정한 결과를 낼 수 있다.
# 일정한 결과를 내면 >> 항상 같은 결과가 나오는 실험 환경을 구축할 수 있다.
# 변수를 바꿔가면서 영향성 등을 분석할 수 있다.
# 씨드를 고정하지 않으면 >> 현재 시간이 씨드가 된다. >> b/c 시간은 계속 흘러가기 때문에 
random.shuffle(target_data) # 섞기 함수
print(ori_data)
print(target_data)

'''


'''
# 방법 1
import random
CARD_TYPE = 4 #card 종류는 4가지
CARD_PER_TYPE_SIZE = 13 # 한가지 card 종류가 가질 수 있는 값 == 사이즈
TOTAL_CARD_COUNT = CARD_TYPE * CARD_PER_TYPE_SIZE # 카드 종류 * 하나의 카드가 가질 수 있는 값  

# 모든 카드 생성
all_cards = list(range(52))
seq = list('♤♡♧◇')
card_id = list('A23456789')+['10']+list('JQK')
print(seq, card_id)

# 12는 ♤k이다
#target_num = 33

print(seq[int(12/CARD_PER_TYPE_SIZE)])
print(12%CARD_PER_TYPE_SIZE)
'''



#방법 2 


#트럼프 카드 준비
types = list('♤♡♧◇')
nums= list('A23456789')+['10']+list('JQK')
cards = [i+j for i in types for j in nums]


# 셔플
import random
random.shuffle(cards)
print(cards[:8]) # 랜덤으로 뽑은 카드 8개
print('나의 카드',cards[:8:2]) #내 카드
print('컴퓨터의 카드', cards[1:9:2]) # 컴퓨터의 카드

# 카드 합산
# 내 카드 합산 : 최초 2개
# A는 합산값의 * 2을 한다 >> 예를 들어 A, 3 => (1,3) *2 = 8점
# J = 11, Q = 12, K = -5


# 내 카드 최초 두장 추출
my_first_card = cards[:8:2][:2]

#컴퓨터 카드 최초 두장 추출
com_first_cards = cards [1:9:2][:2]



# 합산 값
sum = 0

# 정수값 추출 >> 멤버 하나씩 뽑아서(for문 사용) 슬라이싱 or 추출 or 분해


for n in my_first_card:
    # 타입을 제거한다. (0번째 문자를 없애야함)
    tmp = n[1:]

    if tmp == 'A' or tmp == 'J' or tmp =='K'or tmp =='Q':
        if   tmp == 'A' : sum +=1
        elif tmp == 'J' : sum += 11 
        elif tmp == 'Q' : sum += 12 
        elif tmp == 'K' : sum += 13 
    else: # 기본형이 정수 
        sum += int(tmp)


########
# A~K까지를 키로 보고, 이를 통해 값을 획득하면 간단하게 합산 처리
# 이를 위해 점수 변환 표를 준비한다.
score_table = dict()
k=1
for key in nums:
    # 1~13 값을 차례대로 넣어라 
    score_table[key] = k
    k+=1
print(score_table)

#====================================================
# 합하기
sum = 0
# 내 카드에서 카드 마크 빼서 score_table에 넣기
for n in my_first_card:
    sum += score_table[n[1:]]
print("내 최초 카드 2장의 합",sum)






































































