'''
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''

N = 6

def matrix_of_friends(N):
    """
    Создаем матрицу размером в N и заполняем ее значениями.
    Диагональ содержит единицы, а остальные ячейки нули.
    """
    matrix = [[0] * N for _ in range(N)]

    for index, item in enumerate(matrix[:]):
        for inner, j in enumerate(item[:]):
            if index == inner:
                matrix[index][inner] = 1

    return matrix


friends = matrix_of_friends(N)

print('*' * 40)


def single_hand_shakes(friends):
    """
    Подсчитываем рукопожатия.
    Если значение ноль и рукопожатия еще не было, то меняем значение на 1.
    """
    count = 0
    for index, item in enumerate(friends[:]):
        for inner, j in enumerate(item[:]):
            if j == 0 and inner > index:
                friends[index][inner] = 1
                count += 1
        print(index, item)
    return friends, count


friends, count = single_hand_shakes(friends)
print('*' * 40)
print(f"Если встретились {N} друзей, то рукопожатий было {count}.")
