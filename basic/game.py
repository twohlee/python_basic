# 환경변수 or 게임 데이터 >> 역할 : 프로그램에 영향을 미치는 고정값(임계값)을 상수로 빼고,
# 향후에는 *.py 바깥쪽으로 빼서 저장 (파일 or 디비 or 서버)
# 고정값을 바깥으로 뺀다. 

GAME_TITLE_LEN_MAX = 20  # 상수값을 담는 변수는 늘 대문자로 씁시다.
PLAYER_NAME_LEN_MAX = 15 
GAME_LEVEL_MIN = 1
GAME_LEVEL_MAX = 9

# 절차적 프로그램 실습
# 간단한 게임을 구현하여
# 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다.
# 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행
# 목적, 파이썬 타입, 연산, 조건, 반복, 흐름제어 등을 프로그램을 개발하면서 심화 학습한다.

# <요구사항>
# 1. 게임이 시작하면 "Enjoy Custom Game World"라는 문구를 출력한다.
# 2-1. "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 라는 문구를 출력
# 2-2. 사용자가 입력할 때까지 무제한으로 대기한다.
# 2-3. 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!"라고 출력하고 다시 입력 대기한다.
# 2-4. 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다.
# 2-5. 20자 이내로 입력하면 gameTitle이라는 변수에 게임 제목을 담고, 다음 3단계로 진입한다.
# 3-1. "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다."
# 3-2. 입력에 대한 처리는 2-4~2-5의 조건과 동일하게 처리.
# 3-3. 플레이어의 이름은 player_name이라는 변수에 담는다.
# 4-1. "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."
# 4-2. 입력에 대한 처리는 2-4~2-5의 조건과 동일하게 처리하나, 정수가 아니면 뭐라한다.
# 4-3. 게임 난이도는 game_level이라는 변수에 담는다.

#-----------------------------------------------------------------------------------------------------
'''
# 내가 작성한 코드 


#1
print('Enjoy Custom Game World')

#2
game_Title = str(input('게임 제목을 입력하시오, 단 {} 자 이내로 입력 가능합니다'.format(GAME_TITLE_LEN_MAX)))

while(len(game_Title)>=20 and (game_Title == '')):
    if(game_Title == ''):
        print('정확하게 입력하세요!') 
        game_Title = str(input('게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다'))
    elif((len(game_Title))>=20):
        print("20자가 초과되었습니다.") 
        game_Title = str(input('게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다'))

#3
player_name = str(input('플레이어의 닉네임을 입력하시오, 단 {}자로 제한한다.=>'.format(PLAYER_NAME_LEN_MAX)))

while(len(player_name>=15) and (player_name == '')):
    if(player_name == ''):
        print('정확하게 입력하세요!')
        player_name = str(input('플레이어의 닉네임을 입력하시오, 단 15자로 제한한다.'))
    elif((len(player_name))>=15):
        print("15자가 초과되었습니다.")
        player_name = str(input('플레이어의 닉네임을 입력하시오, 단 15자로 제한한다.'))

#4
game_level = int(input('게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다.'))

while((type(game_level) != int and game_level not in range(1,10))):

    if(type(game_level) != int):
        print('정수가 아니잖아용!!!')
        game_level = int(input('게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다.'))
    elif(game_level not in range(1,10)):
        print("1~9범위 내의 숫자를 입력해주세요")
        game_level = int(input('게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다.'))

#--------------------------------------------------------------------------------------------------------------
'''
# 선생님께서 작성한 코드


print("Enjoy Custom Game World")
# 2-2. 사용자가 입력할 때까지 무제한으로 대기한다.
while True: #반드시 내부에 break가 있어야 한다.
    # 사용자가 엔터키를 칠 때까지 코드를 블럭하고 있다. 
    
    # 2-1. "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 라는 문구를 출력
    tmp = input('게임 제목을 입력하시오, 단 {} 자 이내로 입력 가능합니다 =>'.format(GAME_TITLE_LEN_MAX)).strip()


    # 2-3. 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!"라고 출력하고 다시 입력 대기한다.
    if not tmp: #스페이바를 몇 번치고 엔터를 친 것도 같이 처리한다. >> 위에서 값 입력받을 때 .strip()써서 처리하기.
        print('정확하게 입력하세요!')
        
    # 2-4. 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다.
    elif (len(tmp)>20):
        print("20자가 초과되었습니다.") 
        
    # 2-5. 20자 이내로 입력하면 gameTitle이라는 변수에 게임 제목을 담고, 다음 3단계로 진입한다.
    else:
        gameTitle = tmp 
        
    # 다음 3단계로 진입한다. >> 2단계를 끝내라
        break

#3단계 >> gameTitle은 while안 else안에서 정의하였으나, while 밖에서도 사용이 가능하다.
# 파이썬의 함수 외부, 클래스 외부에서 정의된 변수는 모두 전역변수    
# 3-1. "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다."
# 3-2. 입력에 대한 처리는 2-4~2-5의 조건과 동일하게 처리.
# 3-3. 플레이어의 이름은 player_name이라는 변수에 담는다.
print('gameTitle', gameTitle)


while True:
    tmp = input("플레이어의 닉네임을 입력하시오, 단 {}자로 제한한다.=>".format(PLAYER_NAME_LEN_MAX)).strip()
    if not tmp:
        print('정확하게 입력하세요!')
    elif (len(tmp)>15):
        print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
    else:
        player_name = tmp
        break




# 4단계
# 4-1. "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."
# 4-2. 입력에 대한 처리는 2-4~2-5의 조건과 동일하게 처리하나, 정수가 아니면 뭐라한다.
# 4-2. >> 사용자가 넣을 수 있는 케이스를 고려하여 점점 범위가 줄어들게 배치  
# >> 조건 진행 순서 : 공백 입력, 정수가 될 수 없는 값, // 1~9 이외의 값, 정수가 될 수 없는 값, 정확하게 넣을 경우
# 앞의 조건 2개는 문자열, 뒤의 조건 두개는 정수형을 다룸 >> 조건을 나누기
# 4-3. 게임 난이도는 game_level이라는 변수에 담는다.

'''
# 4단계 구현 case1
while True:
    tmp = input("게임 난이도를 입력하시오, 단 {}~{}까지 정수 형태로 제한한다.=>".format(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    
    if not tmp: #공백은 잡는다
        continue
        print('정확하게 입력하세요!')
    
    elif (len(tmp)>15): # 뭔가는 들어있다 >> 정수가 안되면 컷이 되도록
        continue
        print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
    
    # 여기서 입력 값의 정수 변환이 들어가야함.
    if condition: # 1~9 이외의 값이면 컷
        pass
    
    else: # 정상적인 값 
        player_name = tmp
        break

'''



# 4단계 구현 case2

while True:

    tmp = input("게임 난이도를 입력하시오, 단 {}~{}까지 정수 형태로 제한한다.=>".format(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    
    if not tmp: # 공백이면 컷
        print("정확하게 입력하세요")
        continue
        
    if not tmp.isnumeric(): # 뭔가는 들어 있다 >> 정수 아니면 컷
        print('1~9까지 사이값으로 정확하게 입력하세요')
        continue

# 정수가 될 수 있는 놈들        
# 입력값의 정수변환
    tmp = int(tmp)

    if tmp<1 or tmp>9: # 1~9가 아닌 값 컷
        print('1~9까지 사이값으로 정확하게 입력하세요')
        continue
        
# 정상값
    game_level = tmp
# 정확한 입력

# 5단계

print('-'*20)
print('현재까지 입력 상황')
print('gameTitle', gameTitle)
print('player_name',player_name)      
print('game_level',game_level)
print('-'*20)    

