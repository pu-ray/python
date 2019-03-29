Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[]
>>> for x in range(0,100):
	if x%9==0:
		a.append(x)

		
>>> a
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>> b=[]
>>> for x in range(0,100):
	if x%11==0:
		b.append(x)

		
>>> b
[0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c=[]
>>> c=a+b
>>> c
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> c.sort()
>>> c
[0, 0, 9, 11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88, 90, 99, 99]
>>> d=[]
>>> for x in range(2019,2119):
	if x%2==0:
		d.append(x)

		
>>> d
[2020, 2022, 2024, 2026, 2028, 2030, 2032, 2034, 2036, 2038, 2040, 2042, 2044, 2046, 2048, 2050, 2052, 2054, 2056, 2058, 2060, 2062, 2064, 2066, 2068, 2070, 2072, 2074, 2076, 2078, 2080, 2082, 2084, 2086, 2088, 2090, 2092, 2094, 2096, 2098, 2100, 2102, 2104, 2106, 2108, 2110, 2112, 2114, 2116, 2118]
>>> students1={"name":"pauline","Y.O.B",:2000}

>>> student1={"name":"pauline","Y.O.B":1998}
>>> student2={"name":"Huwa","Y.O.B":2014}
>>> student3={"name":"emma","Y.O.B":1998}
>>> student5={"name":"purity","Y.O.B":1994}
>>> student6={"name":"purity","Y.O.B":1994}
>>> students=[student1,student2,student3,student5,student6]
>>> students
[{'name': 'pauline', 'Y.O.B': 1998}, {'name': 'Huwa', 'Y.O.B': 2014}, {'name': 'emma', 'Y.O.B': 1998}, {'name': 'purity', 'Y.O.B': 1994}, {'name': 'purity', 'Y.O.B': 1994}]
>>> for student in students:
	ageindays = (2019-student["Y.O.B"])*365
	print("Hi {}, you were born in {} thus you have lived for {} days.".format(student["name"],student["y.O.B"],ageindays))

	

>>> for student in students:
	ageindays = (2019-student["Y.O.B"])*365
	print("Hi {}, you were born in {} thus you have lived for {} days.".format(student["name"],student["Y.O.B"],ageindays))

	
Hi pauline, you were born in 1998 thus you have lived for 7665 days.
Hi Huwa, you were born in 2014 thus you have lived for 1825 days.
Hi emma, you were born in 1998 thus you have lived for 7665 days.
Hi purity, you were born in 1994 thus you have lived for 9125 days.
Hi purity, you were born in 1994 thus you have lived for 9125 days.
>>
