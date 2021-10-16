from collections import defaultdict


class Eratosthenes():
    def __init__(self, size):
        self.size = size
        self.isprime = [True] * size
        self.minfactor = [-1] * size
        self.mobius = [1] * size
        self.isprime[1] = False
        self.minfactor[1] = 1
        self.eratosthenes()

    # 初めに篩にかけて,minfactorとisprimeを生成
    def eratosthenes(self):
        for p in range(2, self.size):
            if not self.isprime[p]:
                continue
            self.minfactor[p] = p
            self.mobius[p] = -1
            for q in range(p+p, self.size, p):
                self.isprime[q] = False
                if self.minfactor[q] == -1:
                    self.minfactor[q] = p
                if (q//p) % p == 0:
                    self.mobius[q] = 0
                else:
                    self.mobius[q] = -self.mobius[q]

    # 高速素因数分解
    def prime_factorize(self, number):
        assert 1 <= number <= self.size
        factors = defaultdict(int)
        while number != 1:
            factors[self.minfactor[number]] += 1
            number //= self.minfactor[number]
        return factors

    # 高速約数列挙
    def divisors(self, number):
        res = [1]
        factors = self.prime_factorize(number)
        for p, cnt in factors.items():
            # 追加前の大きさを保存
            res_size = len(res)
            for i in range(res_size):
                pp = 1
                for j in range(cnt):
                    pp *= p
                    res.append(res[i]*pp)
        return res


if __name__ == '__main__':
#     er = Eratosthenes(100000)
#     print(er.prime_factorize(32785))
#     print(er.divisors(1024))



