class BinaryPrefixTree(object):
    def __init__(self, max_query=2*10**5, length=30):
        n = max_query * length
        self.elements_cnt = 0
        self.bitlen = length
        self.nodes = [-1] * (2 * n)  # ポインタを持たせる配列
        self.cnt = [0] * n  # cnt[id] => idを根とする部分木に含まれる要素数
        self.id = 0  # nodes配列に持たせるポインタかつcnt配列のindex

    def insert(self, x: int) -> None:
        """値xを定数時間で挿入"""
        pt = 0
        self.elements_cnt += 1
        for i in range(self.bitlen-1, -1, -1):
            ibit = x >> i & 1
            if self.nodes[2*pt+ibit] == -1:
                self.id += 1
                self.nodes[2*pt+ibit] = self.id
            self.cnt[pt] += 1
            pt = self.nodes[2*pt+ibit]
        self.cnt[pt] += 1

    def included(self, x: int) -> bool:
        """xが含まれているかどうか定数時間で調べる"""
        assert 0 <= x < 1 << self.bitlen
        pt, i = 0, self.bitlen-1
        while i >= 0:
            nxt = 2*pt+(x>>i&1)
            if self.nodes[nxt] == -1:
                return False
            pt = self.nodes[nxt]
            i -= 1
        return True

    def min_element(self) -> int:
        """setに含まれる最小の値を定数時間で調べる"""
        pt, min_value = 0, 0
        for i in range(self.bitlen-1, -1, -1):
            min_value <<= 1
            if self.nodes[2*pt] != -1:
                pt = self.nodes[2*pt]
            else:
                pt = self.nodes[2*pt+1]
                min_value += 1
        return min_value

    def max_element(self) -> int:
        """setに含まれる最大の値を定数時間で調べる"""
        pt, max_value = 0, 0
        for i in range(self.bitlen-1, -1, -1):
            max_value <<= 1
            if self.nodes[2*pt+1] != -1:
                pt = self.nodes[2*pt+1]
                max_value += 1
            else:
                pt = self.nodes[2*pt]
        return max_value

    def kth_elm(self, k: int) -> int:
        """下からk番目(0-indexed)の要素を定数時間で取得"""
        pt, ans = 0, 0
        k += 1
        assert k <= self.elements_cnt
        for i in range(self.bitlen-1, -1, -1):
            ans <<= 1
            if self.nodes[2*pt] != -1:
                if self.cnt[self.nodes[2*pt]] >= k:
                    pt = self.nodes[2*pt]
                else:
                    k -= self.cnt[self.nodes[2*pt]]
                    pt = self.nodes[2*pt+1]
                    ans += 1
            else:
                pt = self.nodes[2*pt+1]
                ans += 1
        return ans

    def lower_bound(self, x: int) -> int:
        """x以上の最小要素のindex(0-indexed)を定数時間で返す"""
        pt, index = 0, 0
        for i in range(self.bitlen-1, -1, -1):
            ibit = x >> i & 1
            if pt == -1:
                break
            if ibit and self.nodes[2*pt] != -1:
                index += self.cnt[self.nodes[2*pt]]
            pt = self.nodes[2*pt+ibit]
        return index


if __name__ == '__main__':
    trie = BinaryPrefixTree()
    trie.insert(7412894)
    trie.insert(0)
    trie.insert(11)
    trie.insert(222)
    trie.max_element()  # => 7412894
    k = trie.lower_bound(100)  # k = 2
    trie.kth_elm(k)  # => 222
    
