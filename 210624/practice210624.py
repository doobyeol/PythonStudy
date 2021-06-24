# 한줄 for 문

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로함 -> 101, 102, 103, 104...
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


# 퀴즈

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 1 ~ 50
    time = randrange(5, 51) # 5 ~ 50분 소요시간
    if 5 <= time <=15 : # 5분~15분 이내의 손님, 탑승 승객수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else : # 매칭 실패한 경우는 탑승 승객 수 증가하지 않
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0}분".format(cnt))



# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값
def deposit(balance, money) : # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money) : # 출금
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}입니다.".format(balance))
        return balance

def withdraw_night(balance, money) : # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))




# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이:{1}\t 주 사용언어:{2}" \
#         .format(name, age, main_lang))
#
# profile("김수한무", 20, "파이썬")
# profile("거북이", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이:{1}\t 주 사용언어:{2}" \
#         .format(name, age, main_lang))
#
# profile("김수한무")
# profile("거북이")



# 키워드값

# def profile(name, age, main_lang) :
#     print(name, age, main_lang)
#
# profile(name="김수한무", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="거북이")



# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print("이름 : {0}\t나이:{1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language) :
    print("이름 : {0}\t나이:{1}\t".format(name, age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()


profile("김수한무", 20, "Python","Java","C","c++","C#","JavaScript")
profile("거북이", 25, "Kotlin", "Swift", "","","")




# 지역변수와 전역변수
gun = 10

def checkpoint(soldiers) : # 경계근무
    # gun = 20
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
