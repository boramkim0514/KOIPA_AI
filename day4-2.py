Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## 사용자 정의 함수

def f1(): ## 함수 정의 
    pass ## 아무일도 하지 않음 
def f2():
    print(' f2... ')

def f3(x):
    print(x, '가 좋아요')
    return None

def f4(x, y):
    print(' {} + {} = {}'.format(x, y, x+y))
    return None


def plus(x, y):
    print(' {} + {} = {}'.format(x, y, x+y))
    return None

def minus(x, y):
    return x-y

f1() ## 함수 호출
f2()
print(f3(100))
f3(100)
f3('BTS')
f4(100, 200)
plus(200, 300)
minus(300, 200)
retv = minus(300, 200)
print(retv)

print(' 20 - 5 = ', minus(20, 5))