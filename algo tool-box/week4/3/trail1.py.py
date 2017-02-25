# Uses python3
import sys
import random

def partition3(a, left, right):
    pivot = a[left]
    i = left
    low = left
    high = right
    while i <= high:
        if a[i] < pivot:
            a[i], a[low] = a[low], a[i]
            low += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[high] = a[high], a[i]
            high -= 1
        else:
            i += 1

    return low, high


def quicksort3(a, left, right):
    if left >= right:
        return

    randpivot = random.randint(left, right)
    a[left], a[randpivot] = a[randpivot], a[left]
    mid1, mid2 = partition3(a, left, right)
    quicksort3(a, left, mid1 - 1)
    quicksort3(a, mid2 + 1, right)


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quicksort3(a, 0, n - 1)
    for x in a:
        print(x, end=" ")