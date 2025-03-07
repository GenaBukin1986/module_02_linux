"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:
    """
    Возвращает средний размер файла в директории.

    Args:
        ls_output (str): Результат выполнения команды ls -l.

    Returns:
        float: Средний размер файла в директории в байтах .
    """
    total_size = 0
    total_file = 0
    data_file = ls_output.split('\n')[1:-1]
    if not data_file:
        return 0.0
    for id_line, data_line in enumerate(data_file, start=1):
        data = data_line.split()
        try:
            size_file = int(data[4])
            total_size += size_file
            total_file += 1
        except Exception:
            print(f'Ошибка! Строка {id_line} некорректна для вычисления!')
    return total_size / total_file


def convert(units: float) -> str:
    """
    Конвертирует байты в человекочитаемый формат

    Args:
        units (int): Размер в байтах.

    Returns:
        str: Размер в удобном формате с единицами измерения.
    """
    if units < 2 ** 10:
        return f'{round(units,1)} Б'
    elif 2 ** 10 <= units < 2 ** 20:
        return f'{round(units / 2 ** 10, 1)} Kб'
    elif 2 ** 20 <= units < 2 ** 30:
        return f'{round(units / 2 ** 20, 1)} Mб'
    elif 2 ** 30 <= units < 2 ** 40:
        return f'{round(units / 2 ** 30, 1)} Гб'
    else:
        return f"{round(units / 2 ** 40, 1)} T"


if __name__ == '__main__':
    data: str = sys.stdin.read()
    mean_size: float = get_mean_size(data)
    print(f'Средний размер файла в директории {convert(mean_size)}')
