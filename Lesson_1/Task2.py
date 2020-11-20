# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
vvodSeconds = int(input('Введите время в секундах '))
hours = vvodSeconds // 3600
minutes = (vvodSeconds % 3600) // 60
seconds = (vvodSeconds % 3600) % 60
print('Время в формате чч:мм:сс %s:%s:%s:' % (hours, minutes, seconds))
