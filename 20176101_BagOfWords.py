import os.path
import math
path=input("Enter the Directory Path:")
file=os.listdir(path)
print(file)
os.chdir(path)
def PgChecker(file1,file2):
    def Characters(s):
        s=s.lower()
        c="_0123456789abcdefghijklmnopqrstuvxxyz "
        for i in s:
            if i not in c:
                s=s.replace(i," ")
        s=s.replace("\n"," ").replace("\xa0"," ")
        s=s.split(" ")
        return s
    s1=Characters(file1.read())
    s2=Characters(file2.read())    
    def Dict(s,d):
        for i in s:
            if i==' ' or i=='':
                pass
            elif i not in d:
                d[i]=1
            else:
                d[i]+=1 
        return d
    d1=Dict(s1,{})
    d2=Dict(s2,{})    
    def DotproductofNum(d1,d2):
        L=[]
        for i in d1:
            for j in d2:
                if i==j:
                    L.append(d1[i]*d2[j])
        return L
    numerator=sum(DotproductofNum(d1,d2))
    def DotproductofDen(d):
        dum=0
        for i in d:
            dum+=(d[i])**2
        dum=(dum)**(1/2)
        return dum
    denominator=(DotproductofDen(d1))*(DotproductofDen(d2))
    return round((numerator/denominator)*100)
list1=[]
for j in range (len(file)):
    for i in range (len(file)):
        if j==i:
            list1.append("Nil")
        else:
            file1=open(file[i],"r")
            file2=open(file[j],"r")
            list1.append(PgChecker(file1,file2))
            file1.close()
            file2.close()
    print(file[i],list1,"\n")
    list1=[]
