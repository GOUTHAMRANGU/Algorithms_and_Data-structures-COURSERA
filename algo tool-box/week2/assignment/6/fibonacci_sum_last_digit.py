# Uses python3
import sys
def normal(n):

    n=n%60
    a=[]
    a.append(0)
    a.append(1)
    p=0
    q=1
    r=[]
    r.append(0)
    r.append(1)
    for i in range (2,n+1):
        p,q=q,p+q
        a.append(q)
        r.append(sum(a)%10)
    return r[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(normal(n))


