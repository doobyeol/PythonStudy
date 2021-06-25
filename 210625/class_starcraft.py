# 클래스

# # 마린 : 공격 유닛, 군인. 총을 쓸 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력{0}, 공격력 {1}\n". format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데 일반모드 / 시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# # 탱크2 : 공격 유닛, 탱크. 포를 쏠 수 있는데 일반모드 / 시즈모드
# tank_name2 = "탱크"
# tank_hp2 = 150
# tank_damage2 = 35


# print("{0}유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1} \n".format(tank_hp, tank_damage))

# def attack(name, location, damage) :
#     print("{0} : {1} 벙향으로 적군을 공격합니다. [공격력 {2}]").format( \
#         name, location, damage)


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank_name2, "1시", tank_damage2)


# class 


# # 일반 유닛
# class Unit :
#     def __init__(self, name, hp, damage) : 
#         self.name = name
#         self.hp = hp
#         # self.damage = damage
#         # print("{0} 유닛이 생성되었습니다.".format(self.name))
#         # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)


# # # init 생성자
# # # marine3 = Unit("마린")
# # # marine4 = Unit("마린", 40)
# # marine4 = Unit("마린", 40, 5)




# # 멤버변수

# # # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# # wraith1 = Unit("레이스", 80, 5)
# # print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)

# # wraith2 = Unit("빼앗은 레이스", 80, 5)
# # wraith2.clocking = True

# # if wraith2.clocking == True:
# #     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))




# # 메소드

# # 공격유닛

# class AttackUnit :
#     def __init__(self, name, hp, damage) : 
#         self.name = name
#         self.hp = hp
#         self.damage = damage

    
#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))
    
#     def damaged(self, damage) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)




# 상속


# 메딕 : 의무병

# # 일반 유닛
# class Unit :
#     def __init__(self, name, hp) : 
#         self.name = name
#         self.hp = hp


# # 공격유닛

# class AttackUnit(Unit) : # 상속
#     def __init__(self, name, hp, damage) : 
#         Unit.__init__(self, name, hp)
#         self.damage = damage

    
#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))
    
#     def damaged(self, damage) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)




# 다중 상속

# # 일반 유닛
# class Unit :
#     def __init__(self, name, hp) : 
#         self.name = name
#         self.hp = hp


# # 공격유닛

# class AttackUnit(Unit) : # 상속
#     def __init__(self, name, hp, damage) : 
#         Unit.__init__(self, name, hp)
#         self.damage = damage

    
#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))
    
#     def damaged(self, damage) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# # 날수 있는 기능을 가진 클래스

# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


# 메소드 오버라이딩

# 일반 유닛

# class Unit :
#     def __init__(self, name, hp, speed) : 
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location) :
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
#             .format(self.name, location, self.speed))


# # 공격유닛

# class AttackUnit(Unit) : # 상속
#     def __init__(self, name, hp, speed, damage) : 
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

    
#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))
    
#     def damaged(self, damage) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# # 날수 있는 기능을 가진 클래스

# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location) :
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name,"9시")
# battlecruiser.move("9시")






# pass

# class Unit :
#     def __init__(self, name, hp, speed) : 
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location) :
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
#             .format(self.name, location, self.speed))


# # 공격유닛

# class AttackUnit(Unit) : # 상속
#     def __init__(self, name, hp, speed, damage) : 
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

    
#     def attack(self, location) :
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))
    
#     def damaged(self, damage) :
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# # 날수 있는 기능을 가진 클래스

# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed

#     def fly(self, name, location) :
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location) :
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 건물
# class BuildingUnit(Unit) :
#     def __init__(self, name, hp, location):
#         pass # 아무것도 안하고 일단 넘어간다.

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()




# super

# class Unit :
#     def __init__(self) : 
#         print("Unit 생성자")

# class Flyable :
#     def __init__(self) :
#         print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         # super().__init__()
#         Unit.__init__(self)
#         Flyable.__init__(self)


# # 드랍쉽
# dropship = FlyableUnit()

# # 두개 이상의 클래스를 다중상속 받을때에는 맨 처음 상속받는 클래스에 대해서만 유닛함수가 호출된다.


# 스타크래프트 전반전

class Unit :
    def __init__(self, name, hp, speed) : 
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location) :
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))
    
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격유닛

class Attackunit(Unit) : # 상속
    def __init__(self, name, hp, speed, damage) : 
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))
    
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 마린
class Marine(Attackunit):
    def __init__(self):
        Attackunit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10 :
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(Attackunit):
    # 시즈 모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        Attackunit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False :
            return 
        
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else : 
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


#드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# 날수 있는 기능을 가진 클래스

class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(Attackunit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed):
        Attackunit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location) :
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True : # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else :
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True



# 스타크래프트 후반전

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") # good game
    print("[Player]님이 게임에서 퇴장하셨습니다.")


# 실제 게임 시작

game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine) :
        unit.stimpack()
    elif isinstance(unit, Tank) :
        unit.set_seize_mode()
    elif isinstance(unit, Wraith) :
        unit.clocking()


# 전군 공격
for unit in attack_units :
    unit.attack("1시")


from random import *

# 전군 피해
for unit in attack_units :
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 5 ~ 20 데미지

# 게임 종료
game_over()
