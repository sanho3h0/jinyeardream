from user import User

print("파이썬 파일 시작")
class Post:

    # 생성자는 매개변수로 작성자와 내용을 받아,
    # 그 값을 속성에 저장합니다.
    def __init__(self, author, content):
        print("초기화 시작")
        self.author = author
        self.content = content
        self.comments= []
        self.likes = 0
    # 메서드 (동작,클래스의 함수)
    def show(self):
        print("show 함수 호출")
        print(self.content,"저는",self.author.name,'입니다.!')

print("전역변수 선언")
me = User('taekyun')
my_post = Post(me, "안녕하세요!")
my_post.show()
