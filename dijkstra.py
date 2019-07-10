class Graph:
  def __init__(self,vertices):
    self.v = vertices
    self.graph = [[0 for column in range(self.v)] for row in range(self.v) ]

  def printResult(self,dist):
    for i in range(self.v):
      print(i, dist[i])

  def get_min_index(self, dist, sptSet):
    minval = float('inf')
    for v in range(self.v):
      if dist[v]<minval and sptSet[v]==False:
        minval = dist[v]
        min_index = v
    return min_index

  def dijkstra(self, src):
    dist = [float('inf')]*self.v
    dist[src]=0
    sptSet = [False]*self.v
    for c in range(self.v): 
      u = self.get_min_index(dist,sptSet)
      sptSet[u]=True
      for v in range(self.v):
        if self.graph[u][v]>0 and sptSet[v]==False and dist[v]>dist[u]+self.graph[u][v]:
          dist[v]=dist[u]+self.graph[u][v]
    self.printResult(dist)

g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0],[0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]] 
  
g.dijkstra(0)