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
        self.status = not FRESH  # 처음에는 피곤한 상태
        self.디버깅시도횟수 = 0

    def 코딩(self):
        print("코딩 중...")

    def 생각한다(self):
        print("생각 중...")

    def 휴식(self):
        print("휴식 중...")
        self.status = random.choice([FRESH, not FRESH])  # 휴식 후 랜덤 상태 변경

    def 디버깅(self):
        print("디버깅 중...")
        self.디버깅시도횟수 += 1  # 디버깅 시도 횟수 증가

        if self.디버깅시도횟수 > 5:
            print("디버깅을 5번 시도했으므로 종료합니다.")
            return not SUCCESS  # 디버깅 실패로 종료
        
        # ✅ 수정: FRESH 상태일 때 디버깅이 성공해야 함!
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
            break  # 디버깅을 5번 초과하면 종료

        while 개발자.status != FRESH:  # 개발자가 지쳤으면 휴식
            개발자.휴식()
        
        개발자.생각한다()
        개발자.코딩()

    개발자.퇴근()

if __name__ == "__main__":
    개발자 = Developer()
    day_routine(개발자)
