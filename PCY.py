import itertools as itr, numpy as np
from operator import itemgetter, attrgetter
def pairs(l):
    cart = itr.product(l,l) 
    pairs = [item for item in cart if item[0]!=item[1] and item[0]<item[1]] # removes (i,i) and (j,i) pairs
    return pairs
def a(source):
	j=0
	for i in source:
		print(i)
		j=j+1
		if j==20:
			break
s = int(input("Minimum support = "))
f = open("1.txt")
items = {}
source ={}
source1 ={}
pair = {}
air={}
source2={}
destination={}
fpm={}
fpm1={}
j=0
l={}
k=0;
# pass 1
for line in f:
	a1,a2,a3,a4,a5,a6,a7 = line.rstrip().split(",")
	#print(a2)
	if a1 not in fpm:
		fpm[a1]={}
		fpm[a1][a2]=1
	else:
		if a2 in fpm[a1]: 
			fpm[a1][a2] += 1
		else:
			fpm[a1][a2]=1
		
	if a1 in source:
		source[a1] += 1
	else:
		source[a1] = 1

	if a2 in items:
		items[a2] += 1
	else:
		items[a2] = 1
	air[k]=a3
	source2[k]=a1
	destination[k]=a2
	k=k+1;

n = len(air)

#print(fpm)
for src in fpm:
	for dest in fpm[src]:
		if(fpm[src][dest]>=s):
			print(src+"-->"+dest)

n = len(air)
#print(fpm)
for i in range(n):
	for j in range(0, n-i-1):
 
		if air[j] < air[j+1] :
			air[j], air[j+1] = air[j+1], air[j]
			source2[j], source2[j+1] = source2[j+1], source2[j]
print("")
print("Sources(Places) from which Airline wil get more revenue")
print("")
for i in range(20):
	print(source2[i])
	
pair=sorted(items, key=items.__getitem__,reverse=True)
source1=sorted(source, key=source.__getitem__,reverse=True)
'''for c in range(n):
	fpm1[source2[c]]=sorted(fpm[source2[c]], key=fpm[source2[c]].__getitem__,reverse=True)
print(fpm1)'''
print("")
print("Top 20 destination to visit in are:-")
print("")
a(pair)
print("")
print("Top 20 Sources from which travelling takes place are:-")
print("")
a(source1)
