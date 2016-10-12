print('Simple x derivative.')
a=int(input('Enter power of x.\n'))
c=1
if a<0: d=1
else : d=-1
for b in range(a-1,0,d):
    c=c*(a)
    print(c,'x^',b)
    a=a-1
    if b==1:print(c)
    

