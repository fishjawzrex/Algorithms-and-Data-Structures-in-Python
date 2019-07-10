def heapify(arr,n, i):
  l = 2*i+1
  r = 2*i+2
  largest =  i
  if l<n and arr[i]<arr[l]:
    largest = l
  if r<n and arr[largest]<arr[r]:
    largest  = r

  if largest!=i:
    arr[i],arr[largest]=arr[largest],arr[i]
    heapify(arr,n, largest) #recursively call with swapped largest to make sure the children
                            #are also heapified

def heapsort(arr):
  w = len(arr)
  for i in range(int(w/2-1),-1,-1):
    heapify(arr,w, i)#heapify from middle node up until zero index
  for i in range(len(arr)-1,0,-1):
    arr[i],arr[0]=arr[0],arr[i]#swap max value in array with bottom node
    heapify(arr,i,0)#decrease length of array and run heapify
import random
z = random.sample(range(100),15)
for i in z:
  print(i)
heapsort(z)
print("\n")
for i in z:
  print(i)
