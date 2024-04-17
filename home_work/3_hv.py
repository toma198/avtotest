def max_number(x,y):
    if x>y:
        print(x)
    else:
        print(y)


print('max_number:')
max_number(3,7)


def number_ask(x,y):
    if x-y == 135 or y-x == 135:
       print('yes')
    else:
       print('no')


print('number_ask:')
number_ask(137,2)


def name_season(month_number):
    if month_number in [1, 2, 12]:
        print('зима')
    elif month_number in range (3, 6):
        print('весна')
    elif month_number in range(6, 9):
        print('лето')
    elif month_number in range(9, 12):
        print('осень')
    else:
        print('не известный сезон')


print('seasons:')
name_season(1)
name_season(3)
name_season(12)

def ten_number(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')


ten_number(11, 15, 20)






