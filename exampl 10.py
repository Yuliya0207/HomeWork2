
number = int(input('Enter the number: '))
summa = 0

while (number > 0):
    digit = number % 9
    summa = summa + digit
    number = number // 9

print(summa)