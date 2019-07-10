def bs(lst):
  for i in range(len(lst)-1,0,-1):
    for j in range(i):
      if lst[j+1]<lst[j]:
        
        lst[j],lst[j+1] = lst[j+1],lst[j]


import random
w = random.sample(range(100),27)
print(w)
bs(w)
print(w)