Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [3, 6, 9]
>>> type(a)
<class 'list'>
>>> 
>>> a[0]
3
>>> a[1]
6
>>> 
>>> a[2]
9
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> len(a)
3
>>> b = [6, 8, 9]
>>> a
[3, 6, 9]
>>> b
[6, 8, 9]
>>> a + b
[3, 6, 9, 6, 8, 9]
>>> ab = a + b
>>> ab
[3, 6, 9, 6, 8, 9]
>>> a
[3, 6, 9]
>>> b
[6, 8, 9]
>>> a.extend(b)
>>> a
[3, 6, 9, 6, 8, 9]
>>> len(a)
6
>>> aa[5]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    aa[5]
NameError: name 'aa' is not defined
>>> a[5]
9
>>> a[5] = 00
>>> a[5] = 99
>>> a[6]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a[6]
IndexError: list index out of range
>>> a[6] = 77
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a[6] = 77
IndexError: list assignment index out of range
>>> a.append(77)
>>> a.append(44)
>>> a
[3, 6, 9, 6, 8, 99, 77, 44]
>>> len(a)
8
>>> a.append(66, 33)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.append(66, 33)
TypeError: list.append() takes exactly one argument (2 given)
>>> a.append([66, 33])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33]]
>>> a.extend([22, 88])
>>> a
[3, 6, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(2, 80)
>>> a
[3, 6, 80, 9, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(4, 45)
>>> a
[3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.insert(0, 555)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [66, 33], 22, 88]
>>> a.pop()
88
>>> a.pop()
22
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [66, 33]]
>>> a.pop()
[66, 33]
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44]
>>> a.index(3)
1
>>> a.index(555)
0
>>> a.index(9)
4
>>> a.index(22222)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.index(22222)
ValueError: 22222 is not in list
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44]
>>> a.append(b)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, 44, [6, 8, 9]]
>>> a.remove(44)
>>> a
[555, 3, 6, 80, 9, 45, 6, 8, 99, 77, [6, 8, 9]]
>>> a.remove([6])
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.remove([6])
ValueError: list.remove(x): x not in list

>>> a.pop()
[6, 8, 9]
>>> t = a.pop()

>>> t
77
>>> t = a.pop()
>>> t
99
>>> a
[555, 3, 6, 80, 9, 45, 6, 8]
>>> a3 = a.pop()

>>> a3
8
>>> a3
8
>>> a3[2] = 7777
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a3[2] = 7777
TypeError: 'int' object does not support item assignment
>>> a.append([1, 2, 3, 4])
>>> a
[555, 3, 6, 80, 9, 45, 6, [1, 2, 3, 4]]
>>> a.pop()
[1, 2, 3, 4]
>>> a.insert[a3[2] = 7777
	 
SyntaxError: invalid syntax
>>> 
>>> a3
8
>>> type(a3)
<class 'int'>
>>> a
[555, 3, 6, 80, 9, 45, 6]
>>> a = [3, 6, 9]
>>> 
========================== RESTART: Shell =========================
>>> a = [4, 6, 5.6, 7.5, 'ace', 'korea', 3]
>>> a
[4, 6, 5.6, 7.5, 'ace', 'korea', 3]
>>> type(a)
<class 'list'>
>>> len(a)
7
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> b = ['서울', '부산', '대구']
>>> a
[4, 5.6, 6, 7.5, 'ace', 'korea', 3]
>>> b
['서울', '부산', '대구']
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> a
[4, 5.6, 6, 7.5, 'ace', 'korea', 3]
>>> b
['서울', '부산', '대구']
>>> a == b
False
>>> a.__eq__(b)
False
>>> a.append(b)
>>> a
[4, 5.6, 6, 7.5, 'ace', 'korea', 3, ['서울', '부산', '대구']]
>>> a + b
[4, 5.6, 6, 7.5, 'ace', 'korea', 3, ['서울', '부산', '대구'], '서울', '부산', '대구']
>>> bb = a + b
>>> a[3] = 5
>>> a
[4, 5.6, 6, 5, 'ace', 'korea', 3, ['서울', '부산', '대구']]
>>> 
>>> t = (30, 50, 70)
>>> len(t)
3
>>> t[0]
30
>>> t[1], t[2]
(50, 70)
>>> t.index(30)
0
>>> t.index(50)
1
>>> t.index(40)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    t.index(40)
ValueError: tuple.index(x): x not in tuple
>>> t.count(30)
1
>>> t.count(220)
0
>>> t[1] = 400
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    t[1] = 400
TypeError: 'tuple' object does not support item assignment
>>> type(t)
<class 'tuple'>
>>> list(t)
[30, 50, 70]
>>> type(t)
<class 'tuple'>
>>> tt = list(t)
>>> tt
[30, 50, 70]
>>> t
(30, 50, 70)
>>> tt[2] = 99
>>> tt
[30, 50, 99]
>>> t = tuple(tt)
>>> t
(30, 50, 99)
>>> 
>>> 
>>> i = 100
>>> j = 300
>>> i
100
>>> j
300
>>> t = i
>>> i = j
>>> j = t
>>> 
>>> i
300
>>> j
100
>>> i, j = j, i
>>> i
100
>>> j
300
>>> i, j = j, i ## data 맞교환
>>> 
>>> z = 10, 20, 30
>>> z
(10, 20, 30)
>>> type(z)
<class 'tuple'>
>>> z1, z2, z3 = z
>>> 
>>> 
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'bb', 'i', 'j', 't', 'tt', 'z', 'z1', 'z2', 'z3']
>>> del a, b, bb, i, j, tt
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 't', 'z', 'z1', 'z2', 'z3']
>>> del t
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'z', 'z1', 'z2', 'z3']
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> 
>>> 
>>> 
>>> a = {1, 2, 3, 4, 5}
>>> 
>>> b = {2, 4, 6}
>>> type(a)
<class 'set'>
>>> a
{1, 2, 3, 4, 5}
>>> b
{2, 4, 6}
>>> a | b
{1, 2, 3, 4, 5, 6}
>>>  a & b
 
SyntaxError: unexpected indent
>>> a & b
{2, 4}
>>> a - b
{1, 3, 5}
>>> b - a
{6}
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> a | b
{1, 2, 3, 4, 5, 6}
>>> 
>>> a.intersection(b)
{2, 4}
>>> a & b
{2, 4}
>>> len(a)
5
>>> len(b)
3
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> a.add(2)
>>> a.add(2)
>>> a
{1, 2, 3, 4, 5}
>>> k.append(2)
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    k.append(2)
NameError: name 'k' is not defined
>>> k = [ ]
>>> k.append(2)
>>> k.append(2)
>>> k
[2, 2]
>>> a.remove(1)
>>> 2 in a
True
>>> 2.issubset(a)
SyntaxError: invalid syntax
>>> a.add(1)
>>> a.add(4)
>>> a.add(4)
>>> a.add(5)
>>> a
{2, 3, 4, 5, 1}
>>> a2 = {2, 3}
>>> a2
{2, 3}
>>> a2.issubset(a)
True
>>> a2.issuperset(a)
False
>>> 
>>> d = {'이름':'강호동', '나이':51, '직업' : 'MC'}
>>> type(d)
<class 'dict'>
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['이름']
'강호동'
>>> d['나이']
51
>>> d.keys()
dict_keys(['이름', '나이', '직업'])
>>> d.values()
dict_values(['강호동', 51, 'MC'])
>>> d.items()
dict_items([('이름', '강호동'), ('나이', 51), ('직업', 'MC')])
>>> for key, value in d.items():
	print(key, value)

	
이름 강호동
나이 51
직업 MC
>>> for i, j in d.items():
	print(i, ' ===> ', j)

	
이름  ===>  강호동
나이  ===>  51
직업  ===>  MC
>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> ㅇ
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    ㅇ
NameError: name 'ᄋ' is not defined
>>> d
{'이름': '강호동', '나이': 51, '직업': 'MC'}
>>> d.update({'수입' :30})
>>> d.get('나이')
51
>>> d.popitem()
('수입', 30)
>>> d
{'이름': '강호동', '나이': 51, '직업': 'MC'}
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.popitem()
('직업', 'MC')
>>> d
{'이름': '강호동', '나이': 51}
>>> ac = a.copy()
>>> id(ac)
1916008921120
>>> a is ac
False
>>> True & False
False
>>> True | False
True
>>> True ^ False
True
>>> True ^ True
False
>>> ~True
-2
>>> ~0
-1
>>> 
========================== RESTART: Shell =========================
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> type(a)
<class 'list'>
>>> len(a)
3
>>> a[0]
1
>>> a[1]
2
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    a[3]
IndexError: list index out of range
>>> a[3] = 4
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    a[3] = 4
IndexError: list assignment index out of range
>>> a.append(4)
>>> 
>>> a
[1, 2, 3, 4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a.append(66)
>>> a
[1, 2, 3, 4, 5, 66]
>>> a.append([88, 99])
>>> 
>>> a
[1, 2, 3, 4, 5, 66, [88, 99]]
>>>  len(a)
 
SyntaxError: unexpected indent
>>> len(a)
7
>>> a[6]
[88, 99]
>>> a[6][0]
88
>>> a[6][1]
99
>>> a[6][1]
99
>>> a[6][2]
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    a[6][2]
IndexError: list index out of range
>>> a.append(100)
>>> a.append(220)
>>> a.pop()
220
>>> len(a)
8
>>> a
[1, 2, 3, 4, 5, 66, [88, 99], 100]
>>> a.insert(2,7)
>>> a.insert(0,9)
>>> a.reverse()
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    a.sort(reverse=True)
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.sort(reverse=False)
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    a.sort(reverse=False)
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.remove(2)
>>> a
[100, [88, 99], 66, 9, 7, 5, 4, 3, 1]
>>> a
[100, [88, 99], 66, 9, 7, 5, 4, 3, 1]
>>> a = [1, 2, 3, 4, 5, 66, [88, 99], 100]
>>> a
[1, 2, 3, 4, 5, 66, [88, 99], 100]
>>> a.insert(2,7)
>>> a
[1, 2, 7, 3, 4, 5, 66, [88, 99], 100]
>>> a.insert(0,9)
>>> a
[9, 1, 2, 7, 3, 4, 5, 66, [88, 99], 100]
>>> a.reverse()
>>> 
>>> a
[100, [88, 99], 66, 5, 4, 3, 7, 2, 1, 9]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    a.sort(reverse=True)
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a
[100, [88, 99], 66, 9, 7, 5, 4, 3, 2, 1]
>>> a.sort(reverse=False)
Traceback (most recent call last):
  File "<pyshell#277>", line 1, in <module>
    a.sort(reverse=False)
TypeError: '<' not supported between instances of 'list' and 'int'
>>> a.remove([88, 99])
>>> a
[100, 66, 9, 7, 5, 4, 3, 2, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5, 7, 9, 66, 100]
>>> a.sort(reverse=True)
>>> a
[100, 66, 9, 7, 5, 4, 3, 2, 1]
>>> a.sort(reverse=False)
>>> a
[1, 2, 3, 4, 5, 7, 9, 66, 100]
>>> a.remove(2)
>>> a
[1, 3, 4, 5, 7, 9, 66, 100]
>>> a.remove(20)
Traceback (most recent call last):
  File "<pyshell#288>", line 1, in <module>
    a.remove(20)
ValueError: list.remove(x): x not in list
>>> a.count(3)
1
>>> a
[1, 3, 4, 5, 7, 9, 66, 100]
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a.count(4)
1
>>> a.append(1)
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1]
>>> a.append(3)
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1, 3]
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a.index(3)
1
>>> a.count(3)
2
>>> a.count(1)
2
>>> a.count(4)
1
>>> a.extend(1)
Traceback (most recent call last):
  File "<pyshell#302>", line 1, in <module>
    a.extend(1)
TypeError: 'int' object is not iterable
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1, 3]
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1, 3]
>>> a.append(2)
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1, 3, 2]
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1, 3, 2]
>>> type(a)
<class 'list'>
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1, 3, 2]
>>> a.append(2)
>>> a
[1, 3, 4, 5, 7, 9, 66, 100, 1, 3, 2, 2]
>>> a.clear()
>>> a
[]
>>> a.append(1)
>>> a
[1]
>>> a.append(2)
>>> a
[1, 2]
>>> a = [3, 6, 9, 12, 15]
>>> [ : ]
SyntaxError: invalid syntax
>>> print[]
SyntaxError: invalid syntax
>>> [:]
SyntaxError: invalid syntax
>>> a[]
SyntaxError: invalid syntax
>>> a[:]
[3, 6, 9, 12, 15]
>>> a[1:3]
[6, 9]
>>> a[-5:-2]
[3, 6, 9]
>>> a[2:]
[9, 12, 15]
>>> a[-5:-2]
[3, 6, 9]
>>> a[-3:-1]
[9, 12]
>>> a[-2:]
[12, 15]
>>> a[-1]
15
>>> a[0]
3
>>> a[-5]
3
>>> a
[3, 6, 9, 12, 15]
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    a.remove(2)
ValueError: list.remove(x): x not in list
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#337>", line 1, in <module>
    a.remove(2)
ValueError: list.remove(x): x not in list
>>> a.remove[2]
Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    a.remove[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a
[3, 6, 9, 12, 15]
>>> a.count(3)
1
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#341>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a = [1, 2, 3]

>>> a
[1, 2, 3]
>>> a.remove(2)
>>> a
[1, 3]
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#347>", line 1, in <module>
    a.index(2)
ValueError: 2 is not in list
>>> a.index(1)
0
>>> a.clear()
>>> a
[]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = [1, 3, 5, 7, 9]
>>> ca = a.copy()
>>> a
[1, 3, 5, 7, 9]
>>> ca
[1, 3, 5, 7, 9]
>>> a.append(11)
>>> a
[1, 3, 5, 7, 9, 11]
>>> ca
[1, 3, 5, 7, 9]
>>> b = a
>>> 
>>> a.append(13)
>>> a
[1, 3, 5, 7, 9, 11, 13]
>>> a.append(15)
>>> 
>>> a
[1, 3, 5, 7, 9, 11, 13, 15]
>>> a.append(17)
>>> 
>>> a
[1, 3, 5, 7, 9, 11, 13, 15, 17]
>>> id(a) #copy와 대입의 차이
2811707505920
>>> id(a)
2811707505920
>>> id(b)
2811707505920
>>> id(ca)
2811707292160
>>> id(b), id(ca)
(2811707505920, 2811707292160)
>>> 
>>> a[3]
7
>>> a[5]
11
>>> a
[1, 3, 5, 7, 9, 11, 13, 15, 17]
>>> 
>>> 
========================== RESTART: Shell =========================
>>> py
Traceback (most recent call last):
  File "<pyshell#380>", line 1, in <module>
    py
NameError: name 'py' is not defined
>>> korea
Traceback (most recent call last):
  File "<pyshell#381>", line 1, in <module>
    korea
NameError: name 'korea' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#382>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
========================== RESTART: Shell =========================
>>> korea
Traceback (most recent call last):
  File "<pyshell#383>", line 1, in <module>
    korea
NameError: name 'korea' is not defined
>>> 
>>> 
===================== RESTART: C:/dd/day3-2.py ====================
0	1	2	3	4	5	6	7	8	9	
>>> 
====== RESTART: C:/dd/day3-2.py ======
0 1 2 3 4 5 6 7 8 9 
>>> 
====== RESTART: C:/dd/day3-2.py ======
0 2 4 6 8 
>>> 
====== RESTART: C:/dd/day3-2.py ======
1 6 
>>> 
====== RESTART: C:/dd/day3-2.py ======
100 95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 
>>> 
====== RESTART: C:/dd/day3-2.py ======
1 100001 200001 300001 400001 500001 600001 700001 800001 900001 1000001 
>>> 
====== RESTART: C:/dd/day3-2.py ======
1 100001 200001 300001 400001 500001 600001 700001 800001 900001 
>>> 
====== RESTART: C:/dd/day3-2.py ======
1 1
2 3
3 6
4 10
5 15
6 21
7 28
8 36
9 45
>>> 
====== RESTART: C:/dd/day3-2.py ======
 i ==> 1  Sum ==>  1
 i ==> 2  Sum ==>  3
 i ==> 3  Sum ==>  6
 i ==> 4  Sum ==>  10
 i ==> 5  Sum ==>  15
 i ==> 6  Sum ==>  21
 i ==> 7  Sum ==>  28
 i ==> 8  Sum ==>  36
 i ==> 9  Sum ==>  45
>>> 
====== RESTART: C:/dd/day3-2.py ======
 i ==> 1  Sum ==>  1
 i ==> 2  Sum ==>  3
 i ==> 3  Sum ==>  6
 i ==> 4  Sum ==>  10
 i ==> 5  Sum ==>  15
 i ==> 6  Sum ==>  21
 i ==> 7  Sum ==>  28
 i ==> 8  Sum ==>  36
 i ==> 9  Sum ==>  45
 몇 단 출력 : 5
 5 * 1 = 5 
 5 * 2 = 10 
 5 * 3 = 15 
 5 * 4 = 20 
 5 * 5 = 25 
 5 * 6 = 30 
 5 * 7 = 35 
 5 * 8 = 40 
 5 * 9 = 45 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 i ==> 1  Sum ==>  1
 i ==> 2  Sum ==>  3
 i ==> 3  Sum ==>  6
 i ==> 4  Sum ==>  10
 i ==> 5  Sum ==>  15
 i ==> 6  Sum ==>  21
 i ==> 7  Sum ==>  28
 i ==> 8  Sum ==>  36
 i ==> 9  Sum ==>  45
0 1 2 3 4 5 6 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 i ==> 1  Sum ==>  1
 i ==> 2  Sum ==>  3
 i ==> 3  Sum ==>  6
 i ==> 4  Sum ==>  10
 i ==> 5  Sum ==>  15
 i ==> 6  Sum ==>  21
 i ==> 7  Sum ==>  28
 i ==> 8  Sum ==>  36
 i ==> 9  Sum ==>  45
1 2 3 4 5 6 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 i ==> 1  Sum ==>  1
 i ==> 2  Sum ==>  3
 i ==> 3  Sum ==>  6
 i ==> 4  Sum ==>  10
 i ==> 5  Sum ==>  15
 i ==> 6  Sum ==>  21
 i ==> 7  Sum ==>  28
 i ==> 8  Sum ==>  36
 i ==> 9  Sum ==>  45
1 2 4 5 6 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 i ==> 1  Sum ==>  1
 i ==> 2  Sum ==>  3
 i ==> 3  Sum ==>  6
 i ==> 4  Sum ==>  10
 i ==> 5  Sum ==>  15
 i ==> 6  Sum ==>  21
 i ==> 7  Sum ==>  28
 i ==> 8  Sum ==>  36
 i ==> 9  Sum ==>  45
1 2 4 5 6 
>>> 
====== RESTART: C:/dd/day3-2.py ======
1 2 4 5 6 
>>> 
====== RESTART: C:/dd/day3-2.py ======
1  2  
>>> 
====== RESTART: C:/dd/day3-2.py ======
 몇 단 출력 : 5
 5 * 1 = 5 
 5 * 2 = 10 
 5 * 3 = 15 
 5 * 4 = 20 
 5 * 5 = 25 
 5 * 6 = 30 
 5 * 7 = 35 
 5 * 8 = 40 
 5 * 9 = 45 
 몇 단 출력 : 6
 6 * 1 = 6 
 6 * 2 = 12 
 6 * 3 = 18 
 6 * 4 = 24 
 6 * 5 = 30 
 6 * 6 = 36 
 6 * 7 = 42 
 6 * 8 = 48 
 6 * 9 = 54 
 몇 단 출력 : 0
 0 * 1 = 0 
 0 * 2 = 0 
 0 * 3 = 0 
 0 * 4 = 0 
 0 * 5 = 0 
 0 * 6 = 0 
 0 * 7 = 0 
 0 * 8 = 0 
 0 * 9 = 0 
 몇 단 출력 : 
====== RESTART: C:/dd/day3-2.py ======
 몇 단 출력 : 5
 5 * 1 = 5 
 5 * 2 = 10 
 5 * 3 = 15 
 5 * 4 = 20 
 5 * 5 = 25 
 5 * 6 = 30 
 5 * 7 = 35 
 5 * 8 = 40 
 5 * 9 = 45 
 몇 단 출력 : 6
 6 * 1 = 6 
 6 * 2 = 12 
 6 * 3 = 18 
 6 * 4 = 24 
 6 * 5 = 30 
 6 * 6 = 36 
 6 * 7 = 42 
 6 * 8 = 48 
 6 * 9 = 54 
 몇 단 출력 : 0
 Good - bye!!! 
>>> 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 몇 단 출력 : 455
 455 * 1 = 455 
 455 * 2 = 910 
 455 * 3 = 1365 
 455 * 4 = 1820 
 455 * 5 = 2275 
 455 * 6 = 2730 
 455 * 7 = 3185 
 455 * 8 = 3640 
 455 * 9 = 4095 
 몇 단 출력 : 0
 Good - bye!!! 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 몇 단 출력 : 9
 9 * 1 = 9 
 9 * 2 = 18 
 9 * 3 = 27 
 9 * 4 = 36 
 9 * 5 = 45 
 9 * 6 = 54 
 9 * 7 = 63 
 9 * 8 = 72 
 9 * 9 = 81 
 몇 단 출력 : 0
 Good - bye!!! 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 몇 단 출력 : 10
 몇 단 출력 : 1
 몇 단 출력 : 4
 4 * 1 = 4 
 4 * 2 = 8 
 4 * 3 = 12 
 4 * 4 = 16 
 4 * 5 = 20 
 4 * 6 = 24 
 4 * 7 = 28 
 4 * 8 = 32 
 4 * 9 = 36 
 몇 단 출력 : 95
 몇 단 출력 : 0
 Good - bye!!! 
>>> 
====== RESTART: C:/dd/day3-2.py ======
 참 
목요일
>>> 
====== RESTART: C:/dd/day3-2.py ======
 참 
목요일
>>> 
====== RESTART: C:/dd/day3-2.py ======
 정수 입력 : 85
85 집에 가세요.
>>> 
====== RESTART: C:/dd/day3-2.py ======
 정수 입력 : 8542
8542 참 잘했어요
8542 집에 가세요.
>>> 
====== RESTART: C:/dd/day3-2.py ======
 정수 입력 : 150
 정수 입력 : -20
 정수 입력 : 100
100 참 잘했어요
 정수 입력 : 25
25 집에 가세요.
 정수 입력 : 95
95 참 잘했어요
 정수 입력 : 44
44 집에 가세요.
 정수 입력 : 
====== RESTART: C:/dd/day3-2.py ======
 정수 입력 : 30
30 집에 가세요.
 정수 입력 : 50
50 집에 가세요.
 정수 입력 : 90
90 참 잘했어요
 정수 입력 : 55
55 집에 가세요.
 정수 입력 : 85
85 집에 가세요.
 정수 입력 : 75
75 집에 가세요.
 정수 입력 : 0
>>> 
====== RESTART: C:/dd/day3-2.py ======
 정수 입력 : 60
60 양
 정수 입력 : 95
95 수
 정수 입력 : 45
45 가
 정수 입력 : 69
69 양
 정수 입력 : 85
85 우
 정수 입력 : 75
75 미
 정수 입력 : 39
39 가
 정수 입력 : 69
69 양
 정수 입력 : 100
100 수
 정수 입력 : 