# программа с break (но его и УЖ ТЕМ БОЛЕЕ 
# continue лучше не использовать, если это возможно)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# i = 0

# for number in numbers:
#     if number == 0:
#         print('Нашли на итерации:', i+1)
#         break
#     i += 1

# print('Всего итераций выполнено:', i)    

# правильный ход решения:
 
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]

# i = 0
# found = False

# while i < len(numbers) and not found:
#     if numbers[i] == 0:
#         print('Нашли на итерации:', i+1)
#         found = True
#     i += 1

# print('Всего итераций выполнено:', i)   

# время

# import random
# import datetime


# value = 10
# fake_list = []

# for _ in range(1000000):
#     fake_list.append(random.randint(0, 1000))

# start = datetime.datetime.now()
# found = False
# for number in fake_list:
#     if number == value:
#         found = True
# print(found)
# print(datetime.datetime.now() - start)

# start = datetime.datetime.now()
# found = False
# i = 0
# while i < len(fake_list) and not found:
#     if fake_list[i] == value:
#         found = True
#     i += 1
# print(found)
# print(datetime.datetime.now() - start)

# Чситка коллекции

letters = ['a', 'b', 'c', 'd', 'e', 'f', ]

for letter in letters:
    letters.remove(letter)

print('Список после чистки: ', letters)  