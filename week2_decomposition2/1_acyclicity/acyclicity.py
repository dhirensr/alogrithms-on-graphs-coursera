#Uses python3

import sys

def acyclic_check(adj,x,visited,rec_stack):
    neighbours=adj[x]
    visited[x]=1
    rec_stack[x]=1
    for j in range(len(neighbours)):
        if not visited[adj[x][j]] and acyclic_check(adj,adj[x][j],visited,rec_stack):
            return 1
        elif rec_stack[adj[x][j]]:
            return 1
    rec_stack[x]=0
    return 0

def acyclic(adj):
    visited=[0 for _ in range(len(adj))]
    rec_stack=[0 for _ in range(len(adj))]
    for i in range(len(adj)):
        if visited[i]==0:
            if(acyclic_check(adj,i,visited,rec_stack)):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
