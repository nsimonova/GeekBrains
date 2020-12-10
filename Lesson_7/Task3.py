class Cell:
    def __init__(self, cellule_count):
        if cellule_count <= 0:
            print('Число ячеек клетки должно быть больше 0!')
            raise ValueError
        self.cellule_count = cellule_count

    def __str__(self):
        return f'Cell with {self.cellule_count} cellules'

    def __add__(self, other):
        return Cell(self.cellule_count + other.cellule_count)

    def __sub__(self, other):
        if self.cellule_count < other.cellule_count:
            print('Превышение допустимого числа ячеек клетки')
            raise ValueError
        return Cell(self.cellule_count - other.cellule_count)

    def __mul__(self, other):
        return Cell(self.cellule_count * other.cellule_count)

    def __truediv__(self, other):
        return Cell(self.cellule_count // other.cellule_count)

    def make_order(self, count_in_row):
        full_row_count = self.cellule_count // count_in_row
        last_row_elements_count = self.cellule_count % count_in_row
        result = ''
        for element in range(0, full_row_count):
            result += "*" * count_in_row + '\n'
        result += '*' * last_row_elements_count
        return result


big_cell = Cell(25)
small_cell = Cell(7)
print(big_cell + small_cell)
print(big_cell - small_cell)
print(big_cell * small_cell)
print(big_cell / small_cell)
print(big_cell.make_order(4))
