'''
1. maxMachine 클래스를 완성하세요.
2. sorting 함수를 완성하세요.
'''

class maxMachine :
    '''
    이곳에 '최댓값 기계' 문제에서 작성했던 클래스를 붙여넣으세요
    '''
    # 클래스가 생성될 때 호출되는 초기화 함수 (생성자)
    def __init__(self) :
        # 숫자를 담을 빈 리스트를 준비
        self.numbers = []

    # 숫자를 리스트에 추가하는 함수
    def addNumber(self, n) :
        # 입력된 n을 numbers 리스트에 추가
        self.numbers.append(n)

    # 숫자를 리스트에서 제거하는 함수
    def removeNumber(self, n) :
        # numbers 리스트에서 n을 찾아서 제거
        self.numbers.remove(n)

    # 현재 저장된 숫자 중 가장 큰 값을 반환하는 함수
    def getMax(self) :
        # numbers 리스트에서 가장 큰 값을 찾아서 반환
        return max(self.numbers)

def sorting(myList) :
    '''
    myList를 내림차순으로 정렬하여 반환하는 함수를 작성하세요.

    예를 들어, myList = [5, 2, 3, 1] 이라면 [5, 3, 2, 1] 을 반환해야 합니다.

    단, maxMachine class를 이용하도록 합니다. 
    '''

    myMachine = maxMachine()

    result = []

    for c in myList:
        myMachine.addNumber(c)
    for _ in myList:
        number = myMachine.getMax()
        myMachine.removerNumber(number)

    return result