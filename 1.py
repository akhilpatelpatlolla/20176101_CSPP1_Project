file1=open("file1.txt").read().lower().replace(".","").replace(",","").replace("!","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").split()
# print(file1)
file2=open("file2.txt").read().lower().replace(".","").replace(",","").replace("!","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").split()
# print(file2)
# s=['!','@','#','$','%','^','&','*','(',')','-','=','+','[',']','\',':',';','"','']
dict1={}
dict2={}
for word in file1:
	if word in dict1:
		dict1[word]+=1
	else:
		dict1[word]=1
print(dict1)	
for word in file2:
	if word in dict2:
		dict2[word]+=1
	else:
		dict2[word]=1
print(dict2)
sum=0
for i in dict1.keys():
	for j in dict2.keys():
		if i==j:
			c=dict1[i]*dict2[j]
			print(c)
			sum=c+sum
print(sum)
sum1=0
sum2=0
for i in dict1.keys():
	sum1=sum1+(dict1[i]**2)
print(sum1)
for i in dict2.keys():
	sum2=sum2+(dict2[i]**2)
print(sum2)
import math
sum3=math.sqrt(sum2)*math.sqrt(sum1)
print(sum3)
sum4=(sum/sum3)*100
print(sum4)		

# import json
# dict1 = "{'akhil' : 'patel', 'patlolla' : 'msit'}"
# print(type(dict1))
# json_acceptable_string = dict1.replace("'", "\"")
# dict1 = json.loads(json_acceptable_string)
# print(type(dict1))