import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')


def get_word() -> list[str]:
    """Возвращает список слов из книги 'Война и мир'"""
    global BOOK_FILE
    array = []
    with open(BOOK_FILE, 'r', encoding='utf-8') as book:
        for line in book:
            line = re.findall(r'\b(?![IVXLCDM]+)[a-zA-Zа-яА-Яё]+\b', line)
            array.extend(line)
        return array


if __name__ == '__main__':
    print(get_word())
