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
