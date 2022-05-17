
from collections import defaultdict
import sys


def bridge_detect():
    c = 0
    ords, low = [-1] * N, [-1] * N
    res = []
    sys.setrecursionlimit(2 * 10 ** 6)
    
    def dfs(v, p):
        nonlocal c
        ords[v] = c
        c += 1
        low[v] = ords[v]
        for nv in graph[v]:
            if ords[nv] == -1:
                dfs(nv, v)
                low[v] = min(low[v], low[nv])
                if ords[v] < low[nv]:
                    res.append((v, nv))
            else:
                if nv == p:
                    continue
                low[v] = min(low[v], ords[nv])
    dfs(0, -1)
    return res

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(lambda x:int(x)-1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    bridge = bridge_detect()

