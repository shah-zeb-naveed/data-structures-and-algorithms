# djiktra's shortest path (can work on both directed and undirected graphs)

from queue import PriorityQueue
import heapq as hq
from heapq import heappush, heappop
from collections import defaultdict

class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra_adj_mat(self, source):
        visited = set()
        unvisited = set(range(self.v))

        distances = [float('inf')] * self.v
        distances[source] = 0
        prev = [-1] * self.v
        
        q = PriorityQueue()
        q.put((0, source))

        while unvisited: # O(V)
            # print("Visited: ", visited)
            # print("Unvisited: ", unvisited)
            # print("q: ", q.queue)

            _, node = q.get() # O(log(heap size))

            if node in visited:
                continue

            #print('Node: ', node)
            unvisited.remove(node)
            visited.add(node)
 
            # benefit of 2d adj mat was that we could enumerate easily
            for i, neib_dist in enumerate(self.graph[node]):
                #print("Neighbour: ", i, neib_dist)

                # == 0 condition coz of adj. matrxi structure
                if neib_dist == 0 or i in visited:
                    #print('Continue...')
                    continue

                if neib_dist + distances[node] < distances[i]:
                    distances[i] = neib_dist + distances[node]
                    prev[i] = node

                    # add "potential" candidate in the queue
                    # print("Candidate found: ", (distances[i], i))
                    q.put((distances[i], i)) # O(log(heap size))
            
            # O((E+1) log(heap size))
            # Heap size -> VE -> V^2
            # O(Elog(V))

        return list(zip(distances, prev))

    def djikstras(self, source):

        q = [(0, source)]   # Unexplored nodes
        visited = set()
        distances = {i : float('inf') for i in range(self.v)}
        parents = {}

        while len(visited) != self.v:
            print(q)
            _, node = heappop(q)
            print(node)

            if node in visited:
                continue
            
            visited.add(node)

            for neib, cost in self.graph[node]:
                if neib not in visited:
                    if distances[neib] > cost + distances[node]:
                        distances[neib] = cost + distances[node]
                        parents[neib] = node
                        heappush(q, (distances[neib], neib)) #

        return list(zip(distances, parents))

graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
#print(graph.graph)
print(graph.djikstras(0))