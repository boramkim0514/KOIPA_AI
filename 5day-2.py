class Korea(object): ## class define(선언)
    def __init__(self, city, pop): ## 생성자 함수 
        self.city = city
        self.pop = pop
        print(' Korea __init__ : 생성자')

    def __del__(self):## 소멸자 함수
        print('Korea__del__ : 소멸자 ' )
        pass

    def __str__(self): 
        return " {}인구는 ==> {}만명 ".format(self.city, self.pop)

    def disp_korea(self): 
        print(self.city, '인구는 ', self.pop, '만명')

    def get_city(self):
        return self.city
    
    def get_pop(self):
        return self.pop

    def set_city(self, city):
        self.city = city

    def set_pop(self, pop):
        self.pop = pop
        

k1 = Korea('서울시', 950)
k2 = Korea('부산시', 700)
k2.pop = 360

k1.disp_korea()
k2.disp_korea()

k1.city = '수원시'
k1.pop = 110

print(k1.get_city(), k1.get_pop())
print(k2.get_city(), k2.get_pop())

print('k1 ==> ', k1)

print(k1.__str__())
print(k1)

print(k2.__str__())
print(k2)



