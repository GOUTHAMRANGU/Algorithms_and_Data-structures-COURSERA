# Uses python3
import sys
def fiblastdigit(n):
    n=n%60 #the pattern in the last digits repeats itself after 60 terms in the series
    a=0
    b=1
    c=0
    for i in range(2,n+1):
        a,b=b,a+b
        c=b%10
    return c    


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fiblastdigit(n))
