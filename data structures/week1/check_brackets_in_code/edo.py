# python3
import sys
def IsBalence(str):
	cleft=[]
	cright=[]
	copy=[]
	for i, s in enumerate(str):
		if s =='(' or s == '[' or s == '{':
			cleft.append([i,s])

			copy.append([i,s])
		if s == ')' or s== ']' or s== '}':
			cright.append([i,s])
			g=0
			if cleft:
				g=cleft.pop(-1)[1]
			if (g== '(' and s!=')')or (g=='[' and s!=']') or (g=='{' and s!='}'):
				return int(i+1)
	if len(cright)==0 and cleft:
		return cleft.pop(-1)[0]+1
	if len(copy)==0 and cright:
		return cright.pop(0)[0]+1
	return('Success')
if __name__ == "__main__":
    text = sys.stdin.read()
    print(IsBalence(str(text)))