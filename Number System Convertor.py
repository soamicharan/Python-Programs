def binary(dec):
        binary=[]
        count=0
        while dec!=0:
                digit=dec%2
                binary.append(digit)
                dec=(dec-digit)//2
                count+=1
        print("Binary = ",end="")
        for a in range(-1,-count-1,-1):
                print(binary[a],end="")
        print("")
def hexadecimal(dec):
        hex=[]
        count=0
        while dec!=0:
            hexa=dec%16
            if hexa==15:
                hex.append("F")
            elif hexa==14:
                hex.append("E")
            elif hexa==13:
                hex.append("D")
            elif hexa==12:
                hex.append("C")
            elif hexa==11:
                hex.append("B")
            elif hexa==10:
                hex.append("A")
            else:
                hex.append(hexa)
            dec=(dec-hexa)//16
            count+=1
        if dec==15:
            hex.append("F")
        if dec==14:
            hex.append("E")
        if dec==13:
            hex.append("D")
        if dec==12:
            hex.append("C")
        if dec==11:
            hex.append("B")
        if dec==10:
            hex.append("A")
        
        print("Hexadecimal = ",end="")
        for a in range(-1,-count-1,-1):
            print(hex[a],end="")
        print("")
def octal(dec):
    oct=[]
    count=0
    while dec!=0:
        digit=dec%8
        oct.append(digit)
        dec=(dec-digit)//8
        count+=1
    
    print("Octal = ",end="")
    for a in range(-1,-count-1,-1):
        print(oct[a],end="")
    print("")
def anytodec(num,mul):
    dec=0
    count=0
    deci=[]
    while num!=0:
        digit=num%10
        deci.append(digit)
        num=num//10
        count+=1
    for a in range(0,count,1):
        dec=dec+deci[a]*(mul**a)
    return (dec)
print("Choose known number system.\nDec\nBin\nHex\nOct")
cho=input()
if cho=="Dec" or cho=="dec":
    dec=int(input("Enter decimal number.\n"))
    binary(dec)
    hexadecimal(dec)
    octal(dec)
if cho=="Bin" or cho=="bin":
    bin=int(input("Enter binary number.\n"))
    dec=anytodec(bin,2)
    print("Decimal = ",dec,end="")
    print("")
    hexadecimal(dec)
    octal(dec)
if cho=="Oct" or cho=="oct":
    oct=int(input("Enter octal number.\n"))
    dec=anytodec(oct,8)
    print("Decimal = ",dec,end="")
    print("")
    hexadecimal(dec)
    binary(dec)
if cho=="Hex" or cho=="hex":
    print("Enter Hexadecimal number.\nAfter entering every number or alphabet, press enter.\nAfter finishing entering press . to stop.")
    en=","
    count=0
    hex=[]
    while en!=".":
        en=input()
        if en=="1": en=1
        if en=="2": en=2
        if en=="3": en=3
        if en=="4": en=4
        if en=="5": en=5
        if en=="6": en=6
        if en=="7": en=7
        if en=="8": en=8
        if en=="9": en=9
        if en=="0": en=0
        if en=="A": en=10
        if en=="B": en=11
        if en=="C": en=12
        if en=="D": en=13
        if en=="E": en=14
        if en=="F": en=15
        if en!=".":
            hex.append(en)
            count+=1
    dec=0
    for a in range(-1,-count-1,-1):
        dec=dec+hex[a]*(16**(-a-1))
    print("Decimal = ",dec,end="")
    print("")
    binary(dec)
    octal(dec)
            
            
        
        
    
    
            
        

                
   
        
        
        
