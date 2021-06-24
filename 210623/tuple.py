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
