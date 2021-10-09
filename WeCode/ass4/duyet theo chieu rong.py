class Node:
    def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data
class Tree:
       def __init__(self):
           self.root = None        
       def insert_node(self,root,element):
           if self.root is None:
               self.root = Node(element)
           else:
               if root is None:
                   root = Node(element)
               elif root.data < element:
                   root.right = self.insert_node(root.right,element)
               elif root.data > element:
                   root.left = self.insert_node(root.left,element)
           return root
       def findHeight(self, root):
           if root is None: 
               return 0
           return 1 + max(self.findHeight(root.left), self.findHeight(root.right))
       def Breadth(self,root,h1,h):
           if root is not None:
               if h1 == h :
                    print(root.data, end = " ")
               if root.left is not None and h1 < h:
                    self.Breadth(root.left, h1 + 1, h)
               if root.right is not None and h1 < h:
                    self.Breadth(root.right, h1 + 1, h)
a = Tree()
while 1:
    x = (input())
    if x == "0":
        break
    a.insert_node(a.root,int(x))
height = a.findHeight(a.root)
for i in range (height):
    a.Breadth(a.root,0, i)