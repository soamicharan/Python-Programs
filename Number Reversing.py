a=int(input("Enter a number.\n"))
rn=0;
while a!=0 :
    rn=rn*10
    rn=rn+(a%10)
    a=a//10
print(rn)
