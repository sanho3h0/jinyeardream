class Animal:
    def __init__(self, name, say):
        self.name = name
        self.say = say

    def saying(self):
        return self.say
    
animals = {
    "강아지" : Animal("강아지", "멍멍!")
}
