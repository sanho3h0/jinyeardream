'''
1. ListPipe 클래스를 완성하세요. 
2. processBeads 함수를 완성하세요.
'''

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
        self.myPipe.insert(0,n)

    def addRight(self, n) :
        '''
        파이프의 오른쪽으로 구슬 n을 삽입합니다.
        '''
        self.myPipe.append(n)

    def getBeads(self) :
        '''
        파이프의 배치를 list로 반환합니다.
        '''
        return self.myPipe
    
# pipe= ListPipe()
# # print(pipe.myPipe)
# pipe.addRight(1)
# pipe.addRight(2)
# pipe.addRight(3)
# pipe.addLeft(4)
# pipe.addLeft(5)
# print(pipe.getBeads())



def processBeads(myInput) :
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.

    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향

    예를 들어, 예제의 경우 

    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0

    입니다.

    '''
    '''여러줄 주석'''

    myPipe = ListPipe()

    result = []

    for bead, direction in myInput: # [[1,0](입력첫줄), [2,1](입력둘째줄),]
        if direction == 0: # 파이프 오른쪽이 0이면
            myPipe.addLeft(bead) #구슬을 왼쪽에 추가
        elif direction == 1:
            myPipe.addRight(bead)

    result = myPipe.getBeads()
    return result

def main():
    '''
    이 곳은 수정하지 마세요.
    '''

    n = int(input())

    print(f'{n}개의 줄이 올 예정입니다.')

    myList = []

    for i in range(n) :
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))

if __name__ == "__main__":
    main()