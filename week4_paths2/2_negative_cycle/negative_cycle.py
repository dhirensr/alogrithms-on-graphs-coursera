#Uses python3

import sys
import math
import queue


def bellman_ford(adj,dist,cost):
    for i in range(len(adj)):
        for u in range(len(adj)):
             for v_index,v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][v_index]:
                    dist[v] = dist[u] + cost[u][v_index]
    return dist

def negative_cycle(adj, cost):
    #write your code here
    dist=[float('Inf') for i in range(len(adj))]
    dist[0]=0
    for i in range(len(adj)-1):
        dist=bellman_ford(adj,dist,cost)
    dist_temp=dist.copy()
    dist=bellman_ford(adj,dist,cost)
    if(dist_temp==dist):
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
