numbers = [101, 202, 505,]

i = 0
while i < len(numbers):
    number = numbers[i]
    if number % 2 == 0:
        print(number)
    i += 1

print('Конец программы')