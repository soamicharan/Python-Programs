def chain(arr): #this is recursive function for chain matrix multiplication
    st=0        #in this program, it uses slicing the list to obtain to sublist of original list
    end=3        #st and end variable slice the first sublist of original list
    st1=end-1    #st1 and end1 variables slice the second sublist
    end1=len(arr)
    min_cost=[]   #min_cost list will store all possible operation 
    if len(arr)==2:  #if a sliced sublist has length of 2 the it does not required for alogrithm
        return 0
    for l in range(len(arr)-1):
        if(len(arr)==3):                  #if a sliced sublist has length of 3 then it will return the product of their elements
            return arr[0]*arr[1]*arr[2]
        slice1=arr[st:end]         #we create a seperate list for both sublist of original list
        slice2=arr[st1:end1]
        if end==len(arr):   #if first sublist is smaller then second then slicing pattern will change
            st+=1
            st1=0
            end1=st+1
            slice1=arr[st1:end1]
            slice2=arr[st:end]
        cost = slice1[0]*slice1[-1]*slice2[-1]+chain(slice1)+chain(slice2)  #this is main step where sublist goes  through recursion
        min_cost.append(cost)
        if st==0:      #if first sublist is greater then second then it wil execute
            end+=1
            st1=end-1
    return min(min_cost)
    


n=int(input("Enter No. of Matrix."))
mat=[]
print "Enter Dimensions"
for x in range(n+1):
    dim=int(input())
    mat.append(dim)
cost=chain(mat)
print "Minimum Airthmetic operations Required : ",cost
