class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''

    def __init__(self) :
        self.data = [0]

        '''
        우선순위 큐에 value를 삽입합니다.
        '''
    def push(self, value) :
        # 값 넣기
        self.data.append(value)
        # 트리 조정
        # 인덱스 찾기
        index = len(self.data) - 1
        # 만약 부모가 자식보다 값이 크다면 
        while index != 1:
            parent_idx = index // 2  # if index:4 -> 2, index:5 -> 2
            # (부모가 더 작으면 교환)
            if self.data[parent_idx] < self.data[index]:
                # 값 교환 방법 1
                tmp = self.data[index]
                self.data[index] = self.data[parent_idx]
                self.data[parent_idx] = tmp

                # 값 교환 방법 2
                # self.data[index], self.data[parent_idx] = (
                #     self.data[parent_idx], self.data[index] 
                # )
                index = parent_idx
            else:
                break

    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) == 1: # 0번 인덱스만 있을때
            return
        
        # 루트와 마지막 노드 교환
        self.data[1] = self.data[-1]

        # 마지막 노드(원래 루트 노드, 최솟값) 뺌
        self.data.pop()
        
        index = 1 # 루트 인덱스 

        # 부모가 자식보다 작을때까지 교환
        while True:
            priority = -1 # 둘 중 교환할 자식의 인덱스 (왼쪽자식, 오른쪽자식, 둘다아님)
            left_child_index = index * 2 # 왼쪽
            right_child_index = index * 2 + 1 # 오른쪽

            # 1. 왼쪽 자식이 없는 경우 (왼쪽자식이 없으면 오른쪽 무조건 x)
            if len(self.data) - 1 < left_child_index: # [0, 1] 2 - 1 < 2 
                break
            
            # 2. 왼쪽 자식만 있는 경우
            elif len(self.data) - 1 < right_child_index:
                priority = left_child_index # 왼쪽 자식만 있으니, 왼쪽자식이 바꿔줄 후보

            # 3. 양쪽 자식이 있는 경우
            else: # 둘 중 더 큰 값을 바꿔줄 후보로 선정 (큰값을 부모로)
                if self.data[left_child_index] > self.data[right_child_index]:
                    priority = left_child_index
                else:
                    priority = right_child_index
            
            # 선택된 후보 자식이 현재 노드보다 **크면 교환
            if self.data[index] < self.data[priority]:
                tmp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = tmp
                index = priority
            else:
                break

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''
        if len(self.data) == 1: # 0번 인덱스만 있을때
            return -1
        else:
            return self.data[1]


priority_queue = PriorityQueue()
priority_queue.push(1)
print(priority_queue.data)
priority_queue.push(4)
print(priority_queue.data)
priority_queue.push(3)
print(priority_queue.data)
priority_queue.push(2)
print(priority_queue.data)
priority_queue.top()
priority_queue.pop()
print(priority_queue.data)
priority_queue.top()
priority_queue.pop()
print(priority_queue.data)