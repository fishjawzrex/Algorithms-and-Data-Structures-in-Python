def paren(n):
  def helper(l,r,item,res):
    if l>r:
      return
    if l==0 and r==0:
      res.append(item)
    if l>0:
      helper(l-1,r,item+'(',res)
    if r>0:
      helper(l,r-1,item+')',res)
    return res
  return helper(n,n,'',[])

print(paren(3))