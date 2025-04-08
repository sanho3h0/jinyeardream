'''
엘리스씨를 도와 n개의 점토를 하나의 덩이로 합치기 위해 필요한 힘의 크기의 합의 최솟값을 구하는 프로그램을 작성하세요.

만약 무게가 a인 점토와 무게가 b인 점토를 한 덩이가 되도록 합치기 위해서는 a+b의 힘을 들여야 합니다.

4개의 점토가 있고 각각 1, 5, 7, 3의 무게를 가진다면 다음의 순서대로 합치는 것이 최소가 됩니다.

먼저 1과 3을 합칩니다. 합쳐진 점토의 크기는 4가 되고, 힘 4가 필요합니다.
그 후 4와 5를 합칩니다. 합쳐진 점토의 크기는 9가 되고, 힘 9가 필요합니다.
그 후 마지막으로 7과 9를 합치면, 결과적으로 한 덩이가 남게 되고, 이 때는 힘 16이 필요합니다.

따라서 이 모든 점토를 한 덩이로 합치기 위해 필요한 힘의 크기는 4 + 9 + 16 = 29 입니다

'''

import heapq

def getMinForce(weights) :
    '''
    n개의 점토를 하나로 합치기 위해 필요한 힘의 합의 최솟값을 반환하는 함수를 작성하세요.
    '''

    pq = []

    # heapq, heappush()
    
    for w in weights:
        heapq.heappush(pq, w)

    result = 0

    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)

        temp = x + y
        result = result + temp

        heapq.heappush(pq, temp)
        
    return result

# import heapq

# def getMinForce(weights) :
#     '''
#     n개의 점토를 하나로 합치기 위해 필요한 힘의 합의 최솟값을 반환하는 함수를 작성하세요.
#     '''

#     heapq.heapify(weights)

#     result = 0

#     # 점토가 하나 남을 때 까지
#     while len(weights) > 1:
#         x = heapq.heappop(weights)
#         y = heapq.heappop(weights)
#         temp = x + y
