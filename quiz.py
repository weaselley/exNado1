## free lecture (나도 코딩)

# # Quiz 1
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")


# # Quiz 2
# from random import * 
# day = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")


# # Quiz 3
# _input = "http://naver.com"
# _input2 = _input.replace("http://","")
# _dotInd = _input2.index(".")
# _input3 = _input2[:_dotInd]
# print(_input)
# print(_input2)
# print(_dotInd)
# print(_input3)
# _pw = _input3[0:3] + str(len(_input3)) + str(_input3.count("e")) + "!"
# print("생성된 비밀번호:" + _pw)


# # Quiz 4
# from random import *
# _list = list(range(1, 21))
# shuffle(_list)
# _chicken = sample(_list, 1)
# _list.remove(_chicken[0])
# _coffee = sample(_list, 3)
# _coffee.sort()
# # print(" -- 당첨자 발표 --")
# # print(" 치킨 당첨자: ", _chicken)
# # print(" 커피 당첨자: ", _coffee)
# # print(" -- 축하합니다 --")
# print(" -- 당첨자 발표 --")
# print(" 치킨 당첨자: {0}".format(_chicken[0]))
# print(" 커피 당첨자: {0}".format(_coffee))
# print(" -- 축하합니다 --")


# # Quiz 5
# from random import *
# _ind = 1
# _totalCustomer = 0
# while _ind < 51 :
#     Time = randint(5, 51)
#     if Time < 15 :
#         take = 'O'
#         _totalCustomer += 1
#     else :
#         take = ' '
#     print("[{0}] {1} times customer ({2} min. takes)"\
#         .format(take, _ind, Time))
#     _ind += 1
# print("Total Customer: {0}".format(_totalCustomer))
########## Another solution
# from random import *
# _totalCustomer = 0
# for ii in range(1, 51) :
#     Time = randint(5, 51)
#     if 5 <= Time <= 15 :
#         take = 'O'
#         _totalCustomer += 1
#     else :
#         take = ' '
#     print("[{0}] {1} times customer ({2} min. takes)"\
#         .format(take, ii, Time))
# print("Total Customer: {0}".format(_totalCustomer))


# # Quiz 6
# def std_weight(gender, height_cm) :
#     height_m = height_cm / 100
#     if gender == "남자" :
#         return pow(height_m, 2) * 22
#     elif gender == "여자":
#         return pow(height_m, 2) * 21
#     else:
#         pass
# height = 178
# sex = '여자'
# print("키 {0} {1}의 표준 체중은 {2} kg 입니다.".format(height, sex,\
#     round(std_weight(sex, height)), 2))


# # Quiz 7
# def reporting_n_week(number, add_str):
#     file_path = add_str + str(number) + "주차 주간보고.txt"
#     with open(file_path, "w", encoding="utf8") as reporing_file:
#         reporing_file.write("- " + str(number) + " 주차 주간보고 -\n")
#         reporing_file.write("부서 :\n")
#         reporing_file.write("이름 :\n")
#         reporing_file.write("업무요약 :\n")
# cnt = 1
# while cnt < 51:
#     reporting_n_week(cnt, "./userlib_result/")
#     cnt += 1

########## Another solution
# for i in range(1, 51):
#     with open("./userlib_result/" + str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간 보고 -\n".format(i))
#         report_file.write("부서 :\n")
#         report_file.write("이름 :\n")
#         report_file.write("업무요약 :\n")

# # Quiz 8
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         # print(self.location, end=" ")
#         # print(self.house_type, end=" ")
#         # print(self.deal_type, end=" ")
#         # print(self.price, end=" ")
#         # print(self.completion_year)

#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# h1 = House("강남", "아파트", "매매", "10억", "2010년")
# h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# h3 = House("송파", "빌라", "월세", "500/50", "2000년")

# houses = []
# houses.append(h1)
# houses.append(h2)
# houses.append(h3)
# # print("총 " + str(len(houses)) + "대의 매물이 있습니다.")
# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# # Quiz 9
# class SoldOutError(Exception):
#     pass
# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까? "))
#         if order < 1:
#             raise ValueError
        
#         if order > chicken:
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken < 1:
#             raise SoldOutError

#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# # Quiz 10
# import byme
# byme.sign()