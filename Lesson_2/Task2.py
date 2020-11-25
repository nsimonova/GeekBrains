# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
elements = input('Введите элементы списка через запятую ').split(',')
index = 0
while index < len(elements) - 1:
    element_one = elements[index]
    element_two = elements[index + 1]
    elements[index] = element_two
    elements[index + 1] = element_one
    index = index + 2
print(elements)
