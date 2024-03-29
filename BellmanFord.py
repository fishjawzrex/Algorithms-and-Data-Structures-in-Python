class Graph:
  
  def __init__(self,vertices):
    self.v = vertices
    self.graph = []

  def addEdge(self,u,v,w):
    self.graph.append([u,v,w])

  def printArr(self,dist):
    print("Vertex Distance from source")
    for i in range(self.v):
      print("%d \t\t %d" % (i,dist[i]))


  def BellmanFord(self, src):
    dist = [float('inf')]*self.v
    dist[src]=0

    for i in range(self.v -1):
      for u,v,w in self.graph:
        if dist[u]!=float('inf') and dist[v]>dist[u]+w:
          dist[v]=dist[u]+w
    for u,v,w in self.graph:
        if dist[u]!=float('inf') and dist[v]>dist[u]+w:
          print("Graph contains negative weight cycle!")
          return
    self.printArr(dist)

g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
  
#Print the solution 
g.BellmanFord(0) 