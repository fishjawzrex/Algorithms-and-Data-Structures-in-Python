from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self,u,v):
    self.graph[u].append(v)

  def DFSUtil(self,v,visited,stack,stack2):
    visited[v]=True
    stack.append(v)
    print(v,end=' ')
    seen = set(stack2)
    for i in range(len(self.graph)):
      if set(self.graph[i])<=set(stack) and i not in seen:
        seen.add(i)
        stack2.append(i)
    for i in self.graph[v]:
      if visited[i]==False:
        self.DFSUtil(i, visited,stack,stack2)

  def DFS(self,v):
    stack = []
    stack2 = []
    visited = [False]*len(self.graph)
    self.DFSUtil(v,visited,stack,stack2)
    print(stack)
    print('\n')
    print(stack2)
obj = defaultdict(list)
graph = [[0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,4,3,0,0, 0,0,0,0,0,0,0,0,0,0],[5,0,4,7,7,0,0,8,0,0,0,0,0,0,0,0],[0,3,7,0,0,0,0,11,0,0,16,13,14,0,0,0],[0,0,7,0,0,4,0,5,0,0,0,0,0,0,0,0],[0,0,0,4,0,0,9,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,9,0,0,0,0,0,0,0,12,0,0],[0,0,8,11,5,0,0,0,3,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,3,0,4,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,8],[0,0,0,16,0,0,0,0,0,0,0,5,0,7,0,4],[0,0,0,13,0,0,0,0,0,0,5,0,9,0,4,0],[0,0,0,14,0,0,0,0,0,0,0,9,0,0,5,0],[0,0,0,0,0,0,12,0,0,3,7,0,0,0,0,7],[0,0,0,0,0,0,0,0,0,0,0,4,5,0,0,0],[0,0,0,0,0,0,0,0,0,8,4,0,0,7,0,0]] 
for i in range(len(graph)):
  for j in range(len(graph)):
    if graph[i][j]!=0:
      obj[i].append((j))
print(obj)

g = Graph()
g.graph = obj
g.DFS(0)