from typing import List
from collections import defaultdict

class UnionFind(object):
    def __init__(self, n):
        self.parent = [-1] * n
        self.n = n

    def union(self, x: int, y: int) -> None:
        x, y = self.root(x), self.root(y)

        if self.is_same(x, y):
            return
        if self.size(x) < self.size(y):
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

    def root(self, x: int) -> int:
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def size(self, x:int) -> int:
        x = self.root(x)
        return -self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def members(self, x: int) -> List[int]:
        x = self.root(x)
        return [i for i in range(self.n) if self.root(i) == x]

    def group_count(self) -> int:
        return len([i for i in self.parent if i < 0])

    def all_group_members(self) -> dict:
        group_members = defaultdict(list)
        for i in range(self.n):
            group_members[self.root(i)].append(i)
        return group_members

    def __str__(self):
        return '\n'.join(f'{root}: {member}' for root, member in self.all_group_members().items())


if __name__ == '__main__':
#     N = 10
#     uf = UnionFind(N)
#     uf.union(1, 4)
#     uf.union(2, 8)
#     uf.union(1, 9)
#     print(uf.parent)
#     uf.union(3, 4)
#     uf.union(0, 3)
#     print(uf)

