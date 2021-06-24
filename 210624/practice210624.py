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


# 표준 체중 구하기

height = 175
gender = "남자"

def std_weight(height, gender) : # m단위 공식이고 키는 cm이므로 100을 나누어주어야 한다.
    if gender == "남자" :
        result = height * height * 22
    else :
        result = height * height * 21
    return result

result = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, result))


# 표준 입출력
import sys
print("Python" , "Java", "JavaScript", sep=" vs ", end="?")
print("무엇이 더 재밌을까요?")

print("Python" , "Java", "JavaScript", file=sys.stdout)
print("Python" , "Java", "JavaScript", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기순번표
# 001, 002, 003 ...
for num in range(1, 21) : 
    print("대기번호 : " + str(num).zfill(3)) # 0 채우기


# answer = input("아무 값이나 입력하세요.")
answer = 10
# input으로 입력받은 값은 항상 str의 타입을 가진다.
print(type(answer))
print("입력하신 값은 " + str(answer) + "입니다.")



# 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일때는 +로 표시, 음수일때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬 하고 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))

# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))

# 3자리마다 콤마를 찍어주기, 부호도 붙이고 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 (소수점 3ㅉ째 자리에서 반올림)
print("{0:.2f}".format(5/3))

# 파일 입출력

# score_file = open("score.txt","w", encoding="utf8") # 한글인코딩
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.readline(), end="") # 파일 줄별로 읽기, 한줄 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# lines = score_file.readlines() # list 형태로 지정
# for line in lines:
#     print(line, end="")

# score_file.close()



# pikle
# import pickle
# profile_file = open("profile.pickle", "wb") # 쓰기목적w 바이너리타입b
# profile = {"이름":"김수한무","나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # 쓰기목적w 바이너리타입b
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()



# with

import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
    


# 퀴즈

for x in range(1, 51):
    title = str(x)+"주차.txt"
    with open(title, "w", encoding="utf8") as report_file:
        # report_file.write("- " + str(x)+" 주차 주간보고 -\n")
        # report_file.write("부서 : \n")
        # report_file.write("이름 : \n")
        # report_file.write("업무요약 : \n")

        report_file.write("- {0} 주차 주간보고 -".format(x))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무요약 : ")
    