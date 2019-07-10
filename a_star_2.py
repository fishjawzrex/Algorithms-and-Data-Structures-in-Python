#import random
#random.seed(0)
class Graph:
  def __init__(self,vertices):
    self.v = vertices
    self.graph = [[0 for column in range(self.v)]for row in range(self.v)]

  def gmi(self,dist,spt):
    minval = float('inf')
    global minidx
    for i in range(self.v):
      if dist[i]<minval and spt[i]==False:
        minval = dist[i]
        minidx  = i
    return minidx 
  
  def printdist(self,dist,dist2,h):
    print("i g  f  h")
    for i in range(self.v):
      print(i, dist[i],dist2[i],h[i])
     

  def AStar(self,src):
    dist = [float('inf')]*len(self.graph)
    dist[src] = 0
    dist2 = [float('inf')]*len(self.graph)

    h = [16,17,13,16,16,20,17,11,10,8,4,7,10,7,5,0]
    dist2[src]=h[src] # dist2[u] = dist[u]==0 + h[u]
    spt = [False]*len(self.graph)
    w=[] #this is where we append the path based on the min selected vertices
    print('\n')
    for i in range(self.v):

      u = self.gmi(dist2,spt)
      if h[u]==0:
        break     #Terminate the procedure once we have reached destination
      #print(u, end=' ')
      
      w.append(u)
      spt[u]=True 
      for v in range(self.v):
        if self.graph[u][v]>0 and spt[v]==False and dist2[v]>dist[u]+self.graph[u][v]+h[v]: 
          dist[v]=dist[u]+self.graph[u][v]
          dist2[v]=dist[u]+self.graph[u][v]+h[v]

    print('\n')
    print("PATH: ")
    print(w)
    print("TABLE: ")
    self.printdist(dist, dist2,h)

g = Graph(16) 
g.graph = [[0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,4,3,0,0, 0,0,0,0,0,0,0,0,0,0],[5,0,4,7,7,0,0,8,0,0,0,0,0,0,0,0],[0,3,7,0,0,0,0,11,0,0,16,13,14,0,0,0],[0,0,7,0,0,4,0,5,0,0,0,0,0,0,0,0],[0,0,0,4,0,0,9,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,9,0,0,0,0,0,0,0,12,0,0],[0,0,8,11,5,0,0,0,3,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,3,0,4,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,4,0,0,0,0,3,0,8],[0,0,0,16,0,0,0,0,0,0,0,5,0,7,0,4],[0,0,0,13,0,0,0,0,0,0,5,0,9,0,4,0],[0,0,0,14,0,0,0,0,0,0,0,9,0,0,5,0],[0,0,0,0,0,0,12,0,0,3,7,0,0,0,0,7],[0,0,0,0,0,0,0,0,0,0,0,4,5,0,0,0],[0,0,0,0,0,0,0,0,0,8,4,0,0,7,0,0]] 
  
g.AStar(0)