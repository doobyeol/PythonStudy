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
