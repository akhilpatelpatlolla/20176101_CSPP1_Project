file1=open("file1.txt").read().replace(".","").split()

file2=open("file2.txt").read().replace(".","").split()
mydict1={}
mydict={}

for word in file1:
	if word in mydict:
		mydict[word]+=1
	else:
		mydict[word]=1
print(mydict)

for word in file2:
	if word in mydict1:
		mydict1[word]+=1
	else:
		mydict1[word]=1
print(mydict1)

values=mydict.values()
best=max(mydict.values())
words=[]
for k in mydict:
	if mydict[k]==best:
		words.append(k)
print(words)

values=mydict1.values()
best=max(mydict1.values())
words1=[]
for k in mydict1:
	if mydict1[k]==best:
		words1.append(k)
print(words1)

p=[]
for x in mydict1:
	for y in mydict: 
		if x==y:
			p.append(mydict1[x]*mydict[y])
sum0=sum(p)
print(sum0)

sum=0
for x in mydict:
	sum=sum+(mydict[x]**2)
print(sum)
sum1=0
for x in mydict1:
	sum1=sum1+(mydict1[x]**2)
print(sum1)
import math
sum2=math.sqrt(sum1)*math.sqrt(sum)
print(sum2)
sum3=(sum0/sum2)*100
print(sum3)
