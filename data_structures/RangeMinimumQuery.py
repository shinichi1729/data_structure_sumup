INF, LINF = 1 << 31, 1 << 62
class RMQ(object):
    def __init__(self, n):
        self.size = n
        self.binary_round_up()
        self.bitdata = [INF] * (2*self.size-1)
        self.data = [INF] * self.size

    def binary_round_up(self) -> None:
        self.size -= 1
        i = 1
        while self.size != (self.size | self.size >> i):
            self.size |= self.size >> i
            print(bin(self.size))
            i *= 2
        self.size += 1

    def update(self, i: int, x: int) -> None:
        """data[i]番目をxに更新して,応じて二分木を順次更新.O(logN)"""
        self.data[i] = x
        i += self.size-1
        self.bitdata[i] = x
        while i > 0:
            i = (i-1) // 2
            self.bitdata[i] = min(self.bitdata[2*i+1], self.bitdata[2*i+2])

    def find_minimum(self, left, right):
        """indexが[left, right)の半開半閉区間に含まれる最小の値を返す.O(logN)"""
        assert 0 <= left <= right <= self.size

        def query(ql, qr, k, l, r):
            #  [ql, qr)に対して完全に範囲外なら飛ばす.(意味のない値を返す)
            if qr <= l or r <= ql:
                return INF
            #  [ql, qr)に完全に含まれるならそこのnodeの値を返す.
            if ql <= l <= r <= qr:
                return self.bitdata[k]
            left_min = query(ql, qr, 2*k+1, l, (l+r)//2)
            right_min = query(ql, qr, 2*k+2, (l+r)//2, r)
            return min(left_min, right_min)

        return query(left, right, 0, 0, self.size)


if __name__ == '__main__':
    rmq = RMQ(10)
    print(rmq.size)  # => 16 (２の累乗の形で切り上げ)
    rmq.update(2, 4)
    rmq.update(5, 2)
    rmq.update(8, 3)
    print(rmq.find_minimum(2, 5))  # => 4
    print(rmq.find_minimum(2, 6))  # => 2
