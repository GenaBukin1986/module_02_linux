"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    """
    сохранение информации о совершённой в рублях трате за какой-то день
    Args:
        date (str): За какой-то день.
        number (int): Сколько денег было потрачено за день.

    Returns:
        None.
    """
    try:
        year, month, day = int(date[:4]), int(date[4:6]), int(date[-2:])
        print(year, month, day)
        if year not in storage or (year in storage and month not in storage.get(year)):
            if year not in storage:
                storage.setdefault(year, {'total': 0})
            storage.setdefault(year, {}).setdefault(month, {})
            storage.get(year).get(month)[day] = number
            storage[year]['total'] += number
        elif not storage.get(year).get(month).get(day):
            storage.get(year).get(month)[day] = number
            storage[year]['total'] += number

        else:
            storage[year][month][day] += number
            storage[year]['total'] += number

    except TypeError:
        return f'<h2>Введены некорректные данные!<br>{date}</h2>'
    return f'За {day} {month} {year} потрачено {storage.get(year).get(month).get(day)} рублей'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    return f'<h2>За {year} год затраты составили: {storage.get(year)["total"]}</h2>' \
        if year in storage else \
        f'<h2>Указанного вами {year} года нет в базе данных!</h2>'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    result = 0

    if year in storage:
        if month in storage.get(year):
            for money in storage.get(year).get(month).values():
                result += money
            return f'<h2>За {month} {year} года затраты составили: {result}</h2>'
    else:
        return f'<h2>Указанного вами {year} года нет в базе данных!</h2>'

if __name__ == "__main__":
    app.run(debug=True)
