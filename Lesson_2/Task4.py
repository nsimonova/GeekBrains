# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
new_string = input("Введите фразу ")
split_string = new_string.split()
for index, word in enumerate(split_string, 1):
    print(str(index) + '. ' + word[:10])
