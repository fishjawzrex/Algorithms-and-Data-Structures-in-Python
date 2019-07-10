def perm(a):
  r=len(a)
  l=0
  res = []
  def helper(a,l,r):
    if l==r:
      res.append(a[:])
    for i in range(l,r):
      a[i],a[l]=a[l],a[i]
      helper(a,l+1,r)
      a[i],a[l]=a[l],a[i]
    return res 
  return helper(a,l,r)

w = []
c = [
[0,10,15,20],
[5,0,9,10],
[6,13,0,12],
[8,8,9,0]]
for i in range(5):
  w.append(i)

x = w[2:]

cache = perm(x)
for i in cache:
  i.insert(0,1)
  i.append(1)
print(cache)
from collections import defaultdict
cost = defaultdict(int)
for row in cache:
    for elem in row[:-1]:
      #print(elem)
      i = row[(row.index(elem)+1)%len(row)]
      #print(i)
      if c[elem-1][i-1]!=0:
        cost[cache.index(row)]+=c[elem-1][i-1]
        print(c[elem-1][i-1])
      elif c[elem-1][i-1]==0 and elem!=i:
        cost[cache.index(row)]=float('inf')
        break

print(cost)
print(min(cost,key=cost.get))
