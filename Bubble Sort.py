a=int(input("Enter number of elements.\n"))
b=[]
print("Enter elements.\n")
for c in range(0,a):
    d=int(input())
    b.append(d)
for e in range(0,a-1):
    for f in range(0,a-e-1):
        if b[f]>b[f+1] :
            temp = b[f]
            b[f]=b[f+1]
            b[f+1]=temp
print (b)

    
