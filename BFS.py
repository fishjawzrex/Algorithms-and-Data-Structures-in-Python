from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self,u,v):
    self.graph[u].append(v)
  
  def make_adj(self,w):
    adj_list = defaultdict(list)
    for i in range(len(w)):
      for j in range(len(w)):
        if w[i][j]!=0:
          adj_list[i].append(j)
    return adj_list

  def BFS(self,v):
    visited = [False]*len(self.graph)
    queue = []
    queue.append(v)
    seen = set()
    while queue:
      s = queue.pop(0)
      visited[s] = True
      print(s, end =' ')
      for elem in self.graph[s]:
        if visited[elem]==False:
          if elem not in seen:
            queue.append(elem)
            seen.add(elem)

import numpy as np 
np.random.seed(0)
w = np.random.randint(20,size=(9,9))
#print(w)
for i in range(9):
  w[i][i]=0
#print(w) 

x = Graph()
x.graph = x.make_adj(w)
print(x.graph)
print('\n')
x.BFS(0)
'''
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.BFS(2) 
'''