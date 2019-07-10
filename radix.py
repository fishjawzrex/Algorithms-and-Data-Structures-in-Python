def cs(arr,exp1):
  n = len(arr)
  count = [0]*10  #create count array
  output = [0]*n  #create output array
  for i in range(n):
    index = arr[i]//exp1
    count[index%10]+=1

  for i in range(1,10):
    count[i]+=count[i-1]
  
  i = n-1
  while i>=0:
    index = arr[i]//exp1
    output[count[index%10]-1]= arr[i] # you need to reindex because the last element
                                      #is going to be in position n, which is out of range!
    count[index%10]-=1
    i-=1

  for i in range(n):
    arr[i]=output[i]

def rads(arr):
  max1 = max(arr)
  exp = 1
  while max1/exp >=1:
    cs(arr,exp)
    exp *= 10

import random
w = random.sample(range(200), 50)
rads(w)
for i in range(len(w)):
  print(w[i])