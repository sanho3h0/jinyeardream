class Animal():
    # 초기화 함수만들기 (__init__)
    def __init__(self , name, say):
        self.name = name
        self.say = say

    def saying(self):
        print(self.say)
    
# 1번을 해보세요.
dog = Animal (name='강아지' , say='멍멍!')
dog.saying()
# dog=Animal("강아지","멍멍")
# cat = Animal (name='고양이' , say='야옹!')

# animal_speaks = input()