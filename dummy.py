import heapq

V = int(input("Enter Number of Vertices : "))
E = int(input("Enter Number of Edges : "))
graph = {i : [] for i in range(V)}

print ("Enter the All Edges values in format of u v w")
for _ in range (E):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

visited = [False]*V
min_heap = [(0,0)]
total_cost = 0

print ("Edges : Cost")
while(min_heap):
    cost,current = heapq.heappop(min_heap)
    if visited[current]:
        continue
    visited[current] = True
    total_cost+=cost
    for v, weight in graph[current]:
        if not visited[v]:
            heapq.heappush(min_heap,(weight,v))

print(total_cost)