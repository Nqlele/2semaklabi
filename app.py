from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <main>
            <div>
                <ol>
                    <li>
                        <a href="/lab1">Первая лабораторная</a>
                    </li>
                </ol>
            </div>
        </main>

        <footer>
            &copy; Еремин Захар Дмитриевич, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Еремин Захар Дмитриевич. Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <div style="margin: 10px 0;">
            Flask — фреймворк для создания веб-приложений на языке<br>
            программирования Python, использующий набор инструментов<br>
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так<br>
            называемых микрофреймворков — минималистичных каркасов<br>
            веб-приложений, сознательно предоставляющих лишь самые ба-<br>
            зовые возможности.
        </div>
        <a href="/menu">Меню</a>

        <h2>Реализованные роуты</h2>

        <div style="margin: 10px 0;">
            <ul>
                <li><a href="/lab1/oak">/lab1/oak - Дуб</a></li>
                <li><a href="/lab1/student">/lab1/student - Студент</a></li>
                <li><a href="/lab1/python">/lab1/python - Python</a></li>
                <li><a href="/lab1/monesy">/lab1/monesy - Монеси</a></li>
            <ul>
        </div>
            
        <footer>
            &copy; Еремин Захар, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

@app.route("/lab1/oak")
def oak():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Дуб</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <div>
                <h1>Дуб</h1>
                <img src="''' + url_for('static', filename='oak.jpg') + '''">
            </div>
        </main>
        <footer>
            &copy; Еремин Захар, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Студент</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div>
                <h1>Еремин Захар Дмитриевич</h1>
                <img src="''' + url_for('static', filename='ngtu.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Еремин Захар, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Python</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div style="width: 85%; height: auto; margin: 0 auto;">
                <h1>Python</h1>

                <p>
                    <b>Python</b> — это скриптовый язык программирования. Он универсален, поэтому подходит для решения разнообразных задач и для многих платформ: начиная с iOS и Android и заканчивая серверными операционными системами.
                </p>

                <h2>Как и где применяется Python</h2> 

                <p>
                    Это интерпретируемый язык, а не компилируемый, как C++ или Java. Программа на Python представляет собой обычный текстовый файл. Код можно писать практически в любом редакторе или использовать специальные IDE:
                </p>

                <ol>
                    <li>PyCharm — мощная среда разработки от JetBrains.</li>
                    <li>Spyder — IDE, оптимизированная для работы в Data Science. Идёт в пакете с Anaconda.</li>
                    <li>IDLE — стандартный текстовый редактор в составе языка.</li>
                    <li>SublimeText — текстовый редактор с множеством плагинов.</li>
                    <li>Visual Studio Code — популярный текстовый редактор от Microsoft.</li>
                </ol>

                <p>
                    Python можно встретить почти везде: в вебе, мобильных и десктопных приложениях, а также в играх. На нём пишут нейросети, проводят научные исследования и тестируют программы. Поговорим подробнее об основных сферах его применения.
                </p>
            </div>
            <div>
                <img src="''' + url_for('static', filename='pyth.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Еремин Захар, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''

@app.route("/lab1/monesy")
def monesy():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
        <title>Лабораторная 1. Илья "monesy" Осипов </title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <main>
            <div style="width: 85%; height: auto; margin: 0 auto;">
                <h1>Монеси</h1>

                <p>
                    Думаю, для игрока его возраста у m0NESY действительно большой потенциал.

                </p>

                <p>
                    Учитывая его показатели, даже если поначалу он не сможет выступать так же хорошо на тир-1 уровне, в будущем, набравшись опыта, он сможет стать одним из лучших игроков в истории.
                </p>

                <p>
                    В 2024 году Илья всерьез претендует на звание лучшего игрока года по версии HLTV
                </p>

                <h2>Личная жизнь</h2>

                <p>
                    Монеси встречается с девушкой стримершей по контер-страйку turboxgirl , они часто проводят время как в игре так и вне ее.
                </p>
            </div>
            <div>
                <img src="''' + url_for('static', filename='monesy.jpg') + '''">
            </div>
        </main>

        <footer>
            &copy; Еремин Захар, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
'''
@app.route('/lab2/a')
def a():
    return 'без слэша'
@app.route('/lab2/a/')
def a2():
    return 'со слэшем'
flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
@app.route('/lab2/flowers/<int:flower_id>')
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
@app.route('/lab2/add_flower/<name>')
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
@app.route('/lab2/add_flower/')
def add_flower_without_name():
    return 'нет имени цветка', 400
@app.route('/lab2/flowers/')
def list_flowers():
    flower_count = len(flower_list)
    return render_template('flowers.html', flower_list=flower_list, flower_count=flower_count)
@app.route('/lab2/clear_flowers/')
def clear_flowers():
    flower_list.clear() 
    return f'''
<!doctype html>
<html>
    <body>
        <h1>Список цветов очищен</h1>
        <p>Все цветы были удалены из списка&#128532;</p>
        <a href="/lab2/flowers/">Посмотреть все цветы</a>
    </body>
</html>
'''
@app.route('/lab2/example')
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
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')
@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
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
@app.route('/lab2/calc/')
def calc_default():
    return redirect('/lab2/calc/1/1')
@app.route('/lab2/calc/<int:a>')
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
@app.route('/lab2/books/')
def book_list():
    return render_template('books.html', books=books)
cars = [
    {"title": "Bmw", "description": "M5", "image": "m5.jpg"},
    {"title": "Bmw", "description": "X6", "image": "x6.jpg"},
    {"title": "Bmw", "description": "I8", "image": "i8.jpg"},
    {"title": "Bmw", "description": "M2", "image": "m2.jpg"},
    {"title": "Bmw", "description": "X1", "image": "x1.jpg"}
]
@app.route('/lab2/cars/')
def cars_list(): 
    return render_template('cars.html', cars=cars)