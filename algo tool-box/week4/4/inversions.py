# Uses python3
import sys

def merge(low,high):
        n=0
        i,j,k=0,0,0
        while len(low)>i and len(high)>j:
            if low[i]<high[j]:
                a[k]= low[i]
                i+=1
            else:
                a[k]= high[j]
                j+=1
                n+=len(low)
            k+=1
        while len(low)>i:
                a[k] =low[i]
                i+=1
                k+=1
        while len(high)>j:
                a[k]= high[j]
                j+=1
                k+=1
        return n

def get_number_of_inversions(a):
        if len(a)<2:
            return 0
        mid = len(a)//2
        low=a[:mid]
        high = a[mid:]
        return  get_number_of_inversions(low) + get_number_of_inversions(high) + merge(low,high)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a))
