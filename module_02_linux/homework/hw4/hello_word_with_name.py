"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/hello-world/<string:username>')
def hello_world(username: str):
    weekday = datetime.today().weekday()
    list_weekday = [
        'понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскреснья',
    ]
    good_word = [
        'Хорошего', 'Хорошей'
    ]
    result = f'{good_word[0]} {list_weekday[weekday]}' if weekday in [0, 1, 3,
                                                                      6] else f'{good_word[1]} {list_weekday[weekday]}'

    return f'<h2>Привет, {username.capitalize()}. {result}!</h2>'


if __name__ == '__main__':
    app.run(debug=True)
