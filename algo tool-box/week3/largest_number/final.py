# Uses python3
import sys
def merge(a,b):
    c = []
    while len(a) != 0 and len(b) != 0:
        k=(a[0]//(10**(len(str(a[0]))-1)))
        #print('k',k)
        l=(b[0]//(10**(len(str(b[0]))-1)))
        #print('l',l)
        if k > l:
            c.append(a[0])
            #print('c1',c,a[0],b[0])
            a.remove(a[0])
        elif k == l:
        	if a[0]>b[0]:
        		c.append(b[0])
        		#print('c2',c)
        		b.remove(b[0])
        	else:
        		c.append(a[0])
        		#print('c3',c)
        		a.remove(a[0])
        else:
            c.append(b[0])
            #print('c4',c)
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

'''a=[9,4,6,1,9]
g=(mergesort(a))
q=str()
for i in g:
	q=q+str(i)
print(q)'''
def largest_number(a):
	g=mergesort(a)
	q=str()
	for i in g:
		q=q+str(i)
	return q

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(largest_number(a))