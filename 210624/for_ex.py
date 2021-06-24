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
