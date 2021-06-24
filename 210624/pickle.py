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