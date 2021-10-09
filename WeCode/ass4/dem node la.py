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

data = int(input())
root = node(data)
while True:
    x = int(input())
    if x == 0:
        break
    root.Insert(x)

def Count_Leaf(node): 
    if node is None: 
        return 0 
    if(node.left is None and node.right is None): 
        return 1 
    else: 
        return Count_Leaf(node.left) + Count_Leaf(node.right) 

num = Count_Leaf(root)
print(num)