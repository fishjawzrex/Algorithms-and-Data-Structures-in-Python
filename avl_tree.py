class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 1

class AVL:
  def insert(self,root,data):
    if not root:
      return Node(data)
    elif root.data>data:
      root.left = self.insert(root.left,data)
    elif root.data<data:
      root.right = self.insert(root.right,data)
    root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))
    balance = self.getBalance(root)
    if balance>1 and data<root.left.data:
      return self.rightRotate(root)
    if balance<-1 and data>root.right.data:
      return self.leftRotate(root)
    if balance>1 and data>root.left.data:
      root.left = self.leftRotate(root.left)
      return self.rightRotate(root)
    if balance<-1 and data<root.right.data:
      root.right = self.rightRotate(root.right)
      return self.leftRotate(root)
    return root
  def leftRotate(self,z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height= 1+max(self.getHeight(z.left),self.getHeight(z.right))
    y.height= 1+max(self.getHeight(y.left),self.getHeight(y.right))
    return y
  def rightRotate(self,z):
    y = z.left 
    T3 =y.right 
    y.right =z
    z.left = T3
    z.height= 1+max(self.getHeight(z.left),self.getHeight(z.right))
    y.height= 1+max(self.getHeight(y.left),self.getHeight(y.right))
    return y
  def getHeight(self,root):
    if not root:
      return 0
    return root.height
  def getBalance(self,root):
    if not root:
      return 0
    return self.getHeight(root.left)-self.getHeight(root.right)
  def iot(self,root):
    if root:
      self.iot(root.left)
      print(root.data,root.height)
      self.iot(root.right)

myTree = AVL() 
root = None
#for i in range(0,100,10):
#  root=myTree.insert(root, i)
import random
#random.seed(0)
randList=random.sample(range(100),20)
for elem in randList:
  root=myTree.insert(root,elem)

#root=myTree.insert(root, 25)

myTree.iot(root)



