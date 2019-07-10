def ss(lst):
  for i in range(len(lst)):
    min_idx = i
    for j in range(i+1, len(lst)):
      if lst[j]<lst[min_idx]:
        min_idx = j
    lst[min_idx],lst[i]=lst[i],lst[min_idx]

import random
w = random.sample(range(100),27)
print(w)
ss(w)
print(w)
