import math
num = int(input('Please enter the number you want to check the range up to: '))
x = 2
i = 2
while x <= num :
    while i <= int(math.sqrt(x)+1):
        if x % i == 0 :
           break
        i += 1
    else :
        print(f'{x} is one of our prime numbers ^-^')
    x += 1
