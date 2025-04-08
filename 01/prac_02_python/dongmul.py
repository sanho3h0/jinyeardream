# Animal 클래스의 인스턴스 dog를 만들고 name에는 “강아지”, say에는 “멍멍!” 을 저장하세요.
# saying() 메서드를 이용해서 dog의 울음소리를 출력하세요.

# 클래스, 속성, 메서드, 인스턴스(객체), 초기화 함수(생성자).

class Animal(): #클래스
    def __init__(self, name, say): #초기화함수 생성자 __init__
        # self 는 인스턴스를 가리키는 변수
        # name, say는 초기화할 값(매개변수)
        self.name = name
        # 매개변수name 의 값을 self.name 속성에 저장한다.
        self.say = say
        # 매개변수는 단순히 전달될 뿐, 객체의 속성으로 저장되지 않으면 함수가 끝난 후 사라집니다.
        # __init__()에서 전달받은 매개변수 값을 self.name, self.say 속성으로 저장했기 때문에 객체가 계속 기억합니다.
    
    def saying(self): #메서드 : 클래스 내부에 정의된 함수
        print(self.say) 
        # say는 지역 변수로 선언되지 않은상태 say라는 변수가 없다.
        # 즉 , print(say) 는 오류
        # 객체의 속성 self.say 은 모든 메서드에서 사용가능하다.


dog = Animal(name='강아지', say='멍멍!')
# Animal클래스의 새로운 인스턴스(객체)를 생성하려고 한다.
# __init__() 자동 호출
# self.name = '강아지' self.say = '멍멍!' 속성이 저장됨
cat = Animal('고양이', '야옹~')
# 파라미터(매개변수) 이름을 명시하지 않아도, 클래스의 __init__ 메서드에서 선언된 순서대로 값이 전달됩니다.
# dog와 cat은 Animal클래스의 인스턴스(객체)이다.
print(dog.name)
dog.saying()
print(cat.name)
cat.saying()