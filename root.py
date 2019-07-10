
def root(n):
  low = 0 
  high = n
  epsilon = .0001
  def root2(n,low,high,epsilon):
    mid = (low + high)/2
    #print(mid)
    if abs(mid**2-n)<= epsilon:
      return mid
    elif mid**2>n:
      #high = mid
      return root2(n,low,mid,epsilon)
    elif mid**2<n:
      #low = mid
      return root2(n,mid,high,epsilon)
  return root2(n,low,high,epsilon)

#for i in range(26): 
#  print(i, round(root(i),2))