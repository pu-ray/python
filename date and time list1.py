Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime;
>>> ticks = time.time()

>>> 
>>> import datetime;
>>> ticks = time.time()

>>> 
>>> 
>>> 
>>> import datetime;
>>> ticks = time.time()

>>> import time;
>>> ticks = time.time()
>>> print("Number of ticks since 12.00am,January 1, 1970:".format(ticks))
Number of ticks since 12.00am,January 1, 1970:
>>> import time;
>>> localtime = time.localtime(time.time())
>>> print("your {} is :".format(localtime))
your time.struct_time(tm_year=2019, tm_mon=4, tm_mday=2, tm_hour=8, tm_min=41, tm_sec=0, tm_wday=1, tm_yday=92, tm_isdst=0) is :
>>> import time;
>>> localtime = time.asctime( time.localtime(time.time()))
>>> print (" your {} is :".format(localtime))
 your Tue Apr  2 08:46:14 2019 is :
>>> import calendar
>>> cal = calendar.month(2008,1)
>>> print("here is the calendar {}:".format(cal))
here is the calendar     January 2008
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
:
>>> import calendar
>>> cal = calendar.month(2019,12)
>>> print("Here is the calendar {}:".format(cal))
Here is the calendar    December 2019
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
:
>>> import calendar
>>> 
>>> cal = calendar.month(2019,12)
>>> print("Here is the calendar {}:".format(cal))
Here is the calendar    December 2019
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
:
>>> import calendar
>>> print("Here is the calendar {}:".format(cal))
Here is the calendar    December 2019
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
:
>>> import calendar
>>> cal = calendar.month(1848,4)
>>> print("Here is the calendar {}:".format(cal))
Here is the calendar      April 1848
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
:
>>> 
