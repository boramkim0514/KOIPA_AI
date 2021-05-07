
'''
color = {'black': '검정', 'yellow':'노랑', 'blue':'파랑'} #key & value 쌍으로 된 데이터 -> 사전 인수 


def disp_color(**x):
    for key, value in x.items():
        print(key, value)
    print(x[*['black'], x['yellow'], x['blue'])
        
disp_color(**color)
'''

## 지역 변수 ##

gg = 500
def f1(x):
    global gg ## 전역변수 gg를 뜻함
    gg = 2000000 ## 전역변수 ㅎㅎ 값을 변경함
    print(gg, 'x ==> ', x*x)

def f2(x, y):   
    t = x*y ## tㄹ는 지역 변수, f2함수내에서만 통용된다.
    print(gg, t)

f1(10)
print(' gg ==> ', gg)
f2(100, 300)
print(' gg ==> ', 99)


