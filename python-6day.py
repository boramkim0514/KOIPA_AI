gg = 500 #전역변수
CUR_YEAR = 2021  #전역변수

class Date(object):
    def __init__(self, x, y):
        self.year = year #왼쪽 멤버변수 오른 쪽 넘겨받은 값
        self.month = month
        print('Date __init__ ')

    #def gc leak #garbage collector 
    def Call_age(self, year):
        return CUR_YEAR - year +1
        
    def disp_Date(self):
        print('{}년 {}월'.format(self.year, self.month))

d1 = Date(2021, 10)
d2 = Date(2000, 12)

class Man(object): 
    cnt = 0 ## class함수

    @staticmethod #장식자 decorator
    def get_cnt1():
        return Man.cnt
    
    @classmethod
    def get_cnt2(cls):
        return Man.cnt

## 객체 생성시 자동 호출(constructor)되는 함수, 생성자
    def __init__(self, name, year, month):
        Date.__init_(self, year, month)
        self.name = name
        self.age = age
        Man.cnt += 1
        print(' Man __init__ ')


## 객체 소멸시 자동 호출(destructor)되는 함수, 소멸자
    def __del__(self):
        Man.cnt += 1
        print(' Man __del__ ')

##객체 출력시 자동으로 호출되는 함수, 기본값은 객체의 id 값        
    def __str__(self):
        return '{}님은 {}살'.format(self.name, self.age)

## method 재정의(override) 
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else: 
            return False

def __add__(self, num):
    self.age = self.age + num

def __sub__(self, num):
    self.age -= num

def __disp_Man(self):
        return('{}님은 {}살'.format(self.name, self.age))
    
def get_name(self):
    return self.name
    
def get_age(self):
    return self.age

def set_name(self, name):
    self.name = name

def set_age(self, age):
    self.age = age

#print('현재 객체생성수는: {}'.format(Man.cnt))
#print(' 현재 객체생성수는 : {}'.format(Man.getcnt1)

m1 = Man('손흥민', 30)
m2 = Man('이강인', 21)
m3 = Man('손흥민', 30)

#print(m1)
#print(m2)
#print(m1.__str__())
#print(m2.__str__())

#print(m1 == m3)

#m1 + 2
#m2 - 4
m1.disp_Man()
m2.disp_Man(3)

