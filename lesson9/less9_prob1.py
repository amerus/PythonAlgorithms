'''
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
не решённой.
'''

import hashlib


def rubin_karp(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) >= len(subs), 'Подстрока должна состоять в строке'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()
    counter = 0

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            counter += 1

    return counter

s_1 = input('Введите строку: ')
s_2 = input('Введите подстроку поиска: ')

pos = rubin_karp(s_1, s_2)

print(f'Подстрока найдена {pos} раз(а).' if pos != 0 else f'Подстрока {s_2} не найдена.')
