Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a[3]
NameError: name 'a' is not defined
>>> a = [1, 3, 5, 7, 9]
>>> a[3]
7
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[5]
IndexError: list index out of range
>>> a[4]
9
>>> a[:3]
[1, 3, 5]
>>> a[:5]
[1, 3, 5, 7, 9]
>>> a[5:]
[]
>>> a[2:6]
[5, 7, 9]
>>> a[:5:3]
[1, 7]
>>> a[-1]
9
>>> a[-6:-3]
[1, 3]
>>> b = [21, 23, 25]
>>> len(b)
3
>>> a.extend(b)
>>> a.extend([27, 29, 31])
>>> a
[1, 3, 5, 7, 9, 21, 23, 25, 27, 29, 31]
>>> a.pop()
31
>>> a
[1, 3, 5, 7, 9, 21, 23, 25, 27, 29]
>>> a.pop()
29
>>> a
[1, 3, 5, 7, 9, 21, 23, 25, 27]
>>> a.append(b)
>>> a
[1, 3, 5, 7, 9, 21, 23, 25, 27, [21, 23, 25]]
>>> 
>>> 
>>> 
>>> #3-2-1 tuple
>>> a = [1, 2, 3, 4, 5]
>>> a * 2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> a + 2
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a + 2
TypeError: can only concatenate list (not "int") to list
>>> a - 2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a - 2
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> a / b
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a / b
TypeError: unsupported operand type(s) for /: 'list' and 'list'
>>> b = [10, 20, 30]
>>> b
[10, 20, 30]
>>> b.append('seoul')
>>> b
[10, 20, 30, 'seoul']
>>> b.append('pusan')
>>> b
[10, 20, 30, 'seoul', 'pusan']
>>> b.append(4.789)
>>> len(b)
6
>>> ta = (1, 2, 3, 4, 5)
>>> ta
(1, 2, 3, 4, 5)
>>> type(ta)
<class 'tuple'>
>>> ta.count(2)
1
>>> ta.index(5)
4
>>> 
>>> 
>>> #3-2-2 tuple
>>> a[0] = 100
>>> ta[0]
1
>>> ta[1]
2
>>> ta[2] = 100 #tuple 값 변경 불가
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    ta[2] = 100 #tuple 값 변경 불가
TypeError: 'tuple' object does not support item assignment
>>> ta[2] = 100
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    ta[2] = 100
TypeError: 'tuple' object does not support item assignment
>>> k = 1, 2, 3
>>> type(k)
<class 'tuple'>
>>> k1 = (5, 7, 9)
>>> k1[2]
9
>>> type(k1)
<class 'tuple'>
>>> k = list(k)
>>> type(k)
<class 'list'>
>>> k.append(5)
>>> k.append(7)
>>> 
>>> 
>>> #3 - 2 - 3 tuple
>>> k = tuple(k)
>>> k2 = 10, 20, 30 #패킹
>>> k10, k20, k30 = k2
>>> k10
10
>>> k20
20
>>> k30 #언패킹
30
>>> k10, k30 = k30, k10 # 값 맞교환( 정수, 문자열 다 가능)
>>> s1 = "서울"
>>> b1 = "부산"
>>> s1, b1 = b1, s1
>>> print(s1, b1)
부산 서울
>>> a = [1, 2, 3]
>>> k = [55, 66]
>>> a.append(k)
>>> a
[1, 2, 3, [55, 66]]
>>> ca = a.copy()
>>> ca
[1, 2, 3, [55, 66]]
>>> import copy
>>> cca = copy.copy(a)
>>> 
>>> #3-3-1 set
>>> a = {1, 2, 3, 4, 5}
>>> b = {2, 4, 6, 8, 10}
>>> type(a), type(b)
(<class 'set'>, <class 'set'>)
>>> a | b #합집합
{1, 2, 3, 4, 5, 6, 8, 10}
>>> ㅁ & ㅠ # 교집합
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    ㅁ & ㅠ # 교집합
NameError: name 'ᄆ' is not defined
>>> a & b
{2, 4}
>>> a - b
{1, 3, 5}
>>> b - a
{8, 10, 6}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 8, 10}
>>> a.intersection(b)
{2, 4}
>>> a.difference(b)
{1, 3, 5}
>>> len(a)
5
>>> len(b)
5
>>> a[0] #set은 순차개념이 없다
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a[0] #set은 순차개념이 없다
TypeError: 'set' object is not subscriptable
>>> a[0] #set은 순차개념이 없다
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a[0] #set은 순차개념이 없다
TypeError: 'set' object is not subscriptable
>>> a.add(6)
>>> a
{1, 2, 3, 4, 5, 6}
>>> a.add(7)
>>> 
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.add(7)
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> a.count(6)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a.count(6)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(6)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.index(6)
AttributeError: 'set' object has no attribute 'index'
>>> a
{1, 2, 3, 4, 5, 6, 7}
>>> a.remove(4)
>>> a
{1, 2, 3, 5, 6, 7}
>>> a.discard(2)
>>> a
{1, 3, 5, 6, 7}
>>> a.add(3)
>>> a
{1, 3, 5, 6, 7}
>>> a.add(5)
>>> a
{1, 3, 5, 6, 7}
>>> c = {5, 6}
>>> c.issubset(a)
True
>>> c.issubset(b)
False
>>> b
{2, 4, 6, 8, 10}
>>> a.issuperset(b)
False
>>> a.issuperset(c)
True
>>> c.issuperset(a)
False
>>> s1 = {'seoul', 'la'}
>>> s
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s1
{'seoul', 'la'}
>>> s2 = {'seoul', 'la'}
>>> s2
{'seoul', 'la'}
>>> s3 = {'seoul'}
>>> s1 - s3
{'la'}
>>> s1 | s2
{'seoul', 'la'}
>>> s1 & s3
{'seoul'}
>>> s3.issubset(s1)
True
>>> s1
{'seoul', 'la'}
>>> s2
{'seoul', 'la'}
>>> s3
{'seoul'}
>>> s2.issubset(s3)
False
>>> s5 = {20, 40, 50, 4.789, '서울', '부산'}
>>> s5
{50, 4.789, 20, 40, '부산', '서울'}
>>> print(s5)
{50, 4.789, 20, 40, '부산', '서울'}
>>> type(s5)
<class 'set'>
>>> 
>>> 
>>> #3-4-1 dict
>>> 
>>> a = {'이름' : '김철수', '나이':30, '직업': '학생'}
>>> a['이름']
'김철수'
>>> a['나이']
30
>>> a['직업']
'학생'
>>> a.items()
dict_items([('이름', '김철수'), ('나이', 30), ('직업', '학생')])
>>> a.keys()
dict_keys(['이름', '나이', '직업'])
>>> a.values()
dict_values(['김철수', 30, '학생'])
>>> b = {1: 'one', 2: 'two', 3: 'three'}
>>> type(b)
<class 'dict'>
>>> b[1]
'one'
>>> for i , j in b.itmes():
	print(i,j)

	
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    for i , j in b.itmes():
AttributeError: 'dict' object has no attribute 'itmes'
>>> for i, j in b.items():
	print(i,j)

	
1 one
2 two
3 three
>>> 
>>> for key, value in a.items():
	print(key, value)

	
이름 김철수
나이 30
직업 학생
>>> for key value in b.items():
	
SyntaxError: invalid syntax
>>> for key, value in b.items():
	print(key, value)

	
1 one
2 two
3 three
>>> for key, value in a.items():
	print(key, "--->, value)
	      
SyntaxError: EOL while scanning string literal
>>> for key, value in a.items():
	print(key, "--->", value)

	
이름 ---> 김철수
나이 ---> 30
직업 ---> 학생
>>> print(a, b)
{'이름': '김철수', '나이': 30, '직업': '학생'} {1: 'one', 2: 'two', 3: 'three'}
>>> 
>>> 
>>> #3-4-2 dict
>>> b.pop(1)
'one'
>>> b.get(3)
'three'
>>> b
{2: 'two', 3: 'three'}
>>> b.update({4: 'four'})
>>> b
{2: 'two', 3: 'three', 4: 'four'}
>>> b.UPDATE({5:'five'})
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    b.UPDATE({5:'five'})
AttributeError: 'dict' object has no attribute 'UPDATE'
>>> b.update({5:'five'})
>>> b
{2: 'two', 3: 'three', 4: 'four', 5: 'five'}
>>> b.get(4)
'four'
>>> b.pop(4)
'four'
>>> b.popitem()
(5, 'five')
>>> b
{2: 'two', 3: 'three'}
>>> b.clear()
>>> b
{}
>>> week = {0: '일요일', 1:'월요일', 2:'화요일', 3:'수요일'}
>>> for key, value in week.items():
	print(key, '==>', value)

0 ==> 일요일
1 ==> 월요일
2 ==> 화요일
3 ==> 수요일
>>> w1 = {4: '목요일', 5:'금요일', 6:'토요일'}
>>> 
>>> week
{0: '일요일', 1: '월요일', 2: '화요일', 3: '수요일'}
>>> week1
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    week1
NameError: name 'week1' is not defined
>>> w1
{4: '목요일', 5: '금요일', 6: '토요일'}
>>> week.UPDATE(w1)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    week.UPDATE(w1)
AttributeError: 'dict' object has no attribute 'UPDATE'
>>> week.update(w1)
>>> 
>>> w1
{4: '목요일', 5: '금요일', 6: '토요일'}
>>> week
{0: '일요일', 1: '월요일', 2: '화요일', 3: '수요일', 4: '목요일', 5: '금요일', 6: '토요일'}
>>> for i, j in week.items():
	print(i,j)

	
0 일요일
1 월요일
2 화요일
3 수요일
4 목요일
5 금요일
6 토요일
>>> 
>>> #3-5-1 자료형 정리
>>> 
>>> 
>>> 
>>> 
>>> a = [1, 2, 3, 4, 5]
>>> b = (3, 5, 7, 9)
>>> c = {1, 3, 5, 7, 9}
>>> c2 = {1, 2, 3, 5}
>>> 2 in a
True
>>> 9 in b
True
>>> 3 in c
True
>>> 20 in c
False
>>> la = a
>>> 
>>> la == a
True
>>> a is la
True
>>> id(a)
2850336306560
>>> id(la)
2850336306560
>>> ca = a.copy()
>>> a == ca
True
>>> a is ca
False
>>> id(ca)
2850304746176
>>> c | c2
{1, 2, 3, 5, 7, 9}

>>> c & c2
{1, 3, 5}
>>> c - c2
{9, 7}
>>> c.symmetric_difference(c2)
{2, 7, 9}
>>> type(a)
<class 'list'>
>>> ta = tuple(a)
>>> la = list(ta)
>>> 
>>> 포함하고 있는가 in
SyntaxError: invalid syntax
>>> #값이 같은가? ==
>>> #id가 같은가? is
>>> #대칭차 - 서로에게 없는 것만 모아 놓은 것.
>>> list, tuple, set 상호 호환
SyntaxError: invalid syntax
>>> 
>>> 
>>> 