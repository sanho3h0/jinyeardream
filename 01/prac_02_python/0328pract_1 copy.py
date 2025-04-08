'''
마지막으로 정리한 내용을 이 코드에서 다시한번 복기해보셨으면 좋겠습니다.

일부러 틀린 부분도 넣어놨으니 디버깅으로 돌려보면서 어느 부분에서 에러가 나는지 찾아보세요!

이 코드내에서 어떤 부분이 어떤 개념을 가지고 있는지 생각해보고

그래도 모르시겠다면 코치들에게 DM 남겨주세요!!

실무에서 사실 많이 볼 수있는 에러로 구성을 해서 아마 찾는데 오래 걸릴 걸 예상하고 만들긴 했습니다.
문법이 아닌 논리적인 이유로 원하는 값이 나오지 않을거에요.

의도대로 작동을 하는지 알기위해선 먼저 의도를 이해하고 있어야 하는데요.

'개발자'가 지치면(FRESH status가 아닌 경우) 디버깅을 실패할 가능성이 높기 때문에 status가 FRESH 일 때 디버깅이 성공할 가능성이 높아지겠죠?
실제 코드에서도 이 부분을 잘 살펴보시면 이론상 반대로 적용되있는걸 찾으실 수 있을거에요
'''

import random


SUCCESS = True
FRESH = True

class Employee:
    def 출근(self):
        print("출근했습니다.")

    def 퇴근(self):
        print("퇴근했습니다.")

class Developer(Employee):
    def __init__(self):
        self.status = not FRESH
        self.디버깅시도횟수 = 0

    def 코딩(self):
        print("코딩 중...")

    def 생각한다(self):
        print("생각 중...")

    def 휴식(self):
        
        # 5번의 디버깅만 시도해야함 코딩끝나고 쉬기전에
        if self.디버깅시도횟수 > 5:
            print("디버깅을 5번 시도했으므로 종료합니다.")
            return SUCCESS # 디버깅 못고치고 결국 퇴근
        else:
            print("휴식 중...")
            self.status = FRESH

    def 디버깅(self):
        # 디버깅 시도 횟수 증가
        self.디버깅시도횟수 += 1
        print("디버깅 중...")
        self.status = random.choice([FRESH, not FRESH])
        # 상태변경 랜덤
    
        if self.status == FRESH:
            print("디버깅을 완료했습니다.")
            return SUCCESS
        else:
            print("디버깅을 실패했습니다.")
            return not SUCCESS

def day_routine(개발자: Developer):
    개발자.출근()
    개발자.생각한다()

    개발자.코딩()

    while 개발자.디버깅() != SUCCESS:
        if 개발자.디버깅시도횟수 > 5:
            break
        while 개발자.status != FRESH:
            개발자.휴식()
        개발자.생각한다()
        개발자.코딩()

    개발자.퇴근()

if __name__ == "__main__":
    개발자 = Developer()
    day_routine(개발자)


#오류의 원인:

# 논리적으로 개발자가 "지치지 않은 상태"(FRESH)일 때 디버깅 성공 확률이 높아야 함.

# 하지만 현재 코드에서는 self.status != FRESH일 때만 디버깅 성공으로 간주됨 → 오류!

# 즉, 개발자가 지치지 않은 경우(FRESH일 때) 디버깅이 실패하고, 지친 경우(!FRESH) 성공하는 이상한 논리가 되어 있음.

# 해결 방법:

# self.status == FRESH일 때 성공하도록 수정해야 함.
