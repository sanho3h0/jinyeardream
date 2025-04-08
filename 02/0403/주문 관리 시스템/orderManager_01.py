# '''
# 1. LinkedListElement 클래스를 완성하세요.
# 2. orderManager 클래스를 완성하세요.
# '''

# class LinkedListElement :
#     def __init__(self, data, myPrev, myNext) :
#         self.data = data
#         self.myPrev = myPrev
#         self.myNext =  myNext

# class orderManager :
#     def __init__(self) :
#         self.start = None
#         self.end = None
#         self.elems = {}

#     def addOrder(self, orderId) :
#         element = LinkedListElement(orderId, None, None)
#             # element = LinkedListElement(data=orderId, myPrev=None, myNext=None)
        
#         self.elems[orderId] = element

#         # orderManamger 에 아무것도 없을 때 : 주문이 처음 추가될 경우
#         if self.start is None:
#             self.start = element
#             self.end = element
#         # 그렇지 않을 때 
#         else:
#             self.end.myNext = element
#             self.Myprev = self.end
#             self.end = element

#     # 무조건 orederId 가 self.data에 포함
#     '''
#     주문번호 100번을 지우고 싶다

#     1.연결리스트
#     맨 앞에 노드부터 하나씩 찾아서 (O(n))
#     주문번호가 100인지 아닌지 확인
#     100찾으면 제거

#     2. 연결리스트 + 해시 테이블
#     해시테이브에서 주문번호 찾아서 (O(1))
#     바로 제거

#     '''
#     def removeOrder(self, orderId):
#         if self.start == None and self.end == None:
#             return
        
#         current = self.elems[orderId]  # 삭제할 노드 찾기

#     # prevElem = current.myPrev  # 이전 노드
#     # nextElem = current.myNext  # 다음 노드
#     if prevElem != None:  # 이전 노드가 있으면, 이전 노드의 next를 삭제할 노드의 next로 연결
#         prevElem.myNext = nextElem

#     if nextElem != None:  # 다음 노드가 있으면, 다음 노드의 prev를 삭제할 노드의 prev로 연결
#         nextElem.myPrev = prevElem

#     if current == self.end:  # 삭제할 노드가 마지막 노드(end)라면, 이전 노드를 새로운 끝 노드로 설정
#         self.end = prevElem

#     if current == self.start:  # 삭제할 노드가 시작 노드(start)라면, 다음 노드를 새로운 시작 노드로 설정
#         self.start = nextElem


#     def getOrder(self, orderId) :
#         '''current = self.start로 시작 노드 저장 self.start 후 순회
#         현재 노드 (self.start) 부터 마지막 노드 (self.end)까지 순회하면서 노드값 (node.data)이 주문번호 (orderId)와 같은지 확인 후 인덱스 반환
#         마지막 노드(self.end)까지 없으면 -1 반환'''
#         cnt = 0
#         current = self.start

#         # 노드가 비어있기 전까지
#         while current != None:
#             # 노드값(current.data)이 주문번호 (orderId)와 같은지 확인
#             if current.data == orderId:
#                 return cnt +1
#             else: # 찾으려는 주문번호가 아니면 다음리스트 순회


# manager = orderManager()
# manager= addOrder(100)
# manager= addOrder(200)
# manager= addOrder(300)

# '''
# 연결리스트 는 순서/ 조회 느림
# 해시테이블 (딕셔너리) 는 조회는 빠르지만 순서는 x

# 파이썬의 딕셔너리
# 순서가 보장된 딕셔너리
# '''