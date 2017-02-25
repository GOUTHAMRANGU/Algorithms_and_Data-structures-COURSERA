# Uses python3
import sys
def fib(n):
	if n <= 1:
		return n
	a,b=0,1
	for _ in range(n):
		a,b = b,a+b
	return a
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib(n))
