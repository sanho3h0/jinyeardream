'''
heapSort 함수를 구현하세요.
'''
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
        heapq.heappush(self.data, value)
    
    def top(self) :
        '''우선순위가 가장 높은 원소를 반환한다.'''
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0]

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) > 0:
            heapq.heappop(self.data)


def heapSort(items) :
    '''
    items에 있는 원소를 heap sort하여 리스트로 반환하는 함수를 작성하세요.

    단, 이전에 작성하였던 priorityQueue를 이용하세요.
    '''

    result = []

    pq = PriorityQueue()

    for item in items :
        pq.push(item)

    for i in range(len(items)):
        result.append(pq.top())
        pq.pop()

    return result

nums = list(map(int,input().split()))
result = heapSort(nums)
print(result)