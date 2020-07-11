'''
Закодируйте любую строку по алгоритму Хаффмана.
'''

from collections import Counter


class MyNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def traverse(self, code, value):
        self.left.traverse(code, value + '0')
        self.right.traverse(code, value + '1')


class Leaf:
    def __init__(self, char):
        self.char = char

    def traverse(self, code, value):
        code[self.char] = ''.join(value)


def get_leaves(message: str) -> dict:
    '''
    Функция подсчитывает буквы и возвращает словарь объектов Leaf и подсчет каждой буквы
    '''
    each_letter = Counter(message)
    counted_leaves = {}
    for key, val in each_letter.items():
        counted_leaves[Leaf(key)] = val
    return counted_leaves


def huffman(start_string):
    # Создается список листьев
    items = [x for x in get_leaves(start_string).items()]
    # Цикл соединения узлов и листьев в дерево
    while len(items) >= 2:
        left_leaf = items.pop()
        right_leaf = items.pop()
        leaf_count = left_leaf[1] + right_leaf[1]
        _node = MyNode(left=left_leaf[0], right=right_leaf[0])
        # Добавляем кортежи из узлов и суммы листьев в список
        items.append((_node, leaf_count))
        # Сортируем список по сумме
        items.sort(key=lambda x: x[1], reverse=True)
    node = items.pop()[0]
    # Создаем таблицу
    huff_table = {}
    node.traverse(huff_table, '')
    # Кодируем сообщение
    code_bin = [huff_table[item] for item in start_string]
    # Возвращаем таблицу и кодировку
    return huff_table, code_bin


if __name__ == '__main__':
    to_encode = 'beep boop beer!'
    print(to_encode)
    print('*' * 55)
    code, code_bin = huffman(to_encode)
    for key, value in code.items():
        print("\t", key, "\t: ", value)
    print('*' * 55)
    print(*code_bin)
