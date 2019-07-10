from collections import defaultdict
import heapq
class Graph:
  def __init__(self,vertices):
    self.v = vertices
    self.graph = [[0 for column in range(self.v)] for row in range(self.v) ]

  

  def MCST(self, src):
    #res = []
    rex = []
    seen = set()
    adj_list = defaultdict(list)
    for i in range(self.v):
      for j in range(self.v):
        if self.graph[i][j]!=0:
          adj_list[i].append((self.graph[i][j],str(j)))
    #print(adj_list)
    seen.add(src)
    while len(rex)<self.v +1:
      #print(src)
      rex.append(src)
      res = []
      for elem in adj_list[src]:
        if int(elem[1]) not in seen:
          heapq.heappush(res, elem)
        #print(res)
      if not res:
        break 
      src = int(heapq.heappop(res)[1])
      #print(src)
      seen.add(src)
      
    #print(rex)
    return(rex)

g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0],[0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]] 
  
import numpy as np 
np.random.seed(0)
w = np.random.randint(20,size=(9,9))
#print(w)
for i in range(9):
  w[i][i]=0
#print(w) 
w2 = Graph(9)
w2.graph = w
for i in range(9):
  print(i, w2.MCST(i), len(w2.MCST(i)))