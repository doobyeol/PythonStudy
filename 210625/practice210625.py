# 예외처리

# try :
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err :
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


# 에러 발생시키기
# try : 
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요."))
#     num2 = int(input("두번째 숫자를 입력하세요."))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")


# 사용자 정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self) :
#         return self.msg

# try : 
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요."))
#     num2 = int(input("두번째 숫자를 입력하세요."))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("한자리 숫자만 입력하세요.")
#     print(err)



# finally
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self) :
#         return self.msg

# try : 
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요."))
#     num2 = int(input("두번째 숫자를 입력하세요."))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/ num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("한자리 숫자만 입력하세요.")
#     print(err)
# finally :
#     print("계산기를 이용해주셔서 감사합니다.")

    
# 모듈
# 함수정의나 클래스등 파이썬 문장들을 담고있는 파일. 확장자 py

# 같은 경로이거나 파이썬 모듈이 모여있는 경로


# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# from random import *
# price(3)
# price_morning(4)
# price_soldier(5)


# from theater_module import price, price_morning
# price(3)
# price_morning(4)


from theater_module import price_soldier as price
price(4)  