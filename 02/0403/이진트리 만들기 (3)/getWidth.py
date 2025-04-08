def inorder(tree, depth):
    result = [] #[4,2,5,1,3]

    # 왼쪽 서브트리 순회
    if tree. left != None: # 왼쪽 서브트리
        result = result + inorder(tree.left, depth +1)
    # 루트 (본인) 추가
    tree.setDepth(depth)
    result.append(tree)

def getWidth(myTree) :
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.
    
    반환값 형식 : (l, w)
    '''
    result = inorder(myTree, 1) #[Tree(), Tree()..]     
    print("Inorder result (노드 순서):"), # [(node.Index, node.depth)]
    n = len(result) # 전체 노드의 개수

    # 가장 왼쪽에 있는 노드, 가장 오른쪽 노드의 인덱스를 기록
    left = [1001] * 1000 # left [d] : depth가 d인 노드 중 가장 왼쪽에 있는 노드의 인덱스
    right = [-1] * 1000
    maxDepth = 0 # 트리에서 등장한 최대 Depth 

    # depth별 가장 왼쪽 / 오른쪽 노드 찾기
    for i in range(n):
        d = result[i].depth

        # 더 값이 작은게 있으면 최신화
        left[d] = min(left[d], i)
        right[d] = max(right[d], i)
        maxDepth = max(maxDepth, d)
        # print(f"{result[i]} at index {i} with depth {d}")
        # print(f"{left[i]} = {left[d]} , rigth[{d}] = {right[d]}")
        # print(left[:5])
        # print(right[:5])

    ansDepth = 0 # 너비가 가장 넓은 레벨 번호
    ansWidth = 0 # 너비가 가장 넓은 레벨의 너비 값

    for i in range(1, maxDepth+1):
        temp = right[i] - left[i] + 1

        if ansWidth < temp:
            ansDepth = i
            ansWidth = temp
    return (ansDepth, ansWidth)