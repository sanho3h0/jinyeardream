# 배열 구현
class ListPipe:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        self.myPipe = []

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        self.myPipe.insert(0, n) # (인덱스, 값)

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        self.myPipe.append(n)

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환(return)합니다.
        '''
        return self.myPipe


def processBeads(myInput) :
    myPipe = ListPipe()

    result = []
    for bead, direction in myInput: # [[1, 0](입력첫줄), [2, 1](입력둘째줄), [3, 0]]
        if direction == 0:
            myPipe.addLeft(bead)
        elif direction == 1:
            myPipe.addRight(bead)

    result = myPipe.getBeads()
    return result
# 링크드 리스트 구현
class LinkedListElement :
    def __init__(self, val, ptr) :
        self.value = val
        self.myNext = ptr

class LinkedListPipe:
    '''
   ` Linked List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        '''
        self.start = None # 연결리스트 시작점
        self.end = None # 연결리스트 끝점

        # 1 -> 2 -> 3
        # 4 -> 1 -> 2 -> 3

    def addLeft(self, n) :
        '''
        파이프의 왼쪽으로 구슬 n을 삽입합니다.
        '''
        # 맨처음 (리스트에 시작 끝이 없을 때)
        if self.start is None and self.end is None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else: # 시작 노드나 끝 노드가 있을 때
            element = LinkedListElement(n, self.start) # 노드 다음을 원래 있던 처음 노드에 연결
            self.start = element # 리스트 파이프의 첫 시작을 만든 노드

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        if self.start is None and self.end is None:
            element = LinkedListElement(n, None)
            self.start = element
            self.end = element
        else:
            element = LinkedListElement(n, None)
            self.end.myNext = element
            self.end = element

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        beeds = []
        current = self.start
        # while current is not None and current != self.end:
        while current.myNext is not None:
            beeds.append(current.value)
            current = current.myNext
        beeds.append(current.value)
        return beeds

def processBeads(myInput) :
    myPipe = LinkedListPipe()

    result = []
    for bead, direction in myInput: # [[1, 0](입력첫줄), [2, 1](입력둘째줄), [3, 0]]
        if direction == 0:
            myPipe.addLeft(bead)
        elif direction == 1:
            myPipe.addRight(bead)

    result = myPipe.getBeads()
    return result




# 메인문
pipe = LinkedListPipe()
pipe.addRight(1)
pipe.addRight(2)
pipe.addRight(3)
pipe.getBeads()