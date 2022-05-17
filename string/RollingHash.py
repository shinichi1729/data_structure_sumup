class RollingHash(object):
    def __init__(self, base, mod, data, target):
        self.b = base
        self.m = mod
        self.pow = [1]
        self.data = data
        self.target = target
        for _ in range(len(data)+5):
            self.pow.append((self.pow[-1]*base)%mod)
        self.target_hash = self.make_hash(target)
        self.accum_hash = [0]
        for i in range(len(data)):
            value = self.accum_hash[-1] * base + ord(data[i])
            self.accum_hash.append(value%mod)

    def make_hash(self, string):
        """targetからhashを生成"""
        hash = 0
        for s in string:
            hash *= self.b
            hash += ord(s)
            hash %= self.m
        return hash

    def check(self, i):
        """hashが一致したdataのi番目以降を捜索.本当に合ってたらTrueを返す"""
        for l in range(i, len(self.target)+i):
            if l > len(self.data) or self.data[l] != self.target[l-i]:
                return False
        return True


    def match(self):
        """targetにマッチする文字列があるか"""
        length = len(self.target)
        target_hash = self.make_hash(self.target)
        for l in range(len(self.data)-length):
            r = l+length
            parts_hash = self.accum_hash[r] - self.accum_hash[l]*self.pow[length]
            parts_hash %= self.m
            if parts_hash == target_hash:
                if self.check(l):
                    return l
        return False
