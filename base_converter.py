cache = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def base(n,k):
  res = []
  while n>0:
    if n%k in cache:
      res.insert(0,cache[n%k])
    else:
      res.insert(0,str(n%k))
    n=n//k
  return ''.join(res)
print(base(2000,16))
'''
def rev_base(n,k):
  m,n = 0,str(n)
  L = len(n)
  for i in range(len(n)-1,-1,-1):
    if n[i] in cache2:
      m+=cache2[n[i]]*(k**(L-i-1))
    else:
      m+=int(n[i])*(k**(L-i-1))
  return m

print(rev_base(3E8,16))
'''