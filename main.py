import unittest

import file_parser

# Задание 1

# Реализовать функцию:
# в которой все отрицательные элементы массива списка перенести в его начало, а все остальные – в конец,
# сохраняя исходное взаимное расположение как среди отрицательных, так и среди остальных элементов.
# Дополнительный список или массив не заводить


src = file_parser.read_list("files/input01.txt")


def transfer_numbers(source):
    index_step = 0
    for i in range(0, len(source), 1):
        if source[i] < 0:
            temp = source[i]
            source.remove(source[i])
            source.insert(index_step, temp)
            index_step += 1
    return source


class ListTestCase(unittest.TestCase):
    result_list_1 = [1, 2, 3, 7, 6, 99, 3]
    nums_1_1 = [1, 2, 3, 7, 6, 99, 3]

    result_list_2 = [-3, -5, -9, 1, 2, 3, 5, 4, 9, 0]
    nums_1_2 = [1, 2, 3, 5, 4, -3, -5, 9, 0, -9]

    result_list_3 = [-9, -8, -7, -4, 0, 9]
    nums_1_3 = [-9, -8, 0, -7, -4, 9]

    #false
    result_list_4 = [-9, -8, -7, -4, 0, 9]
    nums_1_4 = [-9, -8, 0, -7, -4, 9, 0]

    def test_1(self):
        assert self.result_list_1 == transfer_numbers(self.nums_1_1)

    def test_2(self):
        assert self.result_list_2 == transfer_numbers(self.nums_1_2)

    def test_3(self):
        assert self.result_list_3 == transfer_numbers(self.nums_1_3)

    # false
    def test_4(self):
        assert self.result_list_4 == transfer_numbers(self.nums_1_4)


data = file_parser.read_list("files/input01.txt")
file_parser.write_list_to_file(transfer_numbers(data), "files/output01.txt")

unittest.main()
