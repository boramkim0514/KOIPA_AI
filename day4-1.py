## 사용자 정의 함수
''''
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
'''
'''
## 덧셈만 할 줄 아는 계산기
def plus(x, y):
    print(' {} + {} = {}'.format(x, y, x+y))
    return None

def Add(x, y):
    return x+y

while True:
    number1 = int(input(' 첫 번째 수 : '))
    if number1 == 0:
        break
    number2 = int(input(' 두 번째 수 : '))

    plus(number1, number2)
    print(' {} + {} = {}'.format(number1, number2, number1+number2))
    
    retv = Add(number1, number2)
    #print(' {} +{} = {}'.format(number1, number2, retv))
'''
'''
def Talk(x, y):
    print(x, '님이', y, '번 말씀하셨다.')

def Aha(x):
    print(x, '누구나 딱 한 번 산다.')

print(' Start ')

name = input(' 이름 : ')
num = int(input(' 횟수 : '))


for i in range(1, num+1):
    Aha(i)

Talk(name, num) ## 함수 호출

print(' End ')
'''

## 초 간단 계산기

def Add(x, y):
    return x+y

def Sub(x, y):
    return x-y

def Mul(x, y):
    return x*y

def Div(x, y):
    return x//y

while True:
    print(' ** 간단 계산기 ** ')
    n1 = int(input('첫 번째 수 : '))
    if n1 == 0:
        break
    op = input(' [ + - * / ] : ')
    
    n2 = int(input(' 두 번째 수 : '))

    if op == '+':
        res = Add(n1, n2)
    elif op == '-':
        res = Sub(n1, n2)
    elif op == '*':
        res = Mul(n1, n2)
    elif op == '/':
        res = Div(n1, n2)
    else:
        print(op, '없는 연산입니다.')

    print('{} {} {} = {}'.format(n1, op, n2, res))
    
    
                        


            
    
