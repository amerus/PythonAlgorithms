'''
Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''
import pprint


def dfs_route(graph, start, end, path=None):
    """Функция depth-first search"""
    if path is None:
        path = [start]
    if start == end:
        yield path
    for vertex in [item for item in graph[start] if item not in path]:
        yield from dfs_route(graph, vertex, end, path=(path + [vertex]))


def matrix_to_list(matrix):
    """Функция, генерирующая граф из матрицы вершин"""
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected:
                adj.append(j)
        graph[i] = adj
    return graph


def generate_graph(n: int) -> dict:
    """Функция, генерирующая матрицу по заданному количеству рядов"""
    matrix = [[0] * n for _ in range(n)]
    counter = 0
    for index, item in enumerate(matrix[:]):
        for inner, j in enumerate(item[:]):
            if index != inner:
                counter += 1
                if counter % 2 != 0:
                    matrix[index][inner] = 1
    return matrix_to_list(matrix)



n = int(input("Введите количество вершин: \t"))
start = int(input("Введите стартовую вершину поиска: \t"))
end = int(input("Введите конечную вершину поиска: \t"))
# Генерируем граф с шестью вершинами
adjacency_list = generate_graph(n)
# Распечатываем список смежности
print("Список смежности:")
pprint.pprint(adjacency_list)
print('*' * 40)
# Выводим на экран все пути алгоритма depth-first
print("Список возможных путей:")
pprint.pprint(list(dfs_route(adjacency_list, start, end)))
