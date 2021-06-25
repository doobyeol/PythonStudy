# super

class Unit :
    def __init__(self) : 
        print("Unit 생성자")

class Flyable :
    def __init__(self) :
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


# 드랍쉽
dropship = FlyableUnit()

# 두개 이상의 클래스를 다중상속 받을때에는 맨 처음 상속받는 클래스에 대해서만 유닛함수가 호출된다.

