class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

    def addNode(self, i, l, r) :
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        # 트리의 현재 노드 인덱스와 i가 일치할때 (혹은 비어있을떄)
        # addNode 성공
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None # Tree(None, None, None) X
            self.right = Tree(r, None, None) if r != None else None
            
        else: # 자식 탐색
            if self.left != None:
                self.left.addNode(i, l, r)
                
            if self.right != None:
                self.right.addNode(i, l, r)


tree = Tree(None, None, None)
tree.addNode(1, 2, 3)
tree.addNode(2, 4, 5)
tree.addNode(3, None, None)
tree.addNode(4, None, None)
tree.addNode(5, None, None)