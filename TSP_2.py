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
c2 = [
[0,10,15,20],
[5,0,9,10],
[6,13,0,12],
[8,8,9,0]]

c =[
[0,2,0,6,1],
[1, 0 ,4 ,4 ,2],
[5, 3, 0, 1, 5],
[4, 7, 2, 0, 1],
[2, 6, 3, 6, 0]]

for i in range(len(c)+1):
  w.append(i)
src = 4
w.remove(0)
w.remove(src)
cache = perm(w)

for i in cache:
  i.insert(0,src)
  i.append(src)
print(cache)

from collections import defaultdict
cost = defaultdict(int)
min_val = float('inf')
for row in cache:
    for elem in row[:-1]:
      i = row[(row.index(elem)+1)%len(row)]
      if c[elem-1][i-1]!=0:
        cost[cache.index(row)]+=c[elem-1][i-1]
        if cost[cache.index(row)]>min_val:
          cost[cache.index(row)]=float('inf')
          break
      elif c[elem-1][i-1]==0 and elem!=i:
        cost[cache.index(row)]=float('inf')
        break
    if cost[cache.index(row)]<min_val:
      min_val = cost[cache.index(row)]
print(cost)
print(str(min(cost,key=cost.get))+ " : " + str(cost[min(cost,key=cost.get)]))
print(min_val)
'''
c2 =[
[0,2,0,6,1],
[1, 0 ,4 ,4 ,2],
[5, 3, 0, 1, 5],
[4, 7, 2, 0, 1],
[2, 6, 3, 6, 0]]
'''