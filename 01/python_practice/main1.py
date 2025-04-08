from user import User

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content + "\n감사합니다!"
        self.likes = ['민수']

    def num_likes(self):
        return len(self.likes)

    def like(self, me):
        return len(self.l)
me = User('kyujin')
my_post = Post(me, "안녕하세요!")
print(my_post.num_likes())
my_post.like(me)
