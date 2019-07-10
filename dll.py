class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.nextval = None 
class DLL: 
  def __init__(self):
    self.head = None
  def append(self,data):
    New = Node(data)
    if not self.head:
      self.head = New
      New.prev = self.head
    curr = self.head
    while curr.nextval:
      curr = curr.nextval
    curr.nextval = New
    New.prev = curr 
  def printlist(self):
    curr = self.head
    while curr:
      print(curr.data)
      curr=curr.nextval
  def push(self,data):
    New = Node(data)
    if not self.head:
      self.head = New
      New.prev = self.head
    New.nextval = self.head
    self.head.prev = New
    self.head = New 
  def insert(self,node,data):
    New = Node(data)
    curr = self.head
    while curr.data!=node.data:
      curr = curr.nextval
    New.nextval = curr.nextval
    curr.nextval = New
    New.prev = curr
  def delete(self,data):
    curr = self.head
    if curr.data == data:
      self.head = curr.nextval
      curr.nextval.prev = self.head
      curr = None
    while curr.data!=data:
      prev1 = curr
      curr = curr.nextval
    prev1.nextval = curr.nextval
    curr.nextval.prev = prev1
    curr = None
  def reverse(self):
    curr = self.head
    stack = []
    while curr:
      stack.append(curr.data)
      curr=curr.nextval
    curr = self.head
    while stack:
      curr.data = stack.pop()
      curr = curr.nextval


e,f,g=Node('Mon'),Node('Wed'),Node('Thur')
e.nextval = f
f.prev = e
f.nextval =g
g.prev = f 
w=DLL()
w.head=e
w.append('Fri')
w.push('Sun')
w.insert(e,'Tue')
w.delete('Wed')
w.reverse()
w.printlist()