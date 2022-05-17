import networkx as nx


if __name__ == '__main__':
    # ABC232 C
    N, M = map(int, input().split())
    G1 = nx.Graph([tuple(map(int, input().split())) for _ in range(M)])
    G2 = nx.Graph([tuple(map(int, input().split())) for _ in range(M)])

    if nx.is_isomorphic(G1, G2):
        # isomorphic
        print("Yes")
    else:
        # not-isomorphic
        print("No")
