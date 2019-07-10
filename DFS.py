from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self,u,v):
    self.graph[u].append(v)

  def DFSUtil(self,v,visited):
    visited[v]=True
    print(v, end = ' ')
    for elem in self.graph[v]:
      if visited[elem]==False:
        self.DFSUtil(elem,visited)
  
  def make_adj(self,w):
    self.adj_list = defaultdict(list)
    for i in range(len(w)):
      for j in range(len(w)):
        if w[i][j]!=0:
          self.adj_list[i].append(j)
    return self.adj_list

  def DFS(self,v):
    visited = [False]*len(self.graph)
    self.DFSUtil(v,visited)



import numpy as np 
np.random.seed(0)
w = np.random.randint(20,size=(9,9))
#print(w)
for i in range(9):
  w[i][i]=0
print(w) 

x = Graph()
x.graph = x.make_adj(w)
#print(x.graph)
x.DFS(3)
print('\n')
z = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0],[0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]] 
y= Graph()
y.graph = y.make_adj(z)
y.DFS(8)
'''


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.DFS(2)
'''