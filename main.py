from collections import deque
class node:
    def __init__(self, name = None):
        self.name = name
        self.parent = None
        self.children = None
        self.level = None
def CreateTree(root):
    if root == None:
        root = node(input('Enter the name of the head of the family : '))
        root.level = 1
        dict_data[root.name] = root
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
            i.level = i.parent.level + 1
            dict_data[i.name] = i
        Q.popleft()
    return root
def check_parent(first_name,second_name):
    first_person=dict_data[first_name]
    second_person=dict_data[second_name]
    while(first_person.level<second_person.level):
        second_person=second_person.parent
    if second_person.name==first_person.name:
        return True
    else:
        return False
def check_sibling(first_name,second_name):
    if dict_data[first_name].parent and dict_data[second_name].parent:
        if dict_data[first_name].parent.name==dict_data[second_name].parent.name:
            return True
    return False
def not_close(first_name,second_name):
    if not dict_data[first_name].parent:
        if check_parent(first_name,second_name):
            return False
    if not dict_data[second_name].parent:
        if check_parent(second_name,first_name):
            return False
    if check_parent(first_name,second_name) or check_parent(second_name,first_name) or check_sibling(first_name,second_name):
        return False
    return True
dict_data = {}
Q = deque()
root = None
root = CreateTree(root)
print(root.name)
print(not_close('1','2'))
print(not_close('5','6'))