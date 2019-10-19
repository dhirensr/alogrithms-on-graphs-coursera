#Uses python3

import sys

def explore_all_paths(adj,x,visited):
    pass


def number_of_components(adj):
    result = 0
    #print(adj)
    visited=[0 for i in range(len(adj))]
    #print(visited)
    #write your code here
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
        adj[b - 1].append(a - 1)
    number_of_components(adj)
    #print()
