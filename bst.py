class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def insert(self, new_data):
    if self.data != None:
      if self.data > new_data:
        if self.left == None:
          self.left = Node(new_data)
        else:
          self.left.insert(new_data)
      if self.data < new_data:
        if self.right == None:
          self.right = Node(new_data)
        else:
          self.right.insert(new_data)
    else:
      self.data = new_data

  def PrintTree(self):
    if self.left != None:
      self.left.PrintTree()
    print(self.data)
    if self.right != None:
      self.right.PrintTree()

  def iot(self, root):
    res = []
    if root != None:
      res = self.iot(root.left)
      res.append(root.data)
      res = res + self.iot(root.right)
    return res 

  def findval(self, lkpval):
    if self.data > lkpval:
      if self.left == None:
        return str(lkpval) + " Not found."
      return self.left.findval(lkpval)
    elif self.data < lkpval:
      if self.right == None:
        return str(lkpval) + " Not found."
      return self.right.findval(lkpval)
    else:
      print("%r found." % lkpval)

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
print(root.iot(root))

print(root.findval(7))
print(root.findval(14))