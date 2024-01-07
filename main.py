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
        root.parent = node(None)
        root.parent.name=''
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
    if dict_data[first_name].parent.name==dict_data[second_name].parent.name:
        return True
    return False
def not_close(first_name,second_name):
    if check_parent(first_name,second_name) or check_parent(second_name,first_name) or check_sibling(first_name,second_name):
        return False
    return True
def furthest_child(person):
    if person.children:
        return 1+max(list(map(furthest_child,person.children)))
    return 0
def lowest_common_ancestor(first_name,second_name): 
    first_person=dict_data[first_name] 
    second_person=dict_data[second_name] 
    while(first_person.level<second_person.level): 
        second_person=second_person.parent 
    while(first_person.level>second_person.level): 
        first_person=first_person.parent 
    while(first_person.parent.name != second_person.parent.name): 
        first_person=first_person.parent 
        second_person=second_person.parent 
    return first_person.parent.name
def furthest_relation():
    max=furthest_child(root)
dict_data = {}
Q = deque()
root = None
root = CreateTree(root)