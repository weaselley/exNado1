##############################
## 예외 처리
# try:
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)

# try:
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# # except:
# #     print("알 수 없는 에러가 발생하였습니다.")
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

##############################
## 에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")

##############################
## 사용자 정의 에러처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력 값: {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# # except BigNumberError:
# #     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
#     print(err)

##############################
## Finally
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력 값: {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")
# except BigNumberError:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
# # except BigNumberError as err:
# #     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
# #     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

##############################
## Module
# import theater_module
# theater_module.price(3)
# theater_module.price_early(4)
# theater_module.price_soldier(5)

# import theater_module as tm
# tm.price(3)
# tm.price_early(4)
# tm.price_soldier(5)

# from theater_module import *
# price(3)
# price_early(4)
# price_soldier(5)

# from theater_module import price, price_early
# price(3)
# price_early(4)
# # price_soldier(5)

# from theater_module import price_soldier as price # price means price_soldier
# price(5)

##############################
## package
# import travel_pack.thailand
# trip_to = travel_pack.thailand.ThailandPackage()
# trip_to.detail()

# from travel_pack.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel_pack import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

##############################
# # __all__
# # 이건 __init__을 수정해줘야 실행됨.
# from travel_pack import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

##############################
## pakage, module location
# import inspect
# import random
# from travel_pack import *
# # from travel_pack_temp import * # random 경로에 travel_pack_temp로 이름 변경해서 넣어두면 실행됨.
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

##############################
## pip install
## pip install beautifulsoup4
## pip uninstall beautifulsoup4
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

##############################
## 내장 함수
## 구글에서 list of python builtins 검색해서 확인 가능
# language = input("무슨 언어를 좋아하세요? ")
# print("{}은/는 아주 좋은 언어입니다.".format(language))

# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())

# import random
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

##############################
## 외장 함수
## 구글에서 list of python modules 검색해서 확인 가능
# glob: 경로 내의 폴더/파일 목록 조회
# import glob
# print(glob.glob("./bk_examples/*.py"))

# os: 운영 체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())
# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print(today + td)