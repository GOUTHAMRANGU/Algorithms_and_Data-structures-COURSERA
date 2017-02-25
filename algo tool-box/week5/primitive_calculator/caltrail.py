# Uses python3
import sys


def optimal_seq(n):
    jumps = [0] * (n + 1)
    jumps[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)
        minjumps = min([jumps[x] for x in indices])
        jumps[i] = minjumps + 1
    pointer = n
    optseq = [pointer]
    while pointer != 1:
        total = [pointer - 1]
        if pointer % 2 == 0:
            total.append(pointer // 2)
        if pointer % 3 == 0:
            total.append(pointer // 3)
        pointer = min(
            [(c, jumps[c]) for c in total],
            key=lambda x: x[1]
        )[0]
        optseq.append(pointer)

    return reversed(optseq)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_seq(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")