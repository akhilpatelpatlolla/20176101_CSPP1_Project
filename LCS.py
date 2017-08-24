class Lcs:
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def st(self):
        k=0
        for i in range(len(self.f1)):
            newitem=i
            item=newitem
            for j in range(len(self.f2)):
                if (newitem<len(self.f1)):
                    if self.f1[newitem]==self.f2[j]:
                        newitem+=1
                        if (newitem-i)>k:
                            k=newitem-i
                            o=self.f1[i:newitem]
                    else:
                        newitem=item
        return o
f1="when there is a will there is a way"
print(len(f1))
f2="re is a w"
print(len(f2))
pl=Lcs(f1,f2)
print(pl.st())  

percentage= (len(pl.st())/(len(f1)+len(f2)))*100
print(percentage)
import os.path
path=input("Enter the Directory Name:")
file=os.listdir(path)
print(file)
os.chdir(path)
