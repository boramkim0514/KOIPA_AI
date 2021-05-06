# for 문
'''
Sum = 0

for i in range(1, 10, 1):
    Sum = Sum + i
    print(' i ==>' , i, ' Sum ==> ', Sum)
'''
'''

Sum = 0
    
#for i in range(1, 101, 1):
#for i in range(2, 101, 2):
#for i in range(1, 101, 2):

for i in range(100, 0, -5):
    Sum = Sum + i
    print(' i ==> ', i, ' Sum ==> ', Sum)

for i in range(1, 7):
    if i == 3: 
        #continue = skip
        break = loop 탈출 
    print(i, end = '  ')    
'''
'''
while True:
    dan = int(input(' 몇 단 출력 : '))
    
    if dan == 0:
        print(' Good - bye!!! ')        
        break

    if dan < 2 or dan > 9:
        continue
        
    for i in range(1, 10):
        print(' {} * {} = {} '.format(dan, i, dan*i))
'''
'''
if (3 < 2) and (3 == 3):
    print(' 참 '); print('목요일')
'''
while True: #다중 if문 
    
    score = int(input(' 정수 입력 : '))
    if score == 0:
        break

    if score > 100 or score < 0 :
        continue

    if score >= 90:
        print( score, '수')
    elif score >=80:
        print( score, '우')
    elif score >= 70:
        print( score, '미')
    elif score >= 60:
        print( score, '양')
    else:
        print( score, '가')
'''       
    


