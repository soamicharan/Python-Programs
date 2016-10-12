ran=int(input("Enter range for primes.\n"))
num=[]
x=0
for a in range(0,ran+1):
    num.append(a)
for b in range(2,ran+1):
	if num[b]==0:
		continue
	else:
		for c in range(b+1,ran+1):
			if c%num[b]==0:
				num[c]=0
for d in range(2,ran+1):
    if num[d]==0:
        continue
    else:
       print(num[d])
