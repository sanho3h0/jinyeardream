'''
문자와 숫자를 섞어서 치더라도 숫자만 나오게 하는 프로그램을 짜보자
1.문자열을 입력받으세요.
2. 입력 받은 문자열에서 문자 또는 기호를 제외한 숫자만 추출해서 문자열 형태로 출력하는 코드를 작성하세요.
Tip. 아스키(ASCII) 코드를 이용
1) ord()함수를 사용해보기
2) isdigit() 함수 사용
3) 리스트 컴프리핸션과 join 사용
'''
# str = input()
# for ch in str: #문자열 안에서 ch 검사
#     if ch.isdigit():
#     # ch.isdigit()은 문자 ch가 숫자인지(True/False) 판별해 주는 문자열 메서드
for num in range(1,44):
    count_num = str(num).count('3') + str(num).count('6') + str(num).count('9')
    # 3,6,9 개수 세기 -> 박수 여러번치기위해

    if count_num > 0:
        print("짝"*count_num+"!", end=" ")
    else:
        print(num, end=" ")