class RangeSumQuery(object):
    def __init__(self, size):
        self.size = size
        self.binary_roundup()
        self.tree = [0] * (2*self.size-1)

    def binary_roundup(self) -> None:
        """self.sizeをself.sizeを超える2^nで最小の数に変換(完全二分木に載せたい)"""
        self.size -= 1
        i = 1
        while self.size != (self.size | self.size >> i):
            self.size |= self.size >> i
            i *= 2
        self.size += 1

    def get(self, i) -> int:
        """i番目(0-indexed)の値をO(logN)で取得"""
        res = 0
        i += self.size-1
        while i >= 0:
            res += self.tree[i]
            i = (i-1) // 2
        return res

    def add(self, left, right, value) -> None:
        """O(logN)で[left, right)の半開区間の各値にvalueを加算を行う."""
        def query(ql, qr, k, l, r, x):
            if qr <= l or r <= ql:
                return
            elif ql <= l <= r <= qr:
                self.tree[k] += x
            else:
                query(ql, qr, 2*k+1, l, (l+r)//2, x)
                query(ql, qr, 2*k+2, (l+r)//2, r, x)
        query(left, right, 0, 0, self.size, value)
