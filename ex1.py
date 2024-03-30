##############################
## contents
## 01. Print format
## 02. file inout
## 03. pickle
## 04. with
## 05. Class
##### 05.1. __init__, 
##### 05.2. 맴버변수, 메소드
##### 05.3. 상속, 다중 상속,
##### 05.4. 메소드 오버라이딩
##### 05.5. pass
##### 05.6. super
##############################
# # 01. Print format
# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# print("{0:_>+10}".format(500))
# print("{0:_<+10}".format(500))

# print("{0:,}".format(100000000000000))
# print("{0:+,}".format(100000000000000))
# print("{0:+,}".format(-100000000000000))

# print("{0:^<+30,}".format(100000000))

# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))

##############################
# 02. file inout
# score_file = open("./data/score.txt", "w", encoding="utf8")
# print("math : 0", file=score_file)
# print("eng : 50", file=score_file)
# score_file.close()

# score_file = open("./data/score.txt", "a", encoding="utf8")
# score_file.write("science : 20\n")
# score_file.write("music: 100")

# score_file = open("./data/score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("./data/score.txt", "r", encoding="utf8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("./data/score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("./data/score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

# score_file = open("./data/score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

##############################
## 03. pickle
# import pickle

# profile_file = open("./data/profile.pickle", "wb")
# profile = {"name": "Jack", "age":30, "hobby":["soccer", "golf", "coding"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("./data/profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

##############################
## 04. with
# import pickle
# with open("./data/profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("./data/study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("I try to learn python")

# with open("./data/study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

##############################
## 05. Class
# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# Tank_name = "탱크"
# Tank_hp = 150
# Tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(Tank_name))
# print("체력 {0}, 공격력 {1}\n".format(Tank_hp, Tank_damage))

# Tank2_name = "탱크"
# Tank2_hp = 150
# Tank2_damage = 35
# print("{} 유닛이 생성되었습니다.".format(Tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(Tank2_hp, Tank2_damage))

# def attack(name, location, damage):
#     print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,
#                                                              location, damage))

# attack(name, "1시", damage)
# attack(Tank_name, "1시", Tank_damage)
# attack(Tank2_name, "1시", Tank2_damage)

##### 05.1. __init__,
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank1 = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True # Adding additional objects is possible (for only wraith2).

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

##### 05.2. 맴버변수, 메소드
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

##### 05.3. 상속, 다중 상속,
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

##### 05.4. 메소드 오버라이딩
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location): # Unit has move function but override move function.
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# vulture1 = AttackUnit("벌쳐", 80, 10, 20)
# BattleCruiser1 = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture1.move("11시")
# BattleCruiser1.move("9시")

##### 05.5. pass
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location): # Unit has move function but override move function.
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 일단 완성된 것 처럼 사용

# supply_depot = BuildingUnit("서플라이디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

##### 05.6. super
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location): # Unit has move function but override move function.
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0) # = Unit.__init__(self, name, hp, 0)
#         self.location = location

# 다중 상속 시 발생하는 문제점: 하나만 super를 쓸 수 있음.
# 명시적으로 써 줘야 함.
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")
# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")
# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()
#         # Unit.__init__(self)
#         # Flyable.__init__(self)
# dropship = FlyableUnit()