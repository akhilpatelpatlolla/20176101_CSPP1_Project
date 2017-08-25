import os.path                                          #importing path function to open directory
path=input("Enter the Directory:")                             
file=os.listdir(path)                                  #forming a list all the available documents in the directory
os.chdir(path)                                          #To change the path of directory
print("  	  ",file,"\n")                              #To print list of documents
class Lcs:		                                        #creation of a class Lcs
    def __init__(self,file1,file2,q=""):                #Constructor of class Lcs  
        self.file1=file1                                       
        self.file2=file2
        self.q=q
    def set_q(self,new_q):
        self.q=new_q
    def get_q(self):
        return self.q
    def STR(self):
        e=0
        for j in range(len(self.file1)):
            newtemp=j
            for i in range(len(self.file2)):
                if (newtemp<len(self.file1)):
                    if self.file1[newtemp]==self.file2[i]:
                        newtemp+=1
                        if (newtemp-j)>e:
                            e=newtemp-j
                            q=self.file1[j:newtemp]
                    else:
                        newtemp=j
        self.set_q(q)
        return self.get_q()
    def math(self):
        v=len(self.STR())
        v=((v*2)/(len(self.file1)+len(self.file2)))*100
        return v
for j in range(len(file)):
    Matrix,Matrix1=[],[]
    for i in range(len(file)):
        if j==i:
            Matrix1.append("Nil")
            Matrix.append("Nil")
        if j!=i:
            y=open(file[j],"r")
            z=open(file[i],"r")
            aa=y.read()
            bb=z.read()
            x=Lcs(aa,bb)
            Matrix1.append(x.STR())
            Matrix.append(x.math())
            y.close()
            z.close()
    print(file[j],Matrix)
    print("     ",Matrix1)
    print("")


