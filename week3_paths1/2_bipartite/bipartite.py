#Uses python3

import sys
import queue

q=queue.Queue()
red_colored=[]
blue_colored=[]
def bipartite(adj):
    #write your code here
    colored=[-999 for i in range(len(adj))]
    colored[0]=1
    q.put(0)
    output=1
    while not (q.empty()):
        u=q.get()
        counter=colored[u]
        for i in adj[u]:
            if(colored[i]==counter):
                output=0
            if (colored[i]==-999):
                q.put(i)
                colored[i]=counter+1

    return output

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
