Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  print("Twinkle,twinkle,little star,\n\tHow i wonder what you are!\n\t\tUp above the world is so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle,little star,\n\tHow i wonder whatyou are")
SyntaxError: unexpected indent
>>> print("Twinkle,twinkle,little star,\n\tHow i wonder what you are!\n\t\tUp above the world is so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle,little star,\n\tHow i wonder whatyou are")
Twinkle,twinkle,little star,
	How i wonder what you are!
		Up above the world is so high,
		Like a diamond in the sky.
Twinkle, twinkle,little star,
	How i wonder whatyou are
>>> color_list=["red","green","white","black"]
>>> color_list[0]
'red'
>>> color_list[3]
'black'
>>> n=[3,5,7,8,9]
>>> print(list)
<class 'list'>
>>> n=[3,5,7,8,9]
>>> list=[]
>>> for x in n:
	list.append(x)

	
>>> list
[3, 5, 7, 8, 9]
>>> numbers=("3,5,7,23")
>>> lists=numbers.split("3,5,7,23")
>>> tuple=tuple(lists)
>>> print("lists:",list)
lists: [3, 5, 7, 8, 9]
>>> print("tuple:",tuple)
tuple: ('', '')
>>> tuple: ('', '')
>>> 
>>> 
>>> 
>>> 
>>> from datetime import date
>>> d1=date(2014,7,2)
>>> d2=date(2014,7,11)
>>> print(d2-d1).days
9 days, 0:00:00

>>> print((d2-d1).days)
9
>>> from math import pi
>>> r=6.0
>>> v=4/3*pi*r**3
>>> v
904.7786842338603
>>> numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
>>> for x in numbers:
	if x ==237:
		print(x)

		
237
>>> for x in numbers:
	if x ==237:
		print(x)
	else x% 2 ==0:
		

>>> for x in numbers:
	if x ==237:
		print(x)
	else x % 2 ==0:
		

>>> 
>>> numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
>>> for x in numbers:
	
SyntaxError: invalid syntax
>>> numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
>>> numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
>>> for x in numbers:
	1f x%2==237:
		
SyntaxError: invalid syntax
>>> for x in numbers:
	if x%2==237:
		print(x)

		
>>> x
527
>>> x, y=4, 3
>>> 
