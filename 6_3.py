#kalkulyator

amallar = input('Amallardan (+ , - , * , /) birini tanlang: ')
son1 = int(input('1-sonni kiriting: '))
son2 = int(input('2-sonni kiriting: '))

if amallar == '+':
    print(son1+son2)
elif amallar == '-':
    print(son1-son2)
elif amallar == '*':
    print(son1*son2)
elif amallar == '/':
    print(son1/son2)
else:
    print('Siz xato amal kiritdingiz!')