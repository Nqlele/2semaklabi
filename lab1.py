from flask import Blueprint, url_for
lab1 = Blueprint('lab1', __name__)

@lab1.route("/lab1")
def lab():
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

@lab1.route("/lab1/oak")
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

@lab1.route("/lab1/student")
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

@lab1.route("/lab1/python")
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

@lab1.route("/lab1/monesy")
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