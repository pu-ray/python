Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Hello():
	print("Hello Akirachix")

	
>>> Hello()
Hello Akirachix
>>> Hello()
Hello Akirachix
>>> Hello()
Hello Akirachix
>>> Hello()
Hello Akirachix
>>> Hello()
Hello Akirachix
>>> def Hello(name):
	print("Hello {}".format(name))

	
>>> Hello("puray")
Hello puray
>>> Hello("emma")
Hello emma
>>> Hello("Huwa")
Hello Huwa
>>> Hello("mbugua")
Hello mbugua
>>> Hello("wanjiku")
Hello wanjiku
>>> Hello("winnie")
Hello winnie
>>> def sum(a,b):
	answer=a+b
	return answer

>>> sum(90,23)
113
>>> def divide(a,b)

>>> def divide(a,b):
	answer=a/b
	return answer

>>> divide(65,`13)

>>> divide(65,13)
5.0
>>> 5.0
5.0
>>> def multiply(a,b):
	answer=a*b
	return answer

>>> multiply(234,567)
132678
>>> def modulous(a,b):
	answer=a/b
	return answer

>>> modulous(89,76)
1.1710526315789473
>>> def exponation(a,b):
	answer=a**b
	return answer

>>> exponation(45,98)
1034728354093759656450988422630450052576382054610149677174690974574967031974377014209561652111382356311323678579479402894238104781976517188013531267642974853515625
>>> def age(name,year):
	x=2019-year
	print("Hello {}, you are {} years old".format(name))

	
>>> age("purity",1994)

>>> 
>>> def age(name,year):
	x=2019-year
	print("Hello {}, year are{} years old".format(name(x)))

	
>>> age("purity",1994)

>>> def age(name,year):
	x=2019-year
	print("Hello {}, year are{} years old".format(name,x))

	
>>> age("purity",1994)
Hello purity, year are25 years old
>>> age("hannah",2000)
Hello hannah, year are19 years old
>>> age("getrude",1989)
Hello getrude, year are30 years old
>>> age("martin","2010")

>>> age("martin",2010)
Hello martin, year are9 years old
>>> age("peter",2007)
Hello peter, year are12 years old
>>> age("huwa",2014)
Hello huwa, year are5 years old
>>> def squares(numbers):
	for number in numbers:
		print(number*number)

		
>>> x=[1,2,3,4,5]
>>> squares(x)
1
4
9
16
25
>>> y=[100,200,300,400]
>>> squares(y)
10000
40000
90000
160000
>>> def squares(numbers):
	a=[]
	for number in numbers:
		s=number*number
		a.append(s)
	return a

>>> squares(x)
[1, 4, 9, 16, 25]
>>> squares(y)
[10000, 40000, 90000, 160000]
>>> 
