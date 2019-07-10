def ins(lst):
  for i in range(1,len(lst)):
    j=i-1
    temp = lst[i]
    while j>=0 and lst[j]>temp:
      lst[j+1] = lst[j]
      j-=1  #after j reaches 0, in while loop, this decrement makes j = -1
    #lst[j+1]=temp#the correction is made to put temp in previous index(0)

import random
w = random.sample(range(100),27)
print(w)
ins(w)
print(w) 