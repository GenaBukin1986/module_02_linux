"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""
import os


def get_summary_rss(ps_output_file_path: str) -> str:
    """
    Возвращает суммарный объём потребляемой памяти в человекочитаемом формате

    Args:
        ps_output_file_path (str): Путь до файла.

    Returns:
        str: Размер в удобном формате с единицами измерения.
    """
    total_rss = get_total_rss(ps_output_file_path)
    return convert(total_rss)

def convert(units: int):
    """
    Конвертирует байты в человекочитаемый формат

    Args:
        units (int): Размер в байтах.

    Returns:
        str: Размер в удобном формате с единицами измерения.
    """
    if units < 2 ** 10:
        return f'{str(units)} Б'
    elif 2 ** 10 <= units < 2 ** 20:
        return f'{round(units / 2 ** 10, 1)} Kб'
    elif 2 ** 20 <= units < 2 ** 30:
        return f'{round(units / 2 ** 20, 1)} Mб'
    elif 2 ** 30 <= units < 2 ** 40:
        return f'{round(units / 2 ** 30, 1)} Гб'
    else:
        return f"{round(units / 2 ** 40, 1)} T"

def get_total_rss(path_file: str) -> int:
    """
    Возвращает суммарный объем потребляемой памяти в байтах

    Args:
        path_file (int): Путь до файла.

    Returns:
        int: Суммарный объём потребляемой памяти в байтах.
    """
    total_rss = 0
    with open(path_file, 'r', encoding='utf-8') as file:
        for id_line, data_line in enumerate(file, start=1):
            if id_line == 1:
                continue
            else:
                data = data_line.split()
                try:
                    digit_rss = int(data[5])
                    total_rss += digit_rss
                except Exception:
                    print(f'Ошибка! В столбце RSS в строке {id_line} находится не число!')
    return total_rss


if __name__ == '__main__':
    path: str = os.path.join(os.getcwd(), 'output_file.txt')
    summary_rss: str = get_summary_rss(path)
    print(f'Cуммарный объём потребляемой памяти: {summary_rss}')
