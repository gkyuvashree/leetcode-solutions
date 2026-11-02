class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        primes = 0

        for i in range(2, n + 1):
            is_prime = True

            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                primes += 1

        return (math.factorial(primes) * math.factorial(n - primes)) % MOD