from sys import stdin
class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def Insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = node(data)
            else:
                self.left.Insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = node(data)
            else:
                self.right.Insert(data)
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        elif self.right:
            self.right.PrintTree()

def FindHeight(node):
    if node is None:
        return 0
    else:
        left = FindHeight(node.left)
        right = FindHeight(node.right)
    
    if left > right:
        return left + 1
    else:
        return right + 1

list = []
while True:
    a = [int(i) for i in stdin.readline().split()]
    if a[0] == 0:
        try:
            position = list.index(a[1])
            list.pop(position)
            list.insert(0,a[1])
        except:
            list.insert(0,a[1])
    elif a[0] == 1:
        if a[1] not in list:
            list.append(a[1])
    elif a[0] == 2:
        try:
            position1 = list.index(a[1])
            if a[2] in list:
                position2 = list.index(a[2])
                if position1 < position2:
                    list.pop(position2)
                    list.insert(position1 + 1,a[2])
            else:
                list.insert(position1 + 1,a[2])
        except:
            list.insert(0,a[2])
    else:
        root = node(list[0])
        break

for i in range(1,len(list)):
    root.Insert(list[i])
print(FindHeight(root))