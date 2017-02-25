# Uses python3
a=[]
a.append(0)
a.append(1)
q=[]
q.append(0)
q.append(1)
n=70
def fib(n):
	if n <= 1:
		return a[n]
	else:
		for i in range(2,n+1):
			b= a[i-1]+a[i-2]		
			a.append(b)
			q.append(b%10)
		return q
def fiblastdigit(n):
	
	a=0
	b=1
	c=0
	s=1
	p=[]
	p.append(0)
	p.append(1)
	for i in range(2,n):
		a,b=b,a+b
		s=s+b
		p.append(s%10)		
		c=b%10
	return c,p	


#print('q',fib(n))
print('c',fiblastdigit(n))