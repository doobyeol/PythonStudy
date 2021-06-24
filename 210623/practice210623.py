# int
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# string
print('풍선')
print("나비")
print("ㅋ"*9)

# 참 / 거짓 blooean
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
animal ="강아지"
name = "보름이"
age = 8
hobby = "공놀이"
is_adult = age >= 3

# 애완동물을 소개해주세요.
print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "산책"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name + "는 " , age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

''' 이렇게
하면
여러문장이
주석처리'''

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기
print(10%3) # 1
print(5//3) # 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # 크거나 작다 False
print(10 <= 3) # False
print(5 <= 5) # True

print(3 == 3) # == 같다.True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not (1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False





print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2
print(number) # 16
number += 2
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 5 # 0
print(number)

print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5, 12)) # 최대값
print(min(5, 12)) # 최소값
print(round(3.14)) # 3 반올림
print(round(4.99)) # 5 반올림

from math import * # math 라이브러리 안에 있는 모든 것을 사용하겠다.
print(floor(4.9)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *

print(random()) # 랜덤 함수 0.0 ~ 1.0 미만 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 45 이하 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 45 이하 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하 임의의 값 생성

from random import *
off_day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(off_day) + "일로 선정되었습니다.")

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990120-1234567"
print('성별 : ' + jumin[7])
print("연도 : " + jumin[0:2]) # 0부터 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) #  처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) #  7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 대문자 검사
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 원하는 값이 없을경우 -1 반환
# print(python.index("Java")) # index에 찾는 값이 없으므로 error
print("hi")

print(python.count("n"))

# 문자열 포맷

# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))

# 방법2

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))

# 방법4 (v3.6 이상~)
age = 20
color = "노란"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출 문자
# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

url = "http://naver.com"
url = "http://daum.net"
print(url)
url = url.replace("http://","")
print(url)
# index = url.index(".")
# url = url[:index]
url = url[:url.index(".")]
print(url)

password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print(password)

print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트[]

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["김수한무","거북이","두루미"]
print(subway)

# 거북이가 어느칸에 타고 있는가?
print(subway.index("거북이"))

# 삼천갑자씨가 다음 정류장에서 다음 칸에 탐
subway.append("삼천갑자")
print(subway)

# 동방삭을 김수한무와 거북이 사이에 태워봄
subway.insert(1, "동방삭")
print(subway)

# 지하철에 있는 사랆을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("김수한무")
print(subway)

print(subway.count("김수한무"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["거북이", 20, True]
# print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


# 사전
cabinet = {3:"김수한무", 100:"거북이"} # key는 3이고 value는 김수한무
print(cabinet[3]) # 대괄호 안에는 키값을 넣는다
print(cabinet[100])

# 사전자료형의 값을 가져오기
# print(cabinet.get(3))
# print(cabinet[5]) # 5라는 key가 없기 때문에 오류 발생
print(cabinet.get(5)) # get은 값이 없으면 None을 출력
print(cabinet.get(5, "사용 가능")) # key중에 5가 없으면 사용가능을 출력

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"김수한무", "B-100":"거북이"} # key 자료형은 str이여도 상관없다.
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "삼천갑자"
cabinet["C-20"] = "두루미"
print(cabinet)

# 간 손님
del cabinet["A-3"] # key값을 넣으면 삭제할수있다.
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)




# 튜플

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# menu.add("생선까스") 튜플은 add 사용 불가

# name = "김수한무"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
(name, age, hobby) = ("김수한무", 20, "코딩")
print(name, age, hobby)



# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 1,2,3

java = {"김수한무", '거북이', "두루미"}
python = set(["김수한무","삼천갑자"])

# 교집합 (java와 python 을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python을 할 수 없는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("동방삭")
print(python)

# java를 잊었어요
java.remove("거북이")
print(java)






# 자료 구조의 변경
# 카페
menu = {"커피", "우유", "주스"} # set 집합
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu)) # list로 타입이 바뀜
menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))



# 퀴즈
# (활용 예제)
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

# users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")




# 분기

weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10<= temp and temp < 30 :
    print("괜찮은 날씨예요")
elif 0 <= temp and temp < 10 :
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요")



# for 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))

# randrange()
# for waiting_no in range(5): # 0 ~ 4
for waiting_no in range(1, 6): # 1 ~ 5
    print("대기번호 : {0}".format(waiting_no))

starnucks = ["아이언맨", "토르", "아이엠 그루트"]

for customer in starnucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))



# while

customer = "토르"
index = 5
# while(조건):
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출{1}회".format(customer, index))
#     index +=1

customer = "토르"
person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


# continue , break

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음

for student in range(1,11): # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))




















print("==================================================")
