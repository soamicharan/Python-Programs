arr=[]
smat=[]
count=0
r=int(input("Enter number of rows."))
c=int(input("Enter number of columns."))
for a in range(0,r):
    for b in range(0,c):
        temp=int(input())
        if temp!=0:
            count+=1
            arr.append(b)
            arr.append(a)
            arr.append(temp)
            smat.append(arr)
        arr=[]

print "Sparce matrix -"
print "Index\tRows\tColumn\tValue"
for a in range(0,count):
    print a,"\t",smat[a][1],"\t",smat[a][0],"\t",smat[a][2]
tmat=[]
tmat=sorted(smat)
print "Transposed Sparce matrix - "
print "Index\tColumn\tRow\tValue"
for a in range(0,count):
    print a,"\t",tmat[a][0],"\t",tmat[a][1],"\t",tmat[a][2]

    
