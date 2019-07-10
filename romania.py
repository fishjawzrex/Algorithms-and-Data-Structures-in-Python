from collections import defaultdict
adj = defaultdict(list)
cat = ['Arad','Bucharest','Craiova','Dobreta',
'Eforie',
'Fagaras',
'Giurgiu',
'Hirsova',
'Iasi',
'Lugoj',
'Mehadia',
'Neamt',
'Oradea',
'Pitesti',
'Rimnicu_Vilcea',
'Sibiu',
'Timisoara',
'Urziceni',
'Vaslui',
'Zerind']
cat2 = {0:'Arad',1:'Bucharest',2:'Craiova',3:'Dobreta',
4:'Eforie',
5:'Fagaras',
6:'Giurgiu',
7:'Hirsova',
8:'Iasi',
9:'Lugoj',
10:'Mehadia',
11:'Neamt',
12:'Oradea',
13:'Pitesti',
14:'Rimnicu_Vilcea',
15:'Sibiu',
16:'Timisoara',
17:'Urziceni',
18:'Vaslui',
19:'Zerind'}
dic = {}
for i in range(len(cat)):
  dic[cat[i]]=i 
#print(dic) 
heur = [366,0,160,242,161,176,77,151,226,244,241,234,380,10,193,253,329,80,199,374]
adj = {0:[(15,18),(16,140),(19,75)],1:[(6,90),(13,101),(5,211),(17,85)],2:[(3,120),(14,148),(13,138)],3:[(2,120),(10,75)],4:[(7,86)],5:[(1,211),(15,99)],6:[(1,90)],7:[(4,86),(17,98)],8:[(11,87),(18,92)],9:[(10,70),(16,111)],10:[(3,75),(9,70)],11:[(8,87)],12:[(15,151),(19,71)],13:[(1,101),(2,138),(14,97)],14:[(2,146),(13,97),(15,80)],15:[(0,140),(5,99),(12,151),(14,80)],16:[(0,118),(9,111)],17:[(1,85),(7,98),(18,142)],18:[(8,92),(17,142)],19:[(0,75),(12,71)]}
obj = defaultdict(list)
graph2 = [[0 for col in range(len(adj))]for row in range(len(adj))]
for i in range(len(adj)):
  for elem in adj[i]:
    graph2[i][elem[0]]=elem[1]
for i in range(len(graph2)):
  for j in range(len(graph2)):
    if graph2[i][j]!=0:
      obj[i].append(j)
print(obj)
class Graph:
  def __init__(self,vertices):
    self.v = vertices
    self.graph = graph2

  def gmi(self,dist,visited):
    global minidx  
    min_val = float('inf')
    for i in range(self.v):
      if dist[i]<min_val and visited[i]==False:
        min_val = dist[i]
        minidx=i
    return minidx
  def printdist(self,dist):
    for i in range(self.v):
      print(i,cat2[i],dist[i])
  def dijkstra(self,src):
    dist = [float('inf')]*self.v
    dist[src] = 0
    dist2 = [float('inf')]*self.v
    w=[]
    x=[]
    h = heur 
    dist2[src]=h[src]
    visited = [False]*self.v 
    for i in range(self.v):


      u = self.gmi(dist2,visited)
      visited[u] = True
      if x:
        z = x[-1]
        for elem in obj[z]:
          visited[elem]=True

      if h[u] == 0:
        break
      x.append(u)
      w.append(cat2[u])
      for v in range(self.v):
        if self.graph[u][v]>0 and visited[v]==False and dist2[v]>dist[u]+self.graph[u][v]+h[v]:
          dist[v]=dist[u]+self.graph[u][v]
          dist2[v]=dist[u]+self.graph[u][v]+h[v]
    self.printdist(dist2)
    print(w + [cat2[1]])
g = Graph(len(graph2))
g.dijkstra(dic['Lugoj'])