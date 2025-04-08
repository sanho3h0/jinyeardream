import heapq
def find_mid(nums) :
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    
    n = len(nums)
    result = [] # 각 단계의 중간값
    # 최대합
    left = []  # 중간값이 루트. 중간값과 같거나 작은 값들
    # 최소합
    right = [] # 중간값보다 큰 값들
    # [left' '][right] 
    
    # 최대
    for i in range(n) :
        x = nums[i] # 현재 숫자

        # 합이 비어있는 경우 최대 합에 삽입
        if not left or not right:
            heapq.heappush(left, -x)
        else:
            if x >= right[0]:
                heapq.heappop(right, x)
            else: # 중간값과 대소비교
                heapq.heappush(left, -x)

    # 항상 최대힙과 최소힙은 길이가 같거나, 최대합이 하나 더 많아야한다.
    while not (len(left) == len(right) or len(left) == len(right) +1):
        # 최대합의 요소가 너무 많으면 최소합으로 이동
        if len(left) > len(right) :
            heapq.heappush(right, -heapq.heappop(left))
        else:
            heapq.heappush(right, -heapq.heappop(right))

        result.append(-left[0])

nums = list(map(int, "1 -2 -5 10 4 7 5".split())) # 입력을 미리 받아줌
find_mid(nums=nums)  # 1 -2 -2 -2 1 1 4