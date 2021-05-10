Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [2, 3, 5]
>>> a = [1, 2, 3, 4]
>>> sum([1,2,3])
6
>>> sum([1,2,3,6])
12
>>> def mySum(*x):
	Sum = 0
	for i in x:
		Sum = Sum + i

		
>>> mySum(2, 3, 4)
>>> def mySum(*x):
	Sum = 0
	for i in x:
		Sum = Sum + i

		
>>> def mySum(*x):
	Sum = 0
	for i in x:
		Sum = Sum + i
	return Sum

>>> mySum(2,3,4)
9
>>> 
>>> mySum(2,3,4,7,9,10)
35
>>> 
>>> a
[1, 2, 3, 4]
>>> mySum(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    mySum(a)
  File "<pyshell#17>", line 4, in mySum
    Sum = Sum + i
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> a
[1, 2, 3, 4]
>>> mySum(1,2,3,4)
10
>>> #list와 int는 같이 더할 수 없다
>>> mySum(2,3,4)
9
>>> mySum(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    mySum(a)
  File "<pyshell#17>", line 4, in mySum
    Sum = Sum + i
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> mySUm(a+5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    mySUm(a+5)
NameError: name 'mySUm' is not defined
>>> 5+a
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    5+a
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> 
>>> def Add2(x=30, y=50):
	return x+y

>>> Add(100, 200)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Add(100, 200)
NameError: name 'Add' is not defined
>>> Add2(100, 200)
300
>>> Add(3)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Add(3)
NameError: name 'Add' is not defined
>>> add2(100, 200)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    add2(100, 200)
NameError: name 'add2' is not defined
>>> Add2()
80
>>> Add2()
80
>>> Add2(y=100, x= 200)
300
>>> 
>>> map(함수, 리스트)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    map(함수, 리스트)
NameError: name '함수' is not defined
>>> #filter(함수, 리스트)
>>> #map(함수, 리스트)
>>> 
>>> def f1(x):
	x*x

	
>>> a = [1, 2, 3, 4]
>>> pow(2, 3)
8
>>> pow(2, 10)
1024
>>> for i in a:
	print(i, i*i)

	
1 1
2 4
3 9
4 16
>>> def f1(x):
	return x*x

>>> for i in a:
	f1(i)

	
1
4
9
16
>>> map(f1, a)
<map object at 0x000002465EEDB4C0>
>>> list(map(f1,a))
[1, 4, 9, 16]
>>> list(filter(f1, a))
[1, 2, 3, 4]
>>> list(filter(lambda x : x+x, a))
[1, 2, 3, 4]
>>> 
>>> 
>>> 
>>> 
>>> aa == 1200
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    aa == 1200
NameError: name 'aa' is not defined
>>> aa == 1000
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    aa == 1000
NameError: name 'aa' is not defined
>>> aa = 1200
>>> aa == 1000
False
>>> aa + 30
1230
>>> aa
1200
>>> aa = aa+ 30
>>> aa
1230
>>> aa +
SyntaxError: invalid syntax
>>> aa + \ 3-
SyntaxError: unexpected character after line continuation character
>>> aa += 30
>>> aa+30
1290
>>> aa._add__(30)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    aa._add__(30)
AttributeError: 'int' object has no attribute '_add__'
>>> aa.__add(30)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    aa.__add(30)
AttributeError: 'int' object has no attribute '__add'
>>> aa.__add__(30)
1290
>>> aa.__eq__(1000)
False
>>> dir(aa)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 
>>> 
>>> 