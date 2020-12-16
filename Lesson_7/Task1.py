class Matrix:
    def __init__(self, values):
        if type(values) != list:
            print('values должен быть списком')
            raise ValueError
        for row in values:
            if type(row) != list:
                print('элементы в values должны быть списком')
                raise ValueError
            if len(row) != len(values[0]):
                print('Все строки должны иметь равную длину')
                raise ValueError
        self.values = values

    def __str__(self):
        result = ''
        for row in self.values:
            result += " ".join(map(str, row)) + '\n'
        return result

    def __add__(self, other):
        if type(other) != Matrix:
            print('Можно складывать только матрицы!')
            raise ValueError
        if len(self.values) != len(other.values):
            print('Число строк в матрицах не совпадает!')
            raise ValueError
        if len(self.values[0]) != len(other.values[0]):
            print('Число столбцов в матрицах не совпадает!')
            raise ValueError
        result = []
        for i, row in enumerate(self.values):
            new_row = []
            for j, element in enumerate(row):
                new_row.append(other.values[i][j] + element)
            result.append(new_row)
        return Matrix(result)


matrix = Matrix([[1, 4, 5], [4, 3, 6], [2, 9, 1]])
print(matrix)
matrix_two = Matrix([[7, 0, 1], [5, 2, 1], [5, 0, 7]])
print(matrix_two)
matrix_sum = matrix + matrix_two
print(matrix_sum)
