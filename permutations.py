res = []
def perm(a,l,r):
  if l==r:
    res.append(a[:])
    #print(a)
  else:
    for i in range(l,r):
      a[i],a[l]=a[l],a[i]
      perm(a,l+1,r)
      a[i],a[l]=a[l],a[i]
  return res 
a = list('ABCD')
n = len(a)

print(perm(a,0,n))