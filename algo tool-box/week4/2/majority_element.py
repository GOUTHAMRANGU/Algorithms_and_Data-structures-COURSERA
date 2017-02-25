# Uses python3
import sys

def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)//2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)
def max(b):
    if len(a)==0:
        print(0)
    elif (b[len(b)//2]==b[0]):
        print(1)
    elif ((len(b)%2==1) and (b[len(b)//2]==b[len(b)-1])):
        print(1)
    elif(len(b)%2==0 and b[len(b)//2-1]== b[len(b)-1]):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b=mergesort(a)
    max(b)