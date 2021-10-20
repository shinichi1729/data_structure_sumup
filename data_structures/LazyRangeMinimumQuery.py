INF, LINF = 1 << 31, 1 << 59
class LRMQ(object):
    def __init__(self, n):
        self.size = n
        self.binary_roundup()
        self.data = [INF] * (2*self.size-1)
        self.lazy = [INF] * (2*self.size-1)

    def binary_roundup(self):
        self.size -= 1
        i = 1
        while self.size != (self.size | self.size >> i):
            self.size |= self.size >> i
            i += 1
        self.size += 1

    def eval(self, k):
        """lazy配列のk番目に対する操作.呼び出さない"""
        if self.lazy[k] == INF:
            return
        if k < self.size:
            self.lazy[2*k+1] = self.lazy[k]
            self.lazy[2*k+2] = self.lazy[k]
        self.data[k] = self.lazy[k]
        self.lazy[k] = INF
        return

    def update(self, left, right, value):
        """[left, right)の半開区間をvalueに更新"""
        assert 0 <= left <= right <= self.size

        def _update(ql, qr, x, k, l, r):
            self.eval(k)
            if ql <= l <= r <= qr:
                self.lazy[k] = x
                self.eval(k)
                return
            if r <= ql or qr <= l:
                return
            _update(ql, qr, x, 2*k+1, l, (l+r)//2)
            _update(ql, qr, x, 2*k+2, (l+r)//2, r)
            self.data[k] = min(self.data[2*k+1], self.data[2*k+2])
        return _update(left, right, value, 0, 0, self.size)

    def find_minimum(self, left, right):
        """[left, right)の半開区間の最小値を返す"""
        assert 0 <= left <= right <= self.size

        def query(ql, qr, k, l, r):
            if r <= ql or qr <= l:
                return INF
            self.eval(k)
            if ql <= l <= r <= qr:
                return self.data[k]
            else:
                left_child = query(ql, qr, 2*k+1, l, (l+r)//2)
                right_child = query(ql, qr, 2*k+2, (l+r)//2, r)
                return min(left_child, right_child)
        return query(left, right, 0, 0, self.size)

    def print_tree(self):
        l, r = 0, 0
        while l <= self.size+1:
            print(self.data[l:r+1])
            l = 2*l+1
            r = 2*r+2
        print("=" * 30)

    def print_lazy(self):
        l, r = 0, 0
        while l <= self.size+1:
            print(self.lazy[l:r+1])
            l = 2*l+1
            r = 2*r+2
        print("=" * 30)


if __name__ == '__main__':
    # rmq = LRMQ(8)
    # rmq.print_tree()
    # rmq.update(1, 4, 3)
    # rmq.print_tree()
    # rmq.print_lazy()
    # rmq.update(2, 7, 5)
    # rmq.print_tree()
    # print(rmq.find_minimum(3, 4))
    # rmq.print_tree()
    # rmq.print_lazy()
    # rmq.update(4, 5, 1)
    # rmq.print_tree()


