file1=open("file1.txt").read().replace(".","").replace(",","").split()
print(file1)
file2=open("file2.txt").read().replace(".","").split()
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
