
# 표준 체중 구하기

height = 175
gender = "남자"

def std_weight(height, gender) : # m단위 공식이고 키는 cm이므로 100을 나누어주어야 한다.
    if gender == "남자" :
        result = height * height * 22
    else :
        result = height * height * 21
    return result

result = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, result))
