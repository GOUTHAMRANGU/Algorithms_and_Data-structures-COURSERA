# Uses python3
import heapq
n = int(input())
if n!=0:
	a = [int(x) for x in input().split()]
	assert(len(a) == n)
	x,y=heapq.nlargest(2, a)
	print(x*y)
else:
	print(0)
