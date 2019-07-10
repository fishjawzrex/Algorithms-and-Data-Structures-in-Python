#import random
#random.seed(0)
class Graph:
  def __init__(self,vertices):
    self.v = vertices
    self.graph = [[0 for column in range(self.v)]for row in range(self.v)]

  def gmi(self,dist,spt):
    minval = float('inf')
    for i in range(self.v):
      if dist[i]<minval and spt[i]==False:
        minval = dist[i]
        minidx  = i
    return minidx 
  
  def printdist(self,dist):
    for i in range(self.v):
      print(i, " is ", dist[i], " units from source vertex")

  def AStar(self,src):
    dist = [float('inf')]*len(self.graph)
    dist[src] = 0
    dist2 = [float('inf')]*len(self.graph)

    h = [16,17,13,16,16,20,17,11,10,8,4,7,10,7,5,0]
    dist2[src]=h[src]
    spt = [False]*len(self.graph)
    for i in range(self.v):
      print(h[i])
    for i in range(self.v):
      u = self.gmi(dist2,spt)
      spt[u]=True 
      for v in range(self.v):
        if self.graph[u][v]>0 and spt[v]==False and dist2[v]>dist[u]+self.graph[u][v]+h[v]:
          dist[v]=dist[u]+self.graph[u][v]
          dist2[v]=dist[u]+self.graph[u][v]+h[v]

    self.printdist(dist2)

g = Graph(16) 
g.graph = [[0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,4,3,0,0, 0,0,0,0,0,0,0,0,0,0],[5,0,4,7,7,0,0,8,0,0,0,0,0,0,0,0],[0,3,7,0,0,0,0,11,0,0,16,13,14,0,0,0],[0,0,7,0,0,4,0,5,0,0,0,0,0,0,0,0],[0,0,0,4,0,0,9,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,9,0,0,0,0,0,0,0,12,0,0],[0,0,8,11,5,0,0,0,3,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,3,0,4,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,8],[0,0,0,16,0,0,0,0,0,0,0,5,0,7,0,4],[0,0,0,13,0,0,0,0,0,0,5,0,9,0,4,0],[0,0,0,14,0,0,0,0,0,0,0,9,0,0,5,0],[0,0,0,0,0,0,12,0,0,3,7,0,0,0,0,7],[0,0,0,0,0,0,0,0,0,0,0,4,5,0,0,0],[0,0,0,0,0,0,0,0,0,8,4,0,0,7,0,0]] 
  
g.AStar(0)