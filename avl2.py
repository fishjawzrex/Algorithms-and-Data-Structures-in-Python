class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    self.avl_ins=AVL()
    self.height = 1

class AVL:
  def insert(self,root,data):
    if not root:
      return Node(data)
    elif data<root.data:
      root.left = self.insert(root.left,data)
    else:
      root.right = self.insert(root.right,data)
    root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))
    balance = self.getBalance(root)
    if balance>1 and data<root.left.data:
      return self.rightRotate(root)
    if balance<-1 and data>root.right.data:
      return self.leftRotate(root)
    if balance>1 and data>root.left.data:
      root.left=self.leftRotate(root.left)
      return self.rightRotate(root)
    if balance<-1 and data<root.right.data:
      root.right=self.rightRotate(root.right)
      return self.leftRotate(root)
    return root 
  def leftRotate(self,z):
    y=z.right
    T2=y.left
      #perform leftRotate
    y.left = z
    z.right = T2
    z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))
    y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
    return y
  def rightRotate(self,z):
    y=z.left
    T2=y.right
      #perform leftRotate
    y.right = z
    z.left = T2
    z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))
    y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
    return y 
  def getHeight(self,root):
    if not root:
      return 0
    return root.height
  def getBalance(self,root):
    if not root:
      return 0
    return self.getHeight(root.left)-self.getHeight(root.right)
  def printdata(self,root):
    if root:
      self.printdata(root.left)
      print(root.data,root.height)
      self.printdata(root.right)
'''
root = None
tree = AVL()
for i in range(0,100,10):
  root=tree.insert(root,i)

tree.printdata(root)
'''
root = Node(15)
import random
#random.seed(0)
randList=random.sample(range(100),20)
for elem in randList:
  root=root.avl_ins.insert(root,elem)
#for elem in range(0,1000,10):
#  root=root.avl_ins.insert(root,elem)
root.avl_ins.printdata(root)
