import test6

# 예외처리
# 코드는 잡재적으로 오류를 가질 수 있다. 
# 이 때, s/w를 다운되지 않게 하고, 그 때의 오류 정보를 수집하고, 문제 없이 다음 단계로 진행시키게 하는 방법
# => 예외처리
# 모든 예외의 근본이 되는 Exception 

# case1) 예외 발생 시 코드 진행 확인 
print(0)
try: # 예외가 발생할만한 코드를 감싼다.
    print(1)
    print(1/0)
    print(2)
except Exception as e: # 예외가 발생하면 호출됨, e는 Exception의 별칭 , 여기서 except는 타 언어에서 catch의 의미
    print(3,e)
else: # 예외없이 정상적으로 코드가 진행되면 호출, except가 발생하면 else의 statement는 실행되지 않음
    print(4)
finally: # 예외가 발생하든 말든 무조건 실행됨
    print(5)
print(6)



# case2) 정상 시, 코드 진행 확인 
print(0)
try: # 예외가 발생할만한 코드를 감싼다.
    print(1)
    print(2)
except Exception as e: # 예외가 발생하면 호출됨, e는 Exception의 별칭 , 여기서 except는 타 언어에서 catch의 의미
    print(3,e)
else: # 예외없이 정상적으로 코드가 진행되면 호출, except가 발생하면 else의 statement는 실행되지 않음
    print(4)
finally: # 예외가 발생하든 말든 무조건 실행됨
    print(5)
print(6)





