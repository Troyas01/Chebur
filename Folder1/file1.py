# Создаем список городов
cities = ['Москва', 'Париж', 'Лондон']

# Выводим список городов до изменения
print(f'Список городов до изменения: {cities}')

# Вычисляем длину списка
new_list_len = len(cities)

# Итерируемся по списку городов
for i in range(new_list_len):
    # В каждой итерации в переменную i будет передаваться значение от 0 до 3 (длины списка)
    # Получаем элемент списка по индексу i и записываем в него новое значение, равное 'Город: ' + значение_элемента
    cities[i] = f'Город: {cities[i]}'


# Выводим список городов после изменения
print(f'Список городов после изменения: {cities}')