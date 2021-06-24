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
