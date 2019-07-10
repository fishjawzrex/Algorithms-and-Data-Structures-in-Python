
def mergesort(arr):
  if len(arr)<=1:
    return arr
  med = len(arr)//2
  left = mergesort(arr[:med])
  right = mergesort(arr[med:])
  return merge(left, right)

def merge(l,r):
  res = []
  while l and r:
    if l[0]<r[0]:
      res.append(l[0])
      l.remove(l[0])
    else:
      res.append(r[0])
      r.remove(r[0])
  if len(l)==0:
    res = res + r
  else:
    res = res + l
  return res  

import random
w = random.sample(range(1000),200)
x = mergesort(w)
for i in x:
  print(i)
  