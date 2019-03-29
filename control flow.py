Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> customer1= {"name":"sharon","balance":400}
>>> customer2= {"name":"sharon","balance":2500}
>>> customer3= {"name":"sharon","balance":300}
>>> customer4= {"name":"purity","balance":800}
>>> customer5= {"name":"emma","balance":1200}
>>> customers=[customer1,customer2,customer3,customer4,customer5]
>>> customers
[{'name': 'sharon', 'balance': 400}, {'name': 'sharon', 'balance': 2500}, {'name': 'sharon', 'balance': 300}, {'name': 'purity', 'balance': 800}, {'name': 'emma', 'balance': 1200}]
>>> for customer in customers:
	sms="Hi"{},your balance is{}".format(customer["name"],customer["balance"])
	

>>> sms="Hi{} , your balance is{}".format(customer["name"],customer["balance"])

>>> sms="Hi{},your balance is{}".format(customers["name"],customers["balance"])

>>> for customer in customers:
	sms="Hi{},your balance is{}".format(customers["name"],customers["balance"])
	print(sms)

	

>>> sms

>>> for customer in customers:
	sms="Hi{},your balance is{}".format(customer["name"],customer["balance"])
	sms

	
'Hisharon,your balance is400'
'Hisharon,your balance is2500'
'Hisharon,your balance is300'
'Hipurity,your balance is800'
'Hiemma,your balance is1200'
>>> for customer in customers:
	loan=customer1["balance"]/2.9
	loan

	
137.93103448275863
137.93103448275863
137.93103448275863
137.93103448275863
137.93103448275863
>>> for customer in customers:
	loan=customer1["balance"]//2.9
	loan

	
137.0
137.0
137.0
137.0
137.0
>>> for customer in customers:
	loan=customer["balance"]//2.9
	sms

	
'Hiemma,your balance is1200'
'Hiemma,your balance is1200'
'Hiemma,your balance is1200'
'Hiemma,your balance is1200'
'Hiemma,your balance is1200'
>>> print(sms)
Hiemma,your balance is1200
>>> for customer in customers:
	loan=customer["balance"]//2.9
	sms="hi{},your loan balance is{}".format(customer["name"],loan)
	sms

	
'hisharon,your loan balance is137.0'
'hisharon,your loan balance is862.0'
'hisharon,your loan balance is103.0'
'hipurity,your loan balance is275.0'
'hiemma,your loan balance is413.0'
>>> customers
[{'name': 'sharon', 'balance': 400}, {'name': 'sharon', 'balance': 2500}, {'name': 'sharon', 'balance': 300}, {'name': 'purity', 'balance': 800}, {'name': 'emma', 'balance': 1200}]
>>> for customer in customers:
	loan=customer["balance"]//2.9
	sms="Hi {} ,your loan is{}".format(customer["name"],loan)
	sms

	
'Hi sharon ,your loan is137.0'
'Hi sharon ,your loan is862.0'
'Hi sharon ,your loan is103.0'
'Hi purity ,your loan is275.0'
'Hi emma ,your loan is413.0'
>>> customers
[{'name': 'sharon', 'balance': 400}, {'name': 'sharon', 'balance': 2500}, {'name': 'sharon', 'balance': 300}, {'name': 'purity', 'balance': 800}, {'name': 'emma', 'balance': 1200}]
>>> for x in range(0,10):
	if x%3==0:
		print(x)

		
0
3
6
9
>>> for x in range(0,10):
	if x%3!=0:
		print(x)

		
1
2
4
5
7
8
>>> if x%3==0:
	print("{} is divisible by 3".format(x))
else:
	print("{} is not divisible by 3".format(x))

	
9 is divisible by 3
>>> for x in range(0,10):
	if x%3==0:
	print("{} is divisible by 3".format(x))
else:
	print("{} is not divisible by 3".format(x))
	

>>> for x in range(0,20):
	if x%3==0:
		print("{} is divisible by 3"
elif x%5==0:
		      

>>> for x in range(0,20):
		      if x%3==0:
		      elif x%5==0:
		      
SyntaxError: expected an indented block
>>> for x in range(0,20):
	if x%3==0:
	elif x%5==0:
		      

>>> >>>for x in range(0,20):
		      
SyntaxError: invalid syntax
>>> for x in range(0,20):
		      if x%3==0:
		      print("{} is divisible by 3"
			    

>>> for x in range(0,10):
	if x%3==0:
		print("{} is divisible by 3".format(x))

			    
0 is divisible by 3
3 is divisible by 3
6 is divisible by 3
9 is divisible by 3
>>> for x in range(0,100):
	if x%7==0:
		print(x)

			    
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
>>> for x in range(0,100):
	if x%7!=0:
		print(x)

			    
1
2
3
4
5
6
8
9
10
11
12
13
15
16
17
18
19
20
22
23
24
25
26
27
29
30
31
32
33
34
36
37
38
39
40
41
43
44
45
46
47
48
50
51
52
53
54
55
57
58
59
60
61
62
64
65
66
67
68
69
71
72
73
74
75
76
78
79
80
81
82
83
85
86
87
88
89
90
92
93
94
95
96
97
99
>>> for x range(0,10):
			    

>>> for x range (0,20):
			    

>>> for x in range(0,10):
	if x%3==0 or x%5==0:
		print(x)

			    
0
3
5
6
9
>>> true and true
			    

>>> true or true=
			    

>>> trueTraceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> true or true=
			    
SyntaxError: invalid syntax
>>> for x in range(0,20):
	if x%3==0 or x%5==0:
		print(x)

			    
0
3
5
6
9
10
12
15
18
>>> True and False
			    
False
>>> True and False
			    
False
>>> False and True
			    
False
>>> False and False
			    
False
>>> True or True
			    
True
>>> True or False
			    
True
>>> False or True
			    
True
>>> False or False
			    
False
>>> for x in range(900,950):
		if x%3==0 or x%5==0:
			    print(x)

			    
900
903
905
906
909
910
912
915
918
920
921
924
925
927
930
933
935
936
939
940
942
945
948
>>> for x in range(900,950):
		if x%3==0 or x%5==0:
			    print(fizzbuzz)

			    

>>> for x in range(900,950):
	if x%3==0:
		print("fizzbuzz").format(x))
		      
SyntaxError: invalid syntax
>>> for x in range(900,950):
		if x%3==0:
		      print("fizzbuzz".format(x))
		 if x%5==0:
		      

>>> for x in range(900,950):
		if x%3==0 or x%5==0:
		      print("fizzbuzz".format(x))
		 elif x%5==0:
		      

>>> for x in range(900,950):
		if x%3==0 or x%5==0:
		      print("fizzbuzz".format(x))
		 elif x%5==0:
		      

>>> for x in range(900,950):
		      if x%3==0 or x%5==0:
		      print("fizzbuzz")
		      
SyntaxError: expected an indented block
>>> for  x in range(900,950):
		if x%3==0 or x%5==0:
		      print("fizzbuzz")
		 elif x%5==0:
		      

>>> for x in range(900,950):
		if x%3==0 or x%5==0:
		      print("fizzbuzz")
		elif x%5==0:
		      print("fizz")
		elif x%3==0:
		      print("buzz")
		else:
		      print(x)

		      
fizzbuzz
901
902
fizzbuzz
904
fizzbuzz
fizzbuzz
907
908
fizzbuzz
fizzbuzz
911
fizzbuzz
913
914
fizzbuzz
916
917
fizzbuzz
919
fizzbuzz
fizzbuzz
922
923
fizzbuzz
fizzbuzz
926
fizzbuzz
928
929
fizzbuzz
931
932
fizzbuzz
934
fizzbuzz
fizzbuzz
937
938
fizzbuzz
fizzbuzz
941
fizzbuzz
943
944
fizzbuzz
946
947
fizzbuzz
949
>>> for x in range(2019,2119):
		if x%2==0:
		      print(x)

		      
2020
2022
2024
2026
2028
2030
2032
2034
2036
2038
2040
2042
2044
2046
2048
2050
2052
2054
2056
2058
2060
2062
2064
2066
2068
2070
2072
2074
2076
2078
2080
2082
2084
2086
2088
2090
2092
2094
2096
2098
2100
2102
2104
2106
2108
2110
2112
2114
2116
2118
>>> for x in range
		      
SyntaxError: invalid syntax
>>> 
		      
>>> 
		      
>>> SyntaxError: invalid syntax
		      

>>> for a in range(0,100):
		if a%9==0:
		      print(a)

		      
0
9
18
27
36
45
54
63
72
81
90
99
>>> for b in range(0,100):
		if b%9==0:
		      print(b)

		      
0
9
18
27
36
45
54
63
72
81
90
99
>>> c=[]
		      
>>> for c in range(0,100):
		if a%9==0: and if b%9==0:
		      
SyntaxError: invalid syntax
>>> for c in range(0,100):
		if a%9==0: or  b%9==0:
		      
SyntaxError: invalid syntax
>>> for a in range(0,100):
		if a%9==0:
		      print(a)

		      
0
9
18
27
36
45
54
63
72
81
90
99
>>> for b in range(0,100):
		if b%11==0:
		      print(b)

		      
0
11
22
33
44
55
66
77
88
99
>>> c=dict()
		      
>>> for a in range(0,100):
		if a%9==0:
		      for b in range(0,100):
		      if b%11==0:
		      

>>> c=dict()
		      
>>> for a in range(0,100):
		      if a%9==0:
		      c(a)=len(a)
		      

>>> for a in range(0,100):
		
