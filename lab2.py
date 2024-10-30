from flask import Blueprint, redirect, url_for, render_template, request
lab2 = Blueprint('lab2', __name__)
@lab2.route('/lab2/a')
def a():
    return 'без слэша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'
flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Ошибка 404</h1>
        <p>Цветка с таким номером нет</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
''', 404
    else:
        return f'''
<!doctype html>
<html>
    <body>
        <h1>Информация о цветке</h1>
        <p>Цветок: {flower_list[flower_id]}</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
'''
@lab2.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    </body>
</html>
'''
@lab2.route('/lab2/add_flower/')
def add_flower_without_name():
    return 'нет имени цветка', 400
@lab2.route('/lab2/flowers/')
def list_flowers():
    flower_count = len(flower_list)
    return render_template('flowers.html', flower_list=flower_list, flower_count=flower_count)
@lab2.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear() 
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список цветов очищен</h1>
        <p>Все цветы были удалены из списка;</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
'''
@lab2.route('/lab2/example')
def example():
    name, number_lab, group_student, number_course = 'Еремин Захар', 2, 'ФБИ-24', 3
    fruits = [
        {'name': 'яблоки', 'price': 121},
        {'name': 'груши', 'price': 161},
        {'name': 'апельсины', 'price': 132},
        {'name': 'мандарины', 'price': 228},
        {'name': 'манго', 'price': 322}
    ]
    return render_template('example.html', name=name, number_lab=number_lab,
                           group_student=group_student, number_course=number_course,
                           fruits=fruits)
@lab2.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b): 
    sum = a + b
    razn = a - b
    umn = a * b
    dele = a / b if b != 0 else 'деление на 0'
    step = a ** b
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Расчёт с параметрами:</h1>
        <p>Сумма: {a} + {b} = {sum}</p>
        <p>Разность: {a} - {b} = {razn}</p>
        <p>Умножение: {a} X {b} = {umn}</p>
        <p>Деление: {a} / {b} = {dele}</p>
        <p>Степень: {a}<sup>{b}</sup> = {step}</p>
    </body>
</html>
'''
@lab2.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')
@lab2.route('/lab2/calc/<int:a>')
def calc_redirect(a):
    return redirect(url_for('calc', a=a, b=1))
books = [
    {"author": "Чак Паланик", "title": "Бойцовский клуб", "genre": "Контркультура", "pages": 190},
    {"author": "Мерседес Рон", "title": "Слоновая кость", "genre": "Роман", "pages": 245},
    {"author": "Лев Толстой", "title": "Война и мир", "genre": "Роман", "pages": 1274},
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 640},
    {"author": "Надежда Мамаева", "title": "Ты просто огонь!", "genre": "Роман", "pages": 200},
    {"author": "Даня Зевс", "title": "Путь к победе", "genre": "Легенда", "pages": 200},
    {"author": "Николай Соболев", "title": "Путь к успеху", "genre": "Легенда", "pages": 150},
    {"author": "Иван Тургенев", "title": "Отцы и дети", "genre": "Роман", "pages": 432},
    {"author": "Беликов Вадим", "title": "Искусство курьера", "genre": "Стихи", "pages": 666},
    {"author": "Максим Горький", "title": "Мать", "genre": "Роман", "pages": 370}
]
@lab2.route('/lab2/books/')
def book_list():
    return render_template('books.html', books=books)
cars = [
    {"title": "Bmw", "description": "M5", "image": "m5.jpg"},
    {"title": "Bmw", "description": "X6", "image": "x6.jpg"},
    {"title": "Bmw", "description": "I8", "image": "i8.jpg"},
    {"title": "Bmw", "description": "M2", "image": "m2.jpg"},
    {"title": "Bmw", "description": "X1", "image": "x1.jpg"}
]
@lab2.route('/lab2/cars/')
def cars_list(): 
    return render_template('cars.html', cars=cars)