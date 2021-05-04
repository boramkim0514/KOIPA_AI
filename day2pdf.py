Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count = 3
>>> print('I have a count apple')
I have a count apple
>>> print('I have a {} apple'.format(count))
I have a 3 apple
>>> print('I have a {} apple'.format(counts))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print('I have a {} apple'.format(counts))
NameError: name 'counts' is not defined
>>> print('I have a {0} apple'.format(count))
I have a 3 apple
>>> print('I have a [] apple'.format(counts))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('I have a [] apple'.format(counts))
NameError: name 'counts' is not defined
>>> print('I have a [] apple'.format(count))
I have a [] apple
>>> print('I have a () apple'.format(count))
I have a () apple
>>> a = 30
>>> b = 2.345
>>> c = "corea"
>>> print(" {} {} {}".format(a, b, c))
 30 2.345 corea
>>> print(" {0} {1} {2}".format(a, b, c))
 30 2.345 corea
>>> print(" {2} {0} {1}".format(a, b, c))
 corea 30 2.345
>>> 
>>> print("[{:10}] [{:10}] [{:10}]".format(a, b, c))
[        30] [     2.345] [corea     ]
>>> print("[{0:10}] [{1:10}] [{:10}]".format(a, b, c))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print("[{0:10}] [{1:10}] [{:10}]".format(a, b, c))
ValueError: cannot switch from manual field specification to automatic field numbering
>>> print("[{0:10}] [{1:10}] [{2:10}]".format(a, b, c))
[        30] [     2.345] [corea     ]
>>> print("[{2:10}] [{0:10}] [{1:10}]".format(a, b, c))
[corea     ] [        30] [     2.345]
>>> 