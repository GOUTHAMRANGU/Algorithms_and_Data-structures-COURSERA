# Uses python3
import sys


def optimal_summands(n):
    nums = [1]
    n -= 1
    while n:
        last = nums[-1]
        if (last + 1) * 2 <= n:
            n -= last + 1
            nums.append(last + 1)
        else:
            if last >= n:
                n += nums.pop()
            nums.append(n)
            n = 0

    return nums


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")