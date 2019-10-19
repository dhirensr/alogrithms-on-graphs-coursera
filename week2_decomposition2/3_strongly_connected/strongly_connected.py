#Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs(adj, used, order, x):
    used[x]=1
    for i in adj[x]:
        if(used[i]==0):
            dfs(adj,used,order,i)
    order.append(x)
    return used,order
    
def number_of_strongly_connected_components(adj):
    result = 0
    used = [0] * len(adj)
    order = []
    for i in range(len(adj)):
        if(used[i]==0):
            result+=1
            used,order=dfs(adj,used,order,i)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
