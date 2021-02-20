class prime():
    def __init__(self, n: int) -> None:
        self.n = n

    def generate(self) -> list:
        if self.n < 2:
            return []
        isprime = [False, False] + [True for _ in range(1,self.n)]
        for i in range(2, self.n+1):
            if isprime[i]:
                for j in range(i*i, self.n+1):
                    isprime[j] = False
        rtn = []
        for i in range(self.n+1):
            if isprime[i]:
                rtn.append(i)
        return rtn
        