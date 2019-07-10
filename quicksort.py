import random
arr = random.sample(range(100), 30)
low = 0
high = len(arr)-1

def part(arr, low, high):
  i = low + 1
  j = high
  pivot = arr[low]
  while i<=j:
    while arr[i]<pivot and i<high:
      i+=1
    while arr[j]>pivot:
      j-=1
    if i<j:
      arr[i], arr[j] = arr[j], arr[i]
    else:
      i+=1 #need this to push pointer past j in order to break out of while loop
  arr[low],arr[j]=arr[j],arr[low]#swap pointer(new piv loc) and old pivot
  return j 

def quick(arr,low,high):
  if low>=high:
    return
  piv_loc = part(arr,low,high)
  quick(arr,low,piv_loc-1)
  quick(arr,piv_loc+1,high)

quick(arr,low,high)
for i in arr:
  print(i)