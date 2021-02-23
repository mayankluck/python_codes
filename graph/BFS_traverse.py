from collections import defaultdict
from collections import deque

def bfs_traverse(graph, start, visited, path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start]= True
    while len(queue) != 0:
        tmpnode = queue.popleft()
        for neighbour in graph[tmpnode]:
            if visited[neighbour]== False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour]= True
    return path


graph = defaultdict(list)
v,e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

path =[]
start = "a"
visited = defaultdict(bool)
bfs_path = bfs_traverse(graph, start, visited, path)
print(bfs_path)
