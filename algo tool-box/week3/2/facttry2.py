# Uses python3
import sys
from collections import namedtuple

Item = namedtuple("Item", "value weight")


def get_optimal_value(capacity, weights, values):
    value = 0

    weival = sorted(
        [Item(v, w) for v, w in zip(values, weights)],
        key=lambda i: i.value / i.weight,
        reverse=True
    )

    gap = int(capacity)
    for item in weival:
        if gap - item.weight >= 0:
            value += item.value
            gap -= item.weight
        else:
            value += (item.value / item.weight) * gap
            gap = 0
        if not gap:
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))