Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\CBN\Desktop\ejemplopython (2)\ejemplopython\ejemplocinco.py 
ingrese el peso: 
Traceback (most recent call last):
  File "C:\Users\CBN\Desktop\ejemplopython (2)\ejemplopython\ejemplocinco.py", line 1, in <module>
    peso = float(input ("ingrese el peso: "))
ValueError: could not convert string to float: 
>>> for i in range(20)
SyntaxError: invalid syntax
>>> for i in range(20):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
>>> for i in range(100):
	if i%2==0:
		print(i)

		
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
>>> lista
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    lista
NameError: name 'lista' is not defined
>>> lista = [5,7,10,15,20,10]
>>> lista.append(10)
>>> lista
[5, 7, 10, 15, 20, 10, 10]
>>> list.remove(10)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list.remove(10)
TypeError: descriptor 'remove' requires a 'list' object but received a 'int'
>>> lista.remove(10)
>>> lista
[5, 7, 15, 20, 10, 10]
>>> lista.remove(10)
>>> lista
[5, 7, 15, 20, 10]
>>> len (lista)
5
>>> 
