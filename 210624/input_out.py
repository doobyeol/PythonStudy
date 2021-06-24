
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