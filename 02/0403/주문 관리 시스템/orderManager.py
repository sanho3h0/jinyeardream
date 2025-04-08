# '''
# 1. LinkedListElement 클래스를 완성하세요.
# 2. orderManager 클래스를 완성하세요.
# '''

# class LinkedListElement :
#     def __init__(self, data, myPrev, myNext) :
#         self.myPrev = myPrev
#         self.myNext =  myNext

# class orderManager :
#     def __init__(self) :
#         self.start = None
#         self.end = None

#     def addOrder(self, orderId) :
#         # orderManamger 에 아무것도 없을 때
#         if self.start is None and self.edn is None:
#             element = LinkedListElement(data=orderId, myPrev=None, myNext=None)
#             # 이전 노드
#             self.end.myNext = element
#             self.end = element
#         # 그렇지 않을 때 
#         else:
#             element = LinkedListElement(data=orderId, myPrev=self.end, myNext=None)
#             self.end.myNext = element
#             self.end = element

#     # 무조건 orederId 가 self.data에 포함
#     def removeOrder(self, orderId) :
#         current = self.start

#         while current != None:
#             # 노드 하나씩 순회 만약에 노드를 만나면 삭제
#             if current.data == orderId:
#             # 삭제할 노드의 이전, 다음노드를 저장
#                 prevElem = current.



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
# 위 코드는 효율성이 좋지 않다.
# 시간복잡도?
# 딕셔너리를 활용할 것.

# '''