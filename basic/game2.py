# 상수값을 담는 변수는 늘 대문자로 씁시다.
GAME_TITLE_LEN_MAX = 20  
PLAYER_NAME_LEN_MAX = 15 
GAME_LEVEL_MIN = 1
GAME_LEVEL_MAX = 9


print("Enjoy Custom Game World")



while True:
    tmp = input('게임 제목을 입력하시오, 단 {} 자 이내로 입력 가능합니다 =>'.format(GAME_TITLE_LEN_MAX)).strip()
    if not tmp:
        print('정확하게 입력하세요!')
    elif (len(tmp)>20):
        print("20자가 초과되었습니다.") 
    else:
        gameTitle = tmp
        break

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




while True:
    
    tmp = input("게임 난이도를 입력하시오, 단 {}~{}까지 정수 형태로 제한한다.=>".format(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    
    if not tmp: 
        print("정확하게 입력하세요")
        continue
        
    if not tmp.isnumeric(): 
        print('1~9까지 사이값으로 정확하게 입력하세요')
        continue

    tmp = int(tmp)

    if tmp<1 or tmp>9:
        print('1~9까지 사이값으로 정확하게 입력하세요')
        continue
        
    game_level = tmp


print('-'*20)
print('현재까지 입력 상황')
print('gameTitle', gameTitle)
print('player_name',player_name)      
print('game_level',game_level)
print('-'*20)    





