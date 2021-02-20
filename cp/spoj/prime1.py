
def generate_primes(n):
    rtn = [False, False] + [True for _ in range(n-1)]
    for i in range(2, n+1):
        if rtn[i]:
            for j in range(i*i, n+1):
                rtn[j] = False
    return rtn


t = input()
for test in range(t):
    inp = input()
    low, high = int(inp[0]), int(inp[1])
    allprimes = generate_primes(n)
    for i in range(low, high+1):
        if allprimes[i]:
            print(i)
print()


