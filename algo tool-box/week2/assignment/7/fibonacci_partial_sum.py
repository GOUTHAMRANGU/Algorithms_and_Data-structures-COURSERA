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


def neg(from_,to):
    a=normal(to)-normal(from_-1)
    if a<0:
        return 10+a
    else:
        return a




if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(neg(from_, to))
