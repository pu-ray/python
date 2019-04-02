Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sumlist(n):
	a=[]
	for x in range(1,n+1):
		a.append(x)
		b = sum(a)
	return b

>>> sumlist(5)
15
>>> sumlist(30)
465
>>> sumlist(3)
6
>>> sumlist(200)
20100
>>> def functionName(lists,i):
	m=[]
	n=[]
	for x in lists:
		if x%i==0:
			m.append(x)
		else:
			n.append(x)

			
>>> print(m)

>>> m

>>> def functionName(lists,i):
	m=[]
	n=[]
	for x in lists:
		if x%i==0:
			m.append(x)
		else:
			n.append(x)
	print(m)
	print(e)

	
>>> 
>>> def functionName(lists,i):
	m=[]
	n=[]
	for x in lists:
		if x%i==0:
			m.append(x)
		else:
			n.append(x)
	print(m)
	print(n)

	
>>> s=[1,2,3,4,5]
>>> functionName(s,2)
[2, 4]
[1, 3, 5]
>>> p=[6,7,8,9,10,11]
>>> functionName(p,6)
[6]
[7, 8, 9, 10, 11]
>>> 
