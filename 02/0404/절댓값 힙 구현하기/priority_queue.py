import heapq
class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = []

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        heapq.heappush(self.data, (abs(value),value))
        # 튜플끼리 비교하기 위해 왼쪽에는 절댓값, 오른쪽은 원래 값
        # 시퀀스 자료형의 값을 비교할 때 왼쪽먼저 비교하기 때문
        # (1,10000) < (2,13) 출력값 True

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) > 0:
            heapq.heappop(self.data)

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0][1]
        
pq = PriorityQueue()
pq.push(5)
pq.push(-4)
pq.push(3)
pq.push(-1)
print(pq.data)
pq.pop()
print(pq.data)
print(pq.top())
pq.pop()
print(pq.top())

