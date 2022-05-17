import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components


def scc(N: int, M: int, edges):
    """有向グラフの強連結成分分解を行う. 返り値は順に連結成分数と所属グループ配列"""
    """edges are 1-indexed"""
    edge = np.array(edges, dtype=np.int64).T
    weight = np.ones(M, dtype=np.int64).T
    graph = csr_matrix((weight, edge[:]-1), (N, N))
    connected_component, array = connected_components(graph, directed=True, connection="strong")
    return connected_component, array


if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))
    connected_components, array = scc(N, M, edges)
