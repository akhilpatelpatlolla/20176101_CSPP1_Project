import os.path
path=input("Enter the Directory Name:")
file=os.listdir(path)
print(file)
os.chdir(path)
def PgChecker(file1,file2):
    def Characters(s):
        s=s.lower()
        c="abcdefghijklmnopqrstuvxxyz_0123456789 "
        for i in s:
            if i not in c:
                s=s.replace(i," ")
        s=s.replace("\n"," ").replace("\xa0"," ")
        s=s.split(" ")
        return s
    s1=Characters(file1.read())
    s2=Characters(file2.read()) 
    print(s1)
    print(s2)