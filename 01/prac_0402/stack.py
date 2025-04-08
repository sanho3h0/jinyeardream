'''
Stack 클래스를 완성하세요.
'''

class Stack:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        자료를 저장할 공간(배열) myStack을 만듭니다.
        '''
        self.myStack= []

    def push(self, n) :
        '''
        stack에 정수 n을 넣습니다.
        '''
        self.myStack.append(n)

    def pop(self) :
        '''
        stack에서 가장 위에 있는 정수를 제거합니다. 만약 stack에 아무 원소가 없다면 아무 일도 하지 않습니다.
        '''
        if self.empty() == 1:
            return
        # del self.myStack[-1]
        self.myStack.pop()

    def size(self) :
        '''
        stack에 들어 있는 정수의 개수를 return 합니다.
        '''
        

    def empty(self) :
        '''
        stack이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        pass

    def top(self) :
        '''
        stack의 가장 위에 있는 정수를 return 합니다. 만약 stack에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1
        return self.myStack[-1]

stack = Stack()
stack.pop()
