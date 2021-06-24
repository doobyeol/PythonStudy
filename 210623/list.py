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
