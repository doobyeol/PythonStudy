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
