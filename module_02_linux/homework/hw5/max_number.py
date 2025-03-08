"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    list_numbers = numbers.split('/')
    list_digits = []
    error_list = []
    for number in list_numbers:
        try:
            digit = int(number)
            list_digits.append(digit)
        except ValueError:
            error_list.append(number)
    result = f'Максимальное число: <i>{max(list_digits)}</i>.' if list_digits else 'Пользователь не передал чисел.'
    result_error = f'Некорректные данные, которые передал пользователь: <i>{", ".join(error_list)}</i>' if error_list else None
    return f'<h2>{result}</h2>' if result_error is None else f'<h2>{result}<br>{result_error}</h2>'


if __name__ == "__main__":
    app.run(debug=True)
