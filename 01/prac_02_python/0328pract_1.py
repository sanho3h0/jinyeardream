'''
마지막으로 정리한 내용을 이 코드에서 다시한번 복기해보셨으면 좋겠습니다.

일부러 틀린 부분도 넣어놨으니 디버깅으로 돌려보면서 어느 부분에서 에러가 나는지 찾아보세요!

이 코드내에서 어떤 부분이 어떤 개념을 가지고 있는지 생각해보고

그래도 모르시겠다면 코치들에게 DM 남겨주세요!!
'''

SUCCESS = True
FRESH = True

class Employee:
    def 출근(self):
        print("출근했습니다.")

    def 퇴근(self):
        print("퇴근했습니다.")

class Developer(Employee):
    def __init__(self):
        self.status = FRESH
        self.디버깅시도횟수 = 0

    def 코딩(self):
        print("코딩 중...")

    def 생각한다(self):
        print("생각 중...")

    def 휴식(self):
        print("휴식 중...")
        self.status = FRESH

    def 디버깅(self):
        print("디버깅 중...")
        # 디버깅 시도 횟수 증가
        self.디버깅시도횟수 += 1
        
        # 5번의 디버깅만 시도
        if self.디버깅시도횟수 > 5:
            print("디버깅을 5번 시도했으므로 종료합니다.")
            return SUCCESS
        
        if self.status != FRESH:
            print("디버깅을 완료했습니다.")
            return SUCCESS
        else:
            print("디버깅을 실패했습니다.")
            return not SUCCESS

def day_routine(개발자: Developer): #타입 힌트(type hint)
    # 개발자 매개변수는 Developer 클래스의 인스턴스여야 한다고 명시하고 있다.
    개발자.출근()
    개발자.생각한다()

    개발자.코딩()

    while 개발자.디버깅시도횟수 < 5:
        # 디버깅 시도 횟수가 5번 미만일 때만 반복
        if 개발자.디버깅() == SUCCESS:
            break
            # 성공 시 디버깅 종료
        while 개발자.status != FRESH:
            개발자.휴식()
            #상태가 FRESH가 아니면 휴식

        개발자.생각한다()
        개발자.코딩()

    개발자.퇴근()

if __name__ == "__main__":
    개발자 = Developer()
    day_routine(개발자)