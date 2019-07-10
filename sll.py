class Node:
  def __init__(self, dataval):
    self.dataval = dataval
    self.nextval = None

class SLL:
  def __init__(self):
    self.headval = None

  #traverse and print
  def printval(self):
    printval = self.headval
    while printval != None:
      print(printval.dataval)
      printval = printval.nextval
  #insert node at the top 
  def atb(self, new_data):
    NewNode = Node(new_data)
    NewNode.nextval = self.headval
    self.headval = NewNode
  def atm(self, mid_node, new_data):
    NewNode = Node(new_data)
    if mid_node == None:
      print('no such node')
      return
    NewNode.nextval = mid_node.nextval
    mid_node.nextval = NewNode

  def ate(self, new_data):
    NewNode = Node(new_data)
    if self.headval == None:
      self.headval = NewNode
    prev = self.headval
    while prev.nextval != None:
      prev = prev.nextval
    prev.nextval = NewNode

  def del_node(self, data):
    curr = self.headval
    if curr.dataval == data:
      self.headval = curr.nextval
      curr = None
      return
    while curr.dataval != data:
      prev = curr
      curr = curr.nextval
    if curr == None:
      print("NSV")
      return
    prev.nextval = curr.nextval
    curr = None

e,f,g = Node('Mon'), Node('Wed'), Node('Thurs')

list1 = SLL()
list1.headval = e
e.nextval = f
f.nextval = g
list1.atm(e, 'Tuesday')
list1.atb('Sunday')
list1.ate('Friday')
list1.del_node('Wed')
list1.printval()