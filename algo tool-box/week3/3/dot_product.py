#Uses python3

import sys
#import random

def max_dot_product(a, b):
    #write your code here
    res = 0
    s1=a.sort()
    s2=b.sort()
    res=sum(a[i]*b[i] for i in range(len(b)))
    return res
#a=random.sample(range(-101000,100000), 129000)
#b=random.sample(range(-101000,100000), 129000)
#print(max_dot_product(a,b))
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
