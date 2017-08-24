file1=open("file1.txt").read()
file2=open("file2.txt").read()
import re
file1 = re.sub('[^a-zA-Z0-9_\n\.\ ]', ' ', file1)
file1 = re.sub(' +',' ',file1)
file2 = re.sub('[^a-zA-Z0-9_\n\.]', ' ',file2)
file2 = re.sub(' +',' ',file2)
file1=file1.lower().replace(".","").replace(",","").split()
file2=file2.lower().replace(".","").replace(",","").split()
dict1={}
dict2={}											
for word in file1:
	if word in dict1:
		dict1[word]+=1
	else:
		dict1[word]=1
for word in file2:
	if word in dict2:
		dict2[word]+=1
	else:
		dict2[word]=1
sum=0
for i in dict1.keys():
	for j in dict2.keys():
		if i==j:
			c=dict1[i]*dict2[j]
			sum=c+sum
sum1=0
sum2=0
for i in dict1.keys():
	sum1=sum1+(dict1[i]**2)
for i in dict2.keys():
	sum2=sum2+(dict2[i]**2)
import math
sum3=math.sqrt(sum2)*math.sqrt(sum1)
sum4=(sum/sum3)*100
print(sum4)	