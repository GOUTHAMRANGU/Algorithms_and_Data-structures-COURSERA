# Uses python3
import sys
#import random

def get_optimal_value(capacity, weights, values):
    a=[]
    for i in range(len(weights)):
    	a.append(values[i]/weights[i])
    	#print('a',a)
    if weights(a.index(max(a)))>capacity:
    	out = capasity*max(a)
    	return (out)
    out=0
    wei=capacity
    while wei:
    	if weights[a.index(max(a))]<wei:
    		wei=wei-weights[a.index(max(a))]
    		out=out+values[a.index(max(a))]
    		#print('1',weights[a.index(max(a))],a,max(a))
    		#print('out',out)
    		a[a.index(max(a))]=0
    		values[a.index(max(a))]=0
    		

    	if weights[a.index(max(a))]>=wei:
    		out = out+(wei*max(a))
    		#print(weights[a.index(max(a))],a,max(a))
    		wei=0
    		#print(out)
    return out


    		    # write your code here

 
'''c=1000
w=[30]
v=[500]
print(get_optimal_value(c,w,v))'''

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
