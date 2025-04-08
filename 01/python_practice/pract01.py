class Animal:
    # 상태(속성 : 클래스가 가지고 있는 변수)
    # 이름
    # 나이
    def __init__(self, name, age): # 생성자, 초기화 함수
        self.name = name
        self.age = age

    # 동작(메서드 : 클래스가 가지고 있는 함수)
    # 자기소개
    def introduce(self):
        print("나는", self.name, "이고", self.age, "살 입니다.")

animal = Animal(name="초롱이", age=10)
anima2 = Animal(name="해피", age=5)
animal.introduce()
anima2.introduce()