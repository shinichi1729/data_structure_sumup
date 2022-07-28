import sys
from collections import defaultdict
sys.setrecursionlimit(4 * 10 ** 5)


class LCA():
    def __init__(self, size, edges, root=0, max_size=20):
        self.size = size
        self.edges = edges
        self.root = root
        self.max_size = max_size
        self.depth = [0] * size
        self.parent = [-1] * size
        self._find_depth_parent()
        self.table = self._make_table()

    def _find_depth_parent(self):
        stack = [0]
        while stack:
            u = stack.pop(-1)
            for v in self.edges[u]:
                if v == self.parent[u]:
                    continue
                stack.append(v)
                self.parent[v] = u
                self.depth[v] = self.depth[u] + 1

    def _make_table(self):
        table = [[-1] * self.size for _ in range(self.max_size)]
        table[0] = self.parent
        for k in range(1, self.max_size):
            for v in range(self.size):
                if table[k-1][v] == -1:
                    table[k][v] = -1
                    continue
                table[k][v] = table[k-1][table[k-1][v]]
        return table

    def query(self, v, k):
        # 頂点v(0-indexed)からk回(k < 2^max_size)移動した先の頂点を求める
        now = v
        p = 0
        while k > 0:
            if k & 1:
                now = self.table[p][now]
            k >>= 1
            p += 1
        return now

    def find_lca(self, u, v):
        # 頂点uとvの最小共通祖先(LCA)を返す
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        if self.depth[u] != self.depth[v]:
            u = self.query(u, self.depth[u] - self.depth[v])
        if u == v:
            return u

        wa, ac = -1, self.depth[v]
        while ac - wa > 1:
            wj = (ac + wa) // 2
            up, vp = self.query(u, wj), self.query(v, wj)
            if up == vp:
                ac = wj
            else:
                wa = wj
        return self.query(u, ac)

    def dist(self, u, v):
        # 頂点uとvの距離を返す
        uv = self.find_lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[uv]


def main():
    # yosupo judge
    # N, Q = map(int, input().split())
    # edges = defaultdict(list)
    # for i, p in enumerate(map(int, input().split())):
    #     edges[i+1].append(p)
    #     edges[p].append(i+1)
    # lca = LCA(N, edges)
    # result = []
    # for _ in range(Q):
    #     u, v = map(int, input().split())
    #     result.append(lca.find_lca(u, v))
    # print(*result, sep="\n")



if __name__ == '__main__':
    main()

