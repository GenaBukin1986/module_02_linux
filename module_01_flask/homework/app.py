import datetime
import random
from get_word import get_word

from flask import Flask

app = Flask(__name__)

list_cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
list_cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
book = get_word()


@app.route('/hello_world')
def get_hello_world():
    """Возвращает строку 'Привет, мир!'"""
    return '<h2>Привет, мир!</h2>'


@app.route('/cars')
def get_list_cars():
    """Возвращает случайно выбранную машину из списка машин"""
    global list_cars
    return f'<h2>Список машин:</h2>\n<h3>{", ".join(list_cars)}</h3>'


@app.route('/cats')
def get_random_cats():
    """Возвращает случайно выбранную породу кошек из списка пород"""
    global list_cats
    return f'<h2>Эта страница про кошек.</h2>\n' \
           f'<h3>Сегодня мы познакомимся с породой: {random.choice(list_cats)}</h3>'


@app.route('/get_time/now')
def get_time_now():
    """Возвращает точное время"""
    return f'<h2>Точное время: {datetime.datetime.now()}</h2>'


@app.route('/get_time/future')
def get_time_future():
    """Возвращает точное время через час"""
    current_time_after_hour = datetime.timedelta(hours=1)
    return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def get_random_word():
    """Возвращает случайное слово из книги 'Война и мир' Льва Толстого"""
    global book
    return f'<h2>Эта страница отображает случайное слово из книги "Война и мир" Льва Толстого</h2>\n' \
           f'<h3>Случайное слово из книги: <i>{random.choice(book)}</i></h3>'


@app.route('/counter')
def get_counter_page():
    """Возвращает сколько раз открывалась страница"""
    get_counter_page.visits += 1
    return f'Эта страница открывалась {get_counter_page.visits} раз'


get_counter_page.visits = 0

if __name__ == '__main__':
    app.run(debug=True)
