def prime(n):
  res = []
  for j in range(n+1):
    res.append(j)
  for i in range(2,int(n**.5)):
    for elem in res:
      if elem%i==0 and elem!=i:
        res.remove(elem)

  return res,len(res)
print(prime(100000))