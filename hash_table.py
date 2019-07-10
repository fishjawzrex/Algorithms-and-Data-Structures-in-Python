class HashTable:
  def __init__(self,size):
    self.size = size
    self.arr = [[None]]*size

  def insert(self,key,value):
    print(key,self.hash_value(key))
    if self.arr[self.hash_value(key)]!=[None]:
      flag = False
      for elem in self.arr[self.hash_value(key)]:
        if elem[0]== key:
          elem[1]=value
          flag = True
          break
      if not flag:
        self.arr[self.hash_value(key)].append([key,value])
    else:
      self.arr[self.hash_value(key)]=[[key,value]]

  def get_value(self,key):
    if len(self.arr[self.hash_value(key)])==1:
      return self.arr[self.hash_value(key)][0]
    elif  self.arr[self.hash_value(key)][0][0] == key:
      return self.arr[self.hash_value(key)][0]
    else:
      i = 0
      while self.arr[self.hash_value(key)][i][0] != key:
        i+=1
      return self.arr[self.hash_value(key)][i]

  def hash_value(self,item):
    hash_key = 0
    for elem in str(item):
      hash_key+=ord(elem)
      hash_key = hash_key%self.size
    return hash_key


'''
  def probe(self,h):
    count = 0
    temp = self.hash_value(h)
    while self.arr[temp]:
      count+=1
      new_val = (temp + count**2)%self.size
    return new_val
'''    

w = HashTable(8)
w.insert('Jones',12)
w.insert('West',22)
w.insert('Adam',52)
w.insert('Adam',46)
print(w.get_value('Jones'))
print(w.get_value('Adam'))
print(w.get_value('West'))

for i in w.arr:
  print(i)