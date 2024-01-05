from collections import deque
class node:
    def __init__(self, name = None):
        self.name = name
        self.parent = None
        self.children = None
def CreateTree(root):
    if root == None:
        root = node(input('Enter the name of the head of the family : '))
        Q.append(root)
    while(True):
        children = input(f"Enter the names of {Q[0].name}'s children : ").split(' ')
        if children[0] == '':
            Q.popleft()
            if len(Q) == 0:
                break
            continue
        children = list(map(node,children))
        for i in children:
             Q.append(i)
        Q[0].children = children
        for i in children:
            i.parent = Q[0]
        Q.popleft()
    return root

Q = deque()
root = None
root = CreateTree(root)
print(root.name)
