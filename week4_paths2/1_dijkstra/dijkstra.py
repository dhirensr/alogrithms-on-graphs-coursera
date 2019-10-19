#Uses python3

import sys
import queue

def extract_min(h,dist):
    min_list=[dist[i] for i in h]
    min_index=min_list.index(min(min_list))
    element=h[min_index]
    h.remove(element)
    return element,h


def distance(adj, cost, s, t):
    #write your code here
    dist=[float('Inf') for i in range(len(adj))]
    prev=[None for i in range(len(adj))]
    dist[s]=0
    h=[i for i in range(len(adj))]
    while(len(h)!=0):
        u,h=extract_min(h,dist)
        for idx,i in enumerate(adj[u]):
            if(dist[i] > dist[u]+cost[u][idx]):
                dist[i] = dist[u]+cost[u][idx]
                prev[i]=u

    if(dist[t]!=float('Inf')):
        return dist[t]
    else:
        return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
