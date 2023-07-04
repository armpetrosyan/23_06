import math


def calculate_area(a):
    res = math.pi * pow(a, 2)
    return res


r = float(input('Enter Radius: '))

if r == 0 or r < 0:
    print('Not Able to Calculate')
i = calculate_area(r)

print(i)
