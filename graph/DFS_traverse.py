from collections import defaultdict

def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if visited[neighbour]==False:
            dfs(graph,neighbour,visited,path)
    return path

graph= defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

t="y"
while t=="y":

    path=[]
    start =input("enter the start node")
    visited= defaultdict(bool)
    dfs_path= dfs(graph,start,visited,path)
    print(dfs_path)
    t=input("press y for more traverse")