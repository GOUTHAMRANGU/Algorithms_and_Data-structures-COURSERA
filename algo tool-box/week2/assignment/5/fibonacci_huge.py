# Uses python3
def fibonacci_huge(n, m):
    c = {0: 0, 1: 1}

    def fib_m(n):
        if n in c:
            return c[n]

        if n % 2 == 0:
            fib_half_n = fib_m(n // 2)
            out = (2 * fib_m(n // 2 - 1) + fib_half_n) * fib_half_n
        else:
            out = fib_m((n + 1) // 2) ** 2 + fib_m((n - 1) // 2) ** 2

        c[n] = out = out % m
        return out

    return fib_m(n)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))